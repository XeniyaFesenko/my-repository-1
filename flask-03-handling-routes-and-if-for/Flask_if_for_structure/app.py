from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def head():
    first = "This is my first conditions experiece" 
    return render_template

@app.route("/gurkan")
def header ():
        numbers = range(1,11)
        render_template("body.html", object=numbers)


if __name__=="__main__":
    app.run(debug=True)