from flask import Flask , render_template

app = Flask(__name__)


JOBS = [
    {
        "id" : 1,
        "name" : "hridhu",
        "age" : 21
    },
    {
        "id" : 2,
        "name" : "aadi",
        "age" : 14
    },
    {
        "id" : 3,
        "name" : "hiran",
        "age" : 17
    }
]



@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS)
  

if __name__=="__main__":
    app.run(debug=True)