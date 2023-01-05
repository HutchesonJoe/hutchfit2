#!/usr/bin/env python3
"""
An application to generate random cardio workouts.
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("workoutsetup.html")

@app.route("/makeworkout", methods = ["POST", "GET"])
def makeworkout():
  if request.method == "POST":
    if request.form["length"]:
      return render_template("workout.html", length=request.form.get("length"))
    else:
      return redirect(url_for("index"))
  return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)