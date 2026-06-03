import json
from flask import Flask, jsonify, request
import matematica
from lista_errori import ERRORE_1
import time
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"messaggio": "Benvenuto nelle API di MilanoToday Geometry!"})

@app.route('/menu', methods=['GET'])
def ottieni_menu():
    try:
        with open('menu.json', 'r') as file:
            lista_forme = json.load(file)
            forme_pulite = [forma.split(" ")[1].capitalize() for forma in lista_forme]
            return jsonify({"opzioni_calcolo": forme_pulite})
    except FileNotFoundError:
        return jsonify({"errore": ERRORE_1}), 500

@app.route('/calcola/quadrato', methods=['POST'])
def calcola_quadrato():
    tempo_inizio = time.time()
    dati = request.get_json()
    if not dati or 'lato' not in dati:
        return jsonify({"errore": "Dati mancanti! Inserisci il 'lato'."}), 400
        
    lato = float(dati['lato'])
    area_calcolata = matematica.quadrato(lato)

    tempo_fine = time.time()
    durata_calcolo = tempo_fine - tempo_inizio
    
    print(f"il tempo impiegato del API è stato di {durata_calcolo}")

    return jsonify({
        "forma": "quadrato",
        "lato": lato,
        "area": area_calcolata
    })

@app.route('/calcola/cerchio', methods=['POST'])
def calcola_cerchio():
    tempo_inizo = time.time()
    dati = request.get_json()
    if not dati or 'raggio' not in dati:
        return jsonify({"errore": "Dati mancanti! Inserisci il 'raggio'."}), 400
        
    raggio = float(dati['raggio'])
    risultati = matematica.cerchio(raggio)

    tempo_fine = time.time()
    durata_calcolo = tempo_fine - tempo_inizo

    print(f"il tempo impiegato del API è stato di {durata_calcolo}")
    
    return jsonify({
        "forma": "cerchio",
        "raggio": raggio,
        "area": risultati["area"],
        "circonferenza": risultati["circonferenza"]
    })

@app.route('/calcola/triangolo/area', methods=['POST'])
def calcola_area_triangolo():
    tempo_inizio = time.time()
    dati = request.get_json()
    if not dati or 'base' not in dati or 'altezza' not in dati:
        return jsonify({"errore": "Dati mancanti! Servono 'base' e 'altezza'."}), 400
        
    base = float(dati['base'])
    altezza = float(dati['altezza'])
    area_calcolata = matematica.area_triangolo(base, altezza)

    tempo_fine = time.time()
    durata_calcolo = tempo_fine - tempo_inizio

    print(f"il tempo impiegato del API è stato di {durata_calcolo}")

    
    return jsonify({
        "forma": "triangolo",
        "tipo": "area",
        "base": base,
        "altezza": altezza,
        "area": area_calcolata
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)