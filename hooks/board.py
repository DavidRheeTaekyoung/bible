"""메인 페이지 글 목록 — 빌드할 때 docs/ 를 훑어 게시판처럼 한 줄씩 만든다.

「**날짜**: YYYY-MM-DD」 줄이 있는 글만 오른다(템플릿은 뺀다).
docs/index.md 의 「<!-- 글목록 -->」 자리에 들어간다. 최신 글이 위.
"""
import re
from pathlib import Path

MARK = "<!-- 글목록 -->"
SKIP = {"템플릿.md", "index.md"}
DATE = re.compile(r"^\*\*날짜\*\*:\s*(\d{4})-(\d{2})-(\d{2})", re.M)
TITLE = re.compile(r"^#\s+(.+?)\s*$", re.M)


def _rows(docs_dir: Path):
    rows = []
    for p in docs_dir.rglob("*.md"):
        rel = p.relative_to(docs_dir).as_posix()
        if rel in SKIP:
            continue
        text = p.read_text(encoding="utf-8")
        d, t = DATE.search(text), TITLE.search(text)
        if not d or not t:
            continue
        cat = rel.split("/")[0] if "/" in rel else ""
        rows.append(("-".join(d.groups()), rel, cat, t.group(1)))
    # 날짜 내림차순, 같은 날짜는 경로순
    rows.sort(key=lambda r: r[1])
    rows.sort(key=lambda r: r[0], reverse=True)
    return rows


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "index.md" or MARK not in markdown:
        return markdown
    rows = _rows(Path(config["docs_dir"]))
    lines = ['<div class="board" markdown>', ""]
    for date, rel, cat, title in rows:
        title = title.replace("[", "\[").replace("]", "\]")
        lines.append(
            f'- <span class="board-date">{date[2:].replace("-", ".")}</span>'
            f'<span class="board-cat">{cat}</span>[{title}]({rel})'
        )
    lines += ["", "</div>", "", f'<p class="board-count">글 {len(rows)}편</p>']
    return markdown.replace(MARK, "\n".join(lines))
