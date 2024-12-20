from ..app import app
from flask import request, render_template
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

    # Paramètres de la requête
    params = {
        "action": "wbgetentities",
        "ids": id,
        "format": "json",
        "languages": "fr"
    }

    # Appel de l'API
    data = requests.get(WIKIDATA_API_URL, params=params)
    # Récupération du JSON
    data = data.json()

    # Requête
    try:
        #return data (test)
        return render_template("pages/retrieve_wikidata.html")  # Renvoie les données de l'entité
    
# Message d'erreur si l'ID n'est pas valide

    except:
        return f"Aucune donnée valide n'a été retournée pour l'ID {id}"
