import requests
from bs4 import BeautifulSoup

class Jobs():
    def __init__(self, header):
        self.header = header
        self.all_jobs = []

    def scrape_keyword(self, keyword):
        response = requests.get(f"https://remoteok.com/remote-{keyword}-jobs", headers={"User-Agent":self.header})      # remoteok 사이트는 일반적으로 접근 시 차단해버린다. 이를 해결하기 위해
        soup = BeautifulSoup(response.content, "html.parser")                                                           # 헤더내용을 직접 추가하여 웹으로 접근하는 척 속이며 접근하게 된다.
        jobs = soup.find("table", id="jobsboard").find_all("td", class_="company position company_and_position")[1:]
        for job in jobs:
            job_info = {
                "title": job.find("h2").text.strip('\n'),
                "company": job.find("span", class_="companyLink").text.strip('\n\xa0 '),
                "region": job.find("div", class_="location").text,
                "link": f"https://remoteok.com{job.find("a", class_="preventLink")["href"]}"
            }
            self.all_jobs.append(job_info)


keywords = ["flutter", "python", "golang"]

jobs_data = Jobs("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.18 Safari/537.36")

for word in keywords:
    jobs_data.scrape_keyword(word)
    print("================================================================", word, "================================================================")
    print(jobs_data.all_jobs, end="\n\n")