from flask import Flask ,render_template
app=Flask(__name__)

posts=[
    {
        'author':'denis ligare',
        'date_posted':'2nd April 2020',
        'title':'the river and the source',
        'content':'sssljcsd hgfd jsdhdjsd'
    },
    {
        'author':'moureen Khavere',
        'date_posted':'2nd December 2020',
        'title':'Kit mikai',
        'content':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum '

    }
]

@app.route("/")
def index():
    return render_template("about.html",posts=posts)


@app.route("/about")
def about():
    return "hellow world!S here is about"


if __name__=="__main__":
    app.run(debug=True)