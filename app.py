from flask import Flask, request, render_template
from plscanner import *

app = Flask(__name__, template_folder='.')

@app.route("/", methods=["GET", "POST"])

def index():
    result = None 
    if request.method == "POST":
        url = request.form["url"]
        result = phishing_scanner(url)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)