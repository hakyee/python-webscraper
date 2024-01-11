import time
import csv
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

class web_scrap():

    def __init__(self, keywords):
        self.jobs_db = []
        self.keywords = keywords

    def keyword_scarp(self, page):
        for word in self.keywords:
            page.goto(f"https://www.wanted.co.kr/search?query={word}&tab=position")
            for x in range(5):
                time.sleep(5)
                page.keyboard.down("End")
            content = page.content()
            self.scrap(word, content)

    def scrap(self, word, content):
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
            location = job.find("span", class_="JobCard_location__2EOr5").text
            reward = job.find("span", class_="JobCard_reward__sdyHn").text
            job_data = {
                "title": title,
                "company_name": company_name,
                "location": location,
                "reward": reward,
                "link": link
            }
            self.jobs_db.append(job_data)
        self.write_csv(word)

    def write_csv(self, word):
        file = open(f"{word}.csv", "w", encoding="utf-8")
        writter = csv.writer(file)
        writter.writerow(self.jobs_db[0].keys())

        for job in self.jobs_db:
            writter.writerow(job.values())
        file.close()
        self.jobs_db.clear()

keywords = [
    "flutter",
    "next.js",
    "kotlin"
]

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

w_scrap = web_scrap(keywords)
w_scrap.keyword_scarp(page)

p.stop()