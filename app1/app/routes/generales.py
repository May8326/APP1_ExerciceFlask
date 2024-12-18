from ..app import app
from flask import render_template, request

@app.route("/pays/<string:nom>")
def pays(nom):
    return render_template("pages/pays.html", pays=nom)

@app.route("/retrieve_wikidata/<string:id>")
def retrieve_wikidata(id):
    return render_template("pages/retrieve_wikidata.html", id=id)