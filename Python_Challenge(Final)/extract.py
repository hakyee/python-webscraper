import requests
from bs4 import BeautifulSoup

header = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def extract_berlin_job(keyword):
    jobs_db = []
    response = requests.get(
            f"https://berlinstartupjobs.com/skill-areas/{keyword}", headers={"User-Agent": header})
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("li", class_="bjs-jlid")
    for job in jobs:
        job_data = {
            "Company": job.find("a", class_="bjs-jlid__b").text.strip(),
            "Title": job.find("h4", class_="bjs-jlid__h").text.strip(),
            "Link": job.find("h4", class_="bjs-jlid__h").find("a")["href"]
        }
        jobs_db.append(job_data)
    return jobs_db


def extract_web3_job(keyword):
    jobs_db = []
    response = requests.get(f"https://web3.career/{keyword}-jobs")
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("tr")[1:]
    for job in jobs:
        if "data-jobid" in job.attrs:
            job_data = {
                "Company": job.find("h3").text.strip(),
                "Title": job.find("h2").text.strip(),
                "Link": f"https://web3.career/{job.find("div", class_="job-title-mobile").find("a")["href"]}"
            }
            jobs_db.append(job_data)
    return jobs_db


def extract_wework_job(keyword):
    jobs_db = []
    response = requests.get(f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}")
    soup = BeautifulSoup(response.content, "html.parser")
    sections = soup.find_all("section", class_="jobs")
    for section in sections:
        jobs = section.find_all("li")[:-1]
        for job in jobs:
            job_data = {
                "Company": job.find("span", class_="company").text.strip(),
                "Title": job.find("span", class_="title").text.strip(),
                "Link": f"https://weworkremotely.com/{job.find_all("a")[1]["href"]}"
            }
            jobs_db.append(job_data)
    return jobs_db