#!/usr/bin/env python3
"""
벨로그 자동 잔디 심기
- 벨로그 RSS를 파싱하여 새 글을 마크다운으로 저장
- GitHub Actions에서 자동 실행되어 잔디를 심음
"""

import hashlib
import os
import re
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request
from xml.etree import ElementTree


POSTS_DIR = Path("posts")


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
    # 한글, 영문, 숫자만 남기고 나머지는 하이픈으로
    text = re.sub(r"[^\w\s가-힣-]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"-+", "-", text)
    return text[:50]  # 파일명 길이 제한


def get_post_hash(link: str) -> str:
    """글 링크의 해시를 생성합니다."""
    return hashlib.md5(link.encode()).hexdigest()[:8]


def get_existing_post_hashes(posts_dir: Path) -> set[str]:
    """기존 포스트 파일에서 해시 목록을 추출합니다."""
    hashes = set()
    if not posts_dir.exists():
        return hashes

    for file in posts_dir.glob("*.md"):
        content = file.read_text(encoding="utf-8")
        # url 필드에서 링크 추출
        match = re.search(r"url:\s*(.+)", content)
        if match:
            link = match.group(1).strip()
            hashes.add(get_post_hash(link))

    return hashes


def save_post_as_markdown(post: dict, posts_dir: Path) -> bool:
    """포스트를 마크다운 파일로 저장합니다."""
    posts_dir.mkdir(parents=True, exist_ok=True)

    slug = slugify(post["title"])
    filename = f"{post['date']}-{slug}.md"
    filepath = posts_dir / filename

    # HTML 태그 제거 (간단한 처리)
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
    return True


def main():
    """메인 함수: RSS를 가져와서 새 글을 저장합니다."""
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

    existing_hashes = get_existing_post_hashes(POSTS_DIR)
    new_count = 0

    for post in posts:
        post_hash = get_post_hash(post["link"])
        if post_hash not in existing_hashes:
            save_post_as_markdown(post, POSTS_DIR)
            new_count += 1

    if new_count == 0:
        print("새로운 글이 없습니다.")
    else:
        print(f"{new_count}개의 새 글이 저장되었습니다.")


if __name__ == "__main__":
    main()
