import feedparser

URL = "https://v2.velog.io/rss/chweyun"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

latest_posts = ""

for idx, entrie in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    feed_date = entrie['published_parsed']
    latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
## 기존의 README.md 내용
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
    f.write(resultREADME)
