#!/usr/bin/env python3
"""Auto-update the featured post, post count, RSS feed, and sitemap.

Reads the first post card in the grid (newest post), pulls takeaway
headings from the actual post HTML, and rewrites the featured section.
Also syncs the "N Posts" counter, generates feed.xml and sitemap.xml.
"""

import datetime
import os
import re
import sys
from pathlib import Path

SITE_URL = "https://ogkranthi.github.io"

MONTH_MAP = {
    "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
    "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
}

CARD_PATTERN = re.compile(
    r'<article\s+class="post-card[^"]*"[^>]*'
    r"onclick=\"window\.location\.href='([^']+)'\""
    r'[^>]*>'
    r'.*?<h3>(.*?)</h3>'
    r'.*?<p\s+class="post-excerpt">(.*?)</p>'
    r'.*?<span\s+class="post-date">(.*?)</span>'
    r'.*?</article>',
    re.DOTALL,
)


def extract_first_card(html):
    """Extract info from the first post-card in the posts-grid."""
    m = CARD_PATTERN.search(html)
    if not m:
        return None
    return {
        "href": m.group(1).strip(),
        "title": m.group(2).strip(),
        "excerpt": m.group(3).strip(),
        "date_line": m.group(4).strip(),
    }


def extract_all_cards(html):
    """Extract all post cards from index.html."""
    cards = []
    for m in CARD_PATTERN.finditer(html):
        href = m.group(1).strip()
        if href == "#":
            continue
        cards.append({
            "href": href,
            "title": m.group(2).strip(),
            "excerpt": m.group(3).strip(),
            "date_line": m.group(4).strip(),
        })
    return cards


def current_featured_href(html):
    """Return the href the featured card currently points to."""
    m = re.search(
        r"<div\s+class=\"featured-card\"\s+onclick=\"window\.location\.href='([^']+)'\"",
        html,
    )
    return m.group(1) if m else None


def extract_takeaways(post_html, count=3):
    """Extract first N article h2 headings as takeaway points."""
    skip = {
        "follow the research",
        "related reading",
        "subscribe",
        "references",
    }
    headings = re.findall(r"<h2>([^<]+)</h2>", post_html)
    result = []
    for h in headings:
        clean = h.strip()
        if clean.lower() not in skip and not clean.lower().startswith("conclusion"):
            result.append(clean)
        if len(result) == count:
            break
    # Pad if the post has fewer than 3 qualifying h2s
    while len(result) < count:
        result.append("Deep technical analysis and practical implications")
    return result


def count_post_cards(html):
    return len(re.findall(r'<article\s+class="post-card', html))


def build_featured_section(card, takeaways):
    return (
        '<section class="featured reveal" id="writing">\n'
        f"  <div class=\"featured-card\" onclick=\"window.location.href='{card['href']}'\">\n"
        '    <div class="featured-left">\n'
        '      <div class="featured-label">Featured Essay</div>\n'
        f"      <h3>{card['title']}</h3>\n"
        f"      <p class=\"featured-excerpt\">{card['excerpt']}</p>\n"
        '      <div class="post-footer" style="margin-top:1.5rem">\n'
        f"        <span class=\"post-date\">{card['date_line']} read</span>\n"
        '        <span class="post-read">Read essay \u2192</span>\n'
        "      </div>\n"
        "    </div>\n"
        '    <div class="featured-right">\n'
        '      <div class="featured-takeaway">\n'
        '        <span class="featured-takeaway-num">01</span>\n'
        f"        <p>{takeaways[0]}</p>\n"
        "      </div>\n"
        '      <div class="featured-takeaway">\n'
        '        <span class="featured-takeaway-num">02</span>\n'
        f"        <p>{takeaways[1]}</p>\n"
        "      </div>\n"
        '      <div class="featured-takeaway">\n'
        '        <span class="featured-takeaway-num">03</span>\n'
        f"        <p>{takeaways[2]}</p>\n"
        "      </div>\n"
        "    </div>\n"
        "  </div>\n"
        "</section>"
    )


def escape_xml(text):
    """Escape XML special characters."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def parse_post_date(date_line):
    """Parse 'Mar 2026 · 15 min' into an RFC 822 date string."""
    m = re.match(r"(\w+)\s+(\d{4})", date_line)
    if not m:
        return ""
    month_str, year = m.group(1), int(m.group(2))
    month = MONTH_MAP.get(month_str, 1)
    dt = datetime.datetime(year, month, 1, tzinfo=datetime.timezone.utc)
    return dt.strftime("%a, %d %b %Y %H:%M:%S +0000")


def generate_feed(html):
    """Generate feed.xml from post cards in index.html."""
    cards = extract_all_cards(html)
    if not cards:
        print("No real post cards found, skipping feed generation")
        return

    items = []
    for card in cards:
        pub_date = parse_post_date(card["date_line"])
        date_tag = f"\n      <pubDate>{pub_date}</pubDate>" if pub_date else ""
        items.append(
            f"    <item>\n"
            f"      <title>{escape_xml(card['title'])}</title>\n"
            f"      <link>{SITE_URL}/{card['href']}</link>\n"
            f"      <guid>{SITE_URL}/{card['href']}</guid>\n"
            f"      <description>{escape_xml(card['excerpt'])}</description>"
            f"{date_tag}\n"
            f"    </item>"
        )

    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
        "  <channel>\n"
        "    <title>Kranthi Manchikanti</title>\n"
        f"    <link>{SITE_URL}</link>\n"
        f'    <atom:link href="{SITE_URL}/feed.xml" rel="self"'
        f' type="application/rss+xml"/>\n'
        "    <description>Technical deep-dives on AI Agents, AI Architectures,"
        " Reinforcement Learning, HITL frameworks, and AI safety.</description>\n"
        "    <language>en-us</language>\n"
        + "\n".join(items)
        + "\n"
        "  </channel>\n"
        "</rss>\n"
    )

    Path("feed.xml").write_text(feed, encoding="utf-8")
    print(f"feed.xml generated with {len(cards)} items")


def generate_sitemap():
    """Generate sitemap.xml from HTML files on disk."""
    pages = ["index.html"]
    for f in sorted(Path(".").glob("*.html")):
        if f.name != "index.html":
            pages.append(f.name)

    entries = []
    for page in pages:
        path = Path(page)
        if not path.exists():
            continue
        mtime = datetime.datetime.fromtimestamp(
            os.path.getmtime(path), tz=datetime.timezone.utc
        )
        lastmod = mtime.strftime("%Y-%m-%d")
        entries.append(
            f"  <url>\n"
            f"    <loc>{SITE_URL}/{page}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"  </url>"
        )

    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(entries)
        + "\n"
        "</urlset>\n"
    )

    Path("sitemap.xml").write_text(sitemap, encoding="utf-8")
    print(f"sitemap.xml generated with {len(entries)} URLs")


def main():
    index_path = Path("index.html")
    html = index_path.read_text(encoding="utf-8")

    card = extract_first_card(html)
    if not card:
        print("No post cards found in index.html")
        return

    if card["href"] == "#":
        print("Newest card is a placeholder (#), skipping")
        return

    changed = False

    # ── Update featured section ──
    if current_featured_href(html) != card["href"]:
        post_path = Path(card["href"])
        if not post_path.exists():
            print(f"Post file {card['href']} not found, skipping featured update")
        else:
            post_html = post_path.read_text(encoding="utf-8")
            takeaways = extract_takeaways(post_html)
            new_section = build_featured_section(card, takeaways)
            html = re.sub(
                r'<section\s+class="featured\s+reveal"\s+id="writing">.*?</section>',
                new_section,
                html,
                flags=re.DOTALL,
            )
            changed = True
            print(f"Featured updated to: {card['title']}")
    else:
        print(f"Featured already points to {card['href']}")

    # ── Update post count ──
    post_count = count_post_cards(html)
    count_match = re.search(r'<span class="count">(\d+)\s+Posts</span>', html)
    if count_match:
        old_count = int(count_match.group(1))
        if old_count != post_count:
            html = re.sub(
                r'<span class="count">\d+\s+Posts</span>',
                f'<span class="count">{post_count} Posts</span>',
                html,
            )
            changed = True
            print(f"Post count updated: {old_count} -> {post_count}")

    if changed:
        index_path.write_text(html, encoding="utf-8")
        print("index.html written")
    else:
        print("No changes needed")

    # ── Generate feed and sitemap ──
    generate_feed(html)
    generate_sitemap()


if __name__ == "__main__":
    main()
