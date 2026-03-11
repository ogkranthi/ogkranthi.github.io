#!/usr/bin/env python3
"""Auto-update the featured post and post count in index.html.

Reads the first post card in the grid (newest post), pulls takeaway
headings from the actual post HTML, and rewrites the featured section.
Also syncs the "N Posts" counter.
"""

import re
import sys
from pathlib import Path


def extract_first_card(html):
    """Extract info from the first post-card in the posts-grid."""
    m = re.search(
        r'<article\s+class="post-card[^"]*"[^>]*'
        r"onclick=\"window\.location\.href='([^']+)'\""
        r'[^>]*>'
        r'.*?<h3>(.*?)</h3>'
        r'.*?<p\s+class="post-excerpt">(.*?)</p>'
        r'.*?<span\s+class="post-date">(.*?)</span>'
        r'.*?</article>',
        html,
        re.DOTALL,
    )
    if not m:
        return None
    return {
        "href": m.group(1).strip(),
        "title": m.group(2).strip(),
        "excerpt": m.group(3).strip(),
        "date_line": m.group(4).strip(),
    }


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


if __name__ == "__main__":
    main()
