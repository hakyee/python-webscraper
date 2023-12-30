from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)                 # 웹 사이트로부터 응답을 가져옴
    if response.status_code == 200:         # 각 번호마다 상태가 다름. 200은 정상상태
        results[website] = "OK"
    else:
        results[website] = "FAILED"

print(results)