import feedparser, time

URL = "https://v2.velog.io/rss/chweyun"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

latest_posts = """

## ✅ Latest Blog Post

"""

for idx, entrie in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    feed_date = entrie['published_parsed']
    latest_posts += f" - [{time.strftime('%Y/%m/%d', feed_date)} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
![Chweyun's GitHub stats](https://github-readme-stats.vercel.app/api?username=chweyun&show_icons=true&theme=panda)
"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
    f.write(resultREADME)
