#flask vid: https://www.youtube.com/watch?v=Z1RJmh_OqeA
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")

def main():
  return render_template("main.html")

def testing():
  if request.method == "POST":
    thing = request.form["input"]
    return render_template("index.html", thing = thing)


if (__name__ == "__main__"):
  app.run(debug=True)