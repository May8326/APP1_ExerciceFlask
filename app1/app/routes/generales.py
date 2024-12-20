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
        "format": "json"
    }

    # Récupération du JSON
    data = requests.get(WIKIDATA_API_URL, params=params)
    data_json = data.json()

    # définition des valeurs pour le jinja


    # Requête
    try:
        #return data ()
        return render_template("pages/retrieve_wikidata.html", 
                               wikidata_id = id,
                               status_code = data.status_code,
                               content_type = data.headers.get('Content-Type'), 
                               data_json = data_json)  # Renvoie les données de l'entité
    
# Message d'erreur si l'ID n'est pas valide
    
    except:
        return f"Aucune donnée valide n'a été retournée pour l'ID {id}"