import requests
from bs4 import BeautifulSoup

url = "https://chweyun-archive.vercel.app"
endpoint = "/posts"
latest_posts = []
MAX_POST = 5
count = 0

response = requests.get(url + endpoint)
soup = BeautifulSoup(response.text, 'html.parser')
post_elements = soup.select("a[href^='/posts']")

def extract_post(li):
    global latest_posts, count

    for i in li:
        if count >= MAX_POST:
            break

        title = i.select_one("h2")
        title_text = title.get_text(strip=True) if title else "No Title"

        link = i.get("href")

        time = i.select_one("span")
        time_text = time.get_text(strip=True) if time else "No Time"

        latest_posts.append(f" - [{time_text}  |  {title_text}]({url}{link})")
        count += 1

for idx, post in enumerate(post_elements):
    post_li = post.parent("li")
    if post_li:
        post_data = post.parent("a")
        extract_post(post_data)
        break

# 기존 README 내용
preREADME = """
![Chweyun's GitHub stats](https://github-readme-stats.vercel.app/api?username=chweyun&show_icons=true&theme=panda)
"""

# 결과 생성
resultREADME = "## ✅ Latest Blog Post\n" + "\n".join(latest_posts)

# README.md 파일로 저장
with open("README.md", "w", encoding='utf-8') as f:
    f.write(preREADME + resultREADME)
