import requests
from bs4 import BeautifulSoup

URL = "https://chweyun-archive.vercel.app/posts"
latest_posts = """
## ✅ Latest Blog Post
"""
MAX_POST = 5

# 웹페이지 요청 및 파싱
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

# 포스트 목록을 찾는 부분
post_elements = soup.select("section ul li")

# 최대 5개 포스트를 가져오기
for idx, post in enumerate(post_elements):
    if idx >= MAX_POST:
        break

    # 타이틀과 링크 추출
    title_tag = post.find("h2")
    title = title_tag.text.strip()

    link_tag = post.find("a")
    link = "https://chweyun-archive.vercel.app" + link_tag['href']

    # 시간 추출
    date_tag = post.find("span")
    post_date = date_tag.text.strip() if date_tag else "Unknown Date"

    # 포스트 정보를 최신 블로그 포스트 형식으로 추가
    latest_posts += f" - [{post_date} - {title}]({link})\n"

# 기존 README 내용
preREADME = """
![Chweyun's GitHub stats](https://github-readme-stats.vercel.app/api?username=chweyun&show_icons=true&theme=panda)
"""

# 결과 생성
resultREADME = f"{preREADME}{latest_posts}"

# README.md 파일로 저장
with open("README.md", "w", encoding='utf-8') as f:
    f.write(resultREADME)
