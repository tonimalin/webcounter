from flask import Flask, redirect, render_template
from counter import Counter
from flask import request

app = Flask(__name__)
cnt = Counter()

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increment", methods=["POST"])
def increment():
    cnt.increase()
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")

@app.route("/set", methods=["POST"])
def set():
    cnt.set(0)
    value = request.form.get("value", type=int)
    cnt.set(value)
    return redirect("/")
