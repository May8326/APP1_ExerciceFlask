from ..app import app
from flask import request, render_template
from ..config import WIKIDATA_API_URL
import requests


# définition de la route interroger l'API de wikidata
@app.route("/retrieve_wikidata/<id>", methods=["GET"])
def retrieve_wikidata(id):
    """
    Récupère les informations d'une entité Wikidata
    :param id: l'identifiant de l'entité Wikidata
    :type id: str   
    
    :return: le JSON de l'entité Wikidata
    """

    # Paramètres de la requête
    params = {
        "action": "wbgetentities",
        "ids": id,
        "format": "json"
    }

    # Récupération du JSON
    data = requests.get(WIKIDATA_API_URL, params=params)
    data_json = data.json()

    # Vérification des erreurs
    if "error" in data_json:

        # Récupère l'erreur
        error_message = data_json["error"]["info"]
        # Renvoie le HTML avec l'erreur
        return render_template(
            "pages/retrieve_wikidata.html",
            wikidata_id=id,
            status_code=data.status_code,
            content_type=data.headers.get("Content-Type"),
            error_message=error_message  # Transmettre l'erreur pour le HTML
        )
    
    # Si ma requête n'a pas renvoyé d'erreur
    else:
        # Renvoie le HTML avec le JSON
        return render_template("pages/retrieve_wikidata.html", 
                               wikidata_id = id,
                               status_code = data.status_code,
                               content_type = data.headers.get('Content-Type'), 
                               wikidata_json = data_json,
                               error_message = None) 
    
