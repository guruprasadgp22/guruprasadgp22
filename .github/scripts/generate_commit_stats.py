import os
import requests
from datetime import datetime, timedelta, timezone

USERNAME = os.environ.get("GITHUB_USERNAME", "GuruprasadGP22")
TOKEN = os.environ.get("GITHUB_TOKEN", "")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.cloak-preview+json",
}

def get_last_30_days():
    today = datetime.now(timezone.utc).date()
    return [(today - timedelta(days=i)) for i in range(29, -1, -1)]

def fetch_commits_last_30_days(days):
    since = days[0].isoformat() + "T00:00:00Z"
    until = days[-1].isoformat() + "T23:59:59Z"
    count_map = {d.isoformat(): 0 for d in days}

    page = 1
    while page <= 10:
        url = (
            f"https://api.github.com/search/commits"
            f"?q=author:{USERNAME}+committer-date:{days[0].isoformat()}..{days[-1].isoformat()}"
            f"&sort=committer-date&order=desc&per_page=100&page={page}"
        )
        resp = requests.get(url, headers=HEADERS)
        if not resp.ok:
            print(f"GitHub API error: {resp.status_code} - {resp.text}")
            break

        data = resp.json()
        items = data.get("items", [])
        for item in items:
            date_str = (
                item["commit"].get("committer", {}).get("date", "")
                or item["commit"].get("author", {}).get("date", "")
            )[:10]
            if date_str in count_map:
                count_map[date_str] += 1

        if len(items) < 100 or len(items) == 0:
            break
        page += 1

    return count_map

def bar(count, max_count, width=20):
    if max_count == 0:
        filled = 0
    else:
        filled = round((count / max_count) * width)
    return "█" * filled + "░" * (width - filled)

def generate_stats_block(days, count_map):
    total = sum(count_map.values())
    active_days = sum(1 for v in count_map.values() if v > 0)
    max_count = max(count_map.values(), default=1) or 1
    best_day = max(count_map, key=count_map.get)
    avg = round(total / active_days, 1) if active_days else 0

    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines = [
        "## 📊 Daily Commit Stats — Last 30 Days",
        "",
        f"> 🕒 Last updated: `{updated}`",
        "",
        "```",
        f"  Total commits   : {total}",
        f"  Active days     : {active_days} / 30",
        f"  Avg per day     : {avg}",
        f"  Best day        : {best_day}  ({count_map[best_day]} commits)",
        "```",
        "",
        "| Date       | Day | Commits | Bar                      |",
        "|------------|-----|---------|--------------------------|",
    ]

    for d in days:
        iso = d.isoformat()
        count = count_map.get(iso, 0)
        weekday = d.strftime("%a")
        b = bar(count, max_count, width=20)
        count_str = str(count) if count > 0 else "·"
        lines.append(f"| {iso} | {weekday} | {count_str:>7} | `{b}` |")

    lines.append("")
    lines.append("> ⚡ Auto-updated every day via GitHub Actions")
    return "\n".join(lines)

def update_readme(stats_block):
    readme_path = "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- COMMIT_STATS_START -->"
    end_marker = "<!-- COMMIT_STATS_END -->"

    if start_marker not in content or end_marker not in content:
        print("Markers not found in README.md — appending at the end.")
        content += f"\n\n{start_marker}\n{stats_block}\n{end_marker}\n"
    else:
        start_idx = content.index(start_marker) + len(start_marker)
        end_idx = content.index(end_marker)
        content = content[:start_idx] + "\n" + stats_block + "\n" + content[end_idx:]

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)

    print("README.md updated successfully.")

if __name__ == "__main__":
    print(f"Fetching commits for: {USERNAME}")
    days = get_last_30_days()
    count_map = fetch_commits_last_30_days(days)
    stats_block = generate_stats_block(days, count_map)
    print("\nGenerated stats:\n")
    print(stats_block)
    update_readme(stats_block)
