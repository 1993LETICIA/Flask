import numpy as np
from flask import Flask, render_template, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
     
        features = [float(request.form['Pontos']),
                    float(request.form['Jogos']), float(request.form['Vitorias']),
                    float(request.form['Empates']), float(request.form['Derrotas']),
                    float(request.form['GolsMarcados']), float(request.form['GolsSofridos'])]

        # Verificar se todos os campos estão presentes
        if None in features:
            raise ValueError("Dados incompletos.")

        # Realizar a previsão
        pred = model.predict([features])
        predicted_desempenho = pred[0] 

       
        # Adicione a lógica para determinar a classe com base nas probabilidades
        if predicted_desempenho == 1:  
            prediction_text = "Este time teve um bom desempenho!"
        else:
            prediction_text = "Este time teve um desempenho ruim."

        return render_template("index.html", prediction_text=prediction_text)

    except Exception as e:
        return render_template("index.html", prediction_text=f"Erro: preencha todos os campos.")

# Altere o trecho de código na rota /api para retornar HTML
@app.route("/api", methods=["POST"])
def api_predict():
    try:
        data = request.get_json()

        # Coletar dados do JSON
        pontos = float(data['Pontos'])
        jogos = float(data['Jogos'])
        vitorias = float(data['Vitorias'])
        empates = float(data['Empates'])
        derrotas = float(data['Derrotas'])
        gols_marcados = float(data['GolsMarcados'])
        gols_sofridos = float(data['GolsSofridos'])

      

        # Verificar se todos os campos estão presentes
        if None in [pontos, jogos, vitorias, empates, derrotas, gols_marcados, gols_sofridos]:
            raise ValueError("Dados incompletos.")

        # Realizar a previsão
        features = [pontos, jogos, vitorias, empates, derrotas, gols_marcados, gols_sofridos]
        pred_proba = model.predict([features])
        predicted_desempenho = pred[0] 

        return jsonify({"is_desempenho": bool(predicted_desempenho)})

    except Exception as e:
        return jsonify({"error": "Erro: preencha todos os campos."})


if __name__ == "__main__":
    app.run(debug=True)
