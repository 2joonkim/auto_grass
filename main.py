#!/usr/bin/env python3
"""
벨로그 자동 잔디 심기
- 벨로그 RSS를 파싱하여 새 글을 마크다운으로 저장
- 삭제된 글은 자동으로 삭제
- README.md에 글 목록 자동 업데이트
"""

import hashlib
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request
from xml.etree import ElementTree


POSTS_DIR = Path("posts")
README_PATH = Path("README.md")


def fetch_rss(username: str) -> str:
    """벨로그 RSS 피드를 가져옵니다."""
    url = f"https://v2.velog.io/rss/@{username}"
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_rss(xml_content: str) -> list[dict]:
    """RSS XML을 파싱하여 글 목록을 반환합니다."""
    root = ElementTree.fromstring(xml_content)
    posts = []

    for item in root.findall(".//item"):
        title = item.findtext("title", "")
        link = item.findtext("link", "")
        description = item.findtext("description", "")
        pub_date = item.findtext("pubDate", "")

        # pubDate 파싱: "Mon, 30 Dec 2024 12:00:00 GMT" 형식
        date_str = ""
        if pub_date:
            try:
                dt = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %Z")
                date_str = dt.strftime("%Y-%m-%d")
            except ValueError:
                date_str = datetime.now().strftime("%Y-%m-%d")

        posts.append({
            "title": title,
            "link": link,
            "description": description,
            "date": date_str,
        })

    return posts


def slugify(text: str) -> str:
    """문자열을 파일명으로 사용할 수 있게 변환합니다."""
    text = re.sub(r"[^\w\s가-힣-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"-+", "-", text)
    return text[:50]


def get_post_hash(link: str) -> str:
    """글 링크의 해시를 생성합니다."""
    return hashlib.md5(link.encode()).hexdigest()[:8]


def get_existing_posts(posts_dir: Path) -> dict[str, Path]:
    """기존 포스트 파일에서 해시 -> 파일경로 매핑을 반환합니다."""
    posts = {}
    if not posts_dir.exists():
        return posts

    for file in posts_dir.glob("*.md"):
        content = file.read_text(encoding="utf-8")
        match = re.search(r"url:\s*(.+)", content)
        if match:
            link = match.group(1).strip()
            posts[get_post_hash(link)] = file

    return posts


def save_post_as_markdown(post: dict, posts_dir: Path) -> Path:
    """포스트를 마크다운 파일로 저장합니다."""
    posts_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(post["title"])
    filename = f"{post['date']}-{slug}.md"
    filepath = posts_dir / filename

    description = re.sub(r"<[^>]+>", "", post["description"])
    description = description.strip()

    content = f"""---
title: "{post['title']}"
date: {post['date']}
url: {post['link']}
---

## 요약

{description}

[원본 글 읽기]({post['link']})
"""

    filepath.write_text(content, encoding="utf-8")
    print(f"저장됨: {filename}")
    return filepath


def delete_post(filepath: Path) -> None:
    """포스트 파일을 삭제합니다."""
    if filepath.exists():
        print(f"삭제됨: {filepath.name}")
        filepath.unlink()


def sync_posts(posts: list[dict], posts_dir: Path) -> tuple[int, int]:
    """RSS와 로컬 파일을 동기화합니다. (추가/삭제)"""
    existing_posts = get_existing_posts(posts_dir)
    rss_hashes = {get_post_hash(post["link"]) for post in posts}

    new_count = 0
    deleted_count = 0

    # 새 글 추가
    for post in posts:
        post_hash = get_post_hash(post["link"])
        if post_hash not in existing_posts:
            save_post_as_markdown(post, posts_dir)
            new_count += 1

    # 삭제된 글 제거
    for post_hash, filepath in existing_posts.items():
        if post_hash not in rss_hashes:
            delete_post(filepath)
            deleted_count += 1

    return new_count, deleted_count


def generate_readme(posts: list[dict], username: str) -> None:
    """README.md를 생성합니다."""
    # 날짜순 정렬 (최신순)
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)

    content = f"""# Velog Auto Grass

> **@{username}**의 벨로그 글이 자동으로 동기화됩니다.

## 글 목록

| 날짜 | 제목 |
|------|------|
"""

    for post in sorted_posts:
        title = post["title"].replace("|", "\\|")
        content += f"| {post['date']} | [{title}]({post['link']}) |\n"

    content += f"""
---

*마지막 업데이트: {datetime.now().strftime("%Y-%m-%d %H:%M")} UTC*
"""

    README_PATH.write_text(content, encoding="utf-8")
    print("README.md 업데이트됨")


def main():
    """메인 함수: RSS를 가져와서 동기화합니다."""
    username = os.environ.get("VELOG_USERNAME")

    if not username:
        print("오류: VELOG_USERNAME 환경변수가 설정되지 않았습니다.")
        print("사용법: VELOG_USERNAME=your_username python main.py")
        return

    print(f"벨로그 RSS 가져오는 중: @{username}")

    try:
        xml_content = fetch_rss(username)
    except Exception as e:
        print(f"RSS 가져오기 실패: {e}")
        return

    posts = parse_rss(xml_content)
    print(f"총 {len(posts)}개의 글 발견")

    new_count, deleted_count = sync_posts(posts, POSTS_DIR)

    if new_count == 0 and deleted_count == 0:
        print("변경사항 없음")
    else:
        if new_count > 0:
            print(f"{new_count}개의 새 글 추가됨")
        if deleted_count > 0:
            print(f"{deleted_count}개의 글 삭제됨")

    # README 업데이트
    generate_readme(posts, username)


if __name__ == "__main__":
    main()
