# TODO APP
# -*- coding: utf-8 -*-
# import flask module and template.
from flask import Flask, request, render_template, redirect, url_for

# create flask object
app = Flask(__name__, template_folder="templates")

todos = [{"task": "todo 1", "done": False},
         {"task": "todo 2", "done": False},
         {"task": "todo 3", "done": False}]

@app.route("/")  # This decorator is needed to map the URL to the function
def index():
    """
    index function to render index.html
    """
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    app.run(debug=True)
