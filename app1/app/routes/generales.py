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

    try:
        # requête GET vers l'API de wikidata
        reponse = requests.get(WIKIDATA_API_URL, params=params)
        reponse.raise_for_status()

        # Décodage des données JSON
        donnees = reponse.json()
        id_donnees = donnees.get('entites', {}).get(id, {})

        # Verifier si l'entité existe
        if id_donnees:
            return render_template("pages/retrieve_wikidata.html", 
                                   status_code=reponse.status_code,
                                   id_donnees=id_donnees, 
                                   wikidata_id=id,
                                   content_type=reponse.headers.get('content-type'))
        # message d'erreur si l'entité n'existe pas
        else:
            return render_template("pages/retrieve_wikidata.html", 
                                   status_code=reponse.status_code,
                                   content_type=reponse.headers.get('content-type'),
                                   error_message=f"Aucune donnée valide n'a été retournée pour l'ID \"{id}\".")
    
    except requests.exceptions.RequestException as e:
            return render_template("pages/retrieve_wikidata.html", 
                                    status_code=500,
                                    error_message=str(e))