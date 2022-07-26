from flask import Blueprint, render_template
from Game import getcard
views = Blueprint(__name__, "views")

@views.route("/")
def home ():
    return render_template("index.html", card=getcard())


@views.route("/rules")
def rules():
    return  render_template("rules.html")