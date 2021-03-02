from flask import Flask 
app=Flask(__name__)

@app.route("/")
def index():
    return "hellow world!S"


@app.route("/about")
def about():
    return "hellow world!S here is about"


if __name__=="__main__":
    app.run(debug=True)