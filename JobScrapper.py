import requests
from bs4 import BeautifulSoup

url ="https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser",)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

all_jobs = []

# job도 beatifulsoup의 object이므로 soup의 모든 기능을 사용할 수 있다.
for job in jobs:
    title = job.find("span", class_="title").text
    company, position, region = job.find_all("span", class_="company")
    url = job.find("div", class_="tooltip").next_sibling["href"]     # 만약 href가 없다면 url = None이 된다. |||   next_sibling : tooltip클래스 다음에 있는 a의 href를 찾아라는 뜻.
    job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region.text,
        "url": f"https://weworkremotely.com{url}"
    }
    all_jobs.append(job_data)

print(all_jobs)