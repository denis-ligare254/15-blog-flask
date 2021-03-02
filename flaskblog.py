from flask import Flask ,render_template
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("about.html")


@app.route("/about")
def about():
    return "hellow world!S here is about"


if __name__=="__main__":
    app.run(debug=True)