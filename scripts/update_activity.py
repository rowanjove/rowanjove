#!/usr/bin/env python3
"""
scripts/update_activity.py
自动获取 rowanjove 的 GitHub 公开项目最新动态并安全更新 README.md。
严格遵循纯标准库、无三方依赖、失败不破坏已有文件的稳健设计。
遵循“去 AI 味”准则：纯净文字排版，拒绝滥用 🚀⚡🔥 符号。
"""

import os
import sys
import re
import json
import urllib.request
import urllib.error
from datetime import datetime

USERNAME = "rowanjove"
README_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")
PROJECTS_DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "projects.json")

START_MARKER = "<!-- RECENT_ACTIVITY:START -->"
END_MARKER = "<!-- RECENT_ACTIVITY:END -->"


def load_project_taglines():
    """从 data/projects.json 加载已校对的项目中文短评，避免生硬机翻或空描述"""
    taglines = {}
    if os.path.exists(PROJECTS_DATA_PATH):
        try:
            with open(PROJECTS_DATA_PATH, "r", encoding="utf-8") as f:
                items = json.load(f)
                for it in items:
                    taglines[it["repo"].lower()] = it.get("tagline") or it.get("description", "")
        except Exception as e:
            print(f"[Warn] 读取 projects.json 失败: {e}", file=sys.stderr)
    return taglines


def make_request(url):
    """发起 GitHub API 请求，优先附带 GITHUB_TOKEN 以避免匿名限流"""
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Profile-Updater")
    req.add_header("Accept", "application/vnd.github.v3+json")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=12) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_recent_activities():
    """获取最近活跃的原创仓库与 Release 动态"""
    taglines = load_project_taglines()
    url = f"https://api.github.com/users/{USERNAME}/repos?sort=pushed&per_page=15"
    try:
        repos = make_request(url)
    except Exception as e:
        print(f"[Error] 获取用户仓库列表失败: {e}", file=sys.stderr)
        return None

    activities = []
    # 排除 profile 自身同名仓库及 fork 仓库
    filtered_repos = [
        r for r in repos
        if not r.get("fork", False)
        and r.get("name", "").lower() != USERNAME.lower()
        and not r.get("private", False)
    ]

    for repo in filtered_repos[:5]:
        repo_name = repo["name"]
        repo_url = repo["html_url"]
        pushed_at = repo.get("pushed_at", "")
        pushed_date = pushed_at[:10] if pushed_at else ""
        
        # 获取中文简述，优先从 projects.json 查找，其次使用 repo description
        short_desc = taglines.get(repo_name.lower()) or repo.get("description") or "独立开源工具"
        if len(short_desc) > 36:
            short_desc = short_desc[:34] + "..."

        # 尝试查询是否有最新 release
        release_tag = None
        try:
            rel_url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/releases/latest"
            rel_data = make_request(rel_url)
            if rel_data and "tag_name" in rel_data:
                release_tag = rel_data["tag_name"]
        except Exception:
            # 仓库无 release 属于正常情况
            pass

        if release_tag:
            activities.append(f"- **[{repo_name}]({repo_url})** — {short_desc} · `{release_tag}` ({pushed_date})")
        else:
            activities.append(f"- **[{repo_name}]({repo_url})** — {short_desc} ({pushed_date})")

    return activities


def update_readme(new_lines):
    if not os.path.exists(README_PATH):
        print(f"[Error] README 路径不存在: {README_PATH}", file=sys.stderr)
        return False

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find(START_MARKER)
    end_idx = content.find(END_MARKER)

    if start_idx == -1 or end_idx == -1 or start_idx >= end_idx:
        print(f"[Error] README 中未找到有效的 Marker 标记", file=sys.stderr)
        return False

    before = content[:start_idx + len(START_MARKER)]
    after = content[end_idx:]

    activity_content = "\n" + "\n".join(new_lines) + "\n"
    updated = before + activity_content + after

    if updated != content:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(updated)
        print("[Info] README.md 最近动态已更新成功！")
        return True
    else:
        print("[Info] 动态内容未发生变化，跳过写入。")
        return False


def main():
    print(f"[Info] 开始检查 @{USERNAME} 最近项目动态...")
    activities = fetch_recent_activities()
    if not activities:
        print("[Warn] 未获取到有效动态或遭遇限流，保持原内容不变。")
        sys.exit(0)

    success = update_readme(activities)
    print(f"[Info] 执行结束。更新状态: {success}")


if __name__ == "__main__":
    main()
