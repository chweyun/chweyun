import requests
from bs4 import BeautifulSoup

URL = "https://chweyun-archive.vercel.app/posts"
latest_posts = """
## ✅ Latest Blog Post
"""
MAX_POST = 5

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
post_elements = soup.select("a[href^='/posts']")
post_data = []
result = []

def extract_post(li):
    global latest_posts

    for i in li:
        title = i.select_one("h2")
        title_text = title.get_text(strip=True) if title else "No Title"

        link = i.get("href")

        time = i.select_one("span")
        time_text = time.get_text(strip=True) if time else "No Time"

        latest_posts += f" - [{time_text} - {title_text}]({link})\n"

for idx, post in enumerate(post_elements):
    if len(post_data) >= MAX_POST:
        break

    post_li = post.parent("li")
    if post_li:
        post_data = post.parent("a")
        extract_post(post_data)
        break

print(result)

# 기존 README 내용
preREADME = """
![Chweyun's GitHub stats](https://github-readme-stats.vercel.app/api?username=chweyun&show_icons=true&theme=panda)
"""

# 결과 생성
resultREADME = f"{preREADME}{latest_posts}"

# README.md 파일로 저장
with open("README.md", "w", encoding='utf-8') as f:
    f.write(resultREADME)
