from flask import Flask, render_template, request, redirect
import extract

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def hello():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    berlin = extract.extract_berlin_job(keyword)
    web3 = extract.extract_web3_job(keyword)
    wework = extract.extract_wework_job(keyword)
    jobs = berlin + web3 + wework
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("127.0.0.1", debug=True)