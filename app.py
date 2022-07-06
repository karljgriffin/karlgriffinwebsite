from flask import Flask, render_template, g,  redirect, url_for, request

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("kg.html")
    
@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/undergradmodules")
def undergradmodules():
    return render_template("undergradmodules.html")

@app.route("/postgradmodules")
def postgradmodules():
    return render_template("postgradmodules.html")

@app.route("/allmodules")
def allmodules():
    return render_template("allmodules.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/sport")
def sport():
    return render_template("sport.html")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
