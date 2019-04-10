from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/result",methods=["GET","POST"])
def find_urls():
    siteUrl = request.form["URL"]
    site_data = requests.get(siteUrl)
    soup = BeautifulSoup(site_data.content)
    links = []
    for a in soup.find_all('a', href=True):
        links.append(a['href'])
    return render_template("result.html",links = links)



if __name__ == "__main__":
    app.run(debug=True)