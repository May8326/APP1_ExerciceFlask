from ..app import app
from flask import render_template
from ..config import WIKIDATA_API_URL
import requests

"""
@app.route("/pays/<string:nom>")
def pays(nom):
    return render_template("pages/pays.html", pays=nom)
"""

# définition de la route interroger l'API de wikidata
@app.route("/retrieve_wikidata/<id>", methods=["GET"])
def retrieve_wikidata(id):
    params = {
        "action": "wbgetentities",
        "ids": id,
        "format": "json"
    }
    return render_template("pages/retrieve_wikidata.html")