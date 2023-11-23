import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Carregar o modelo treinado
model = pickle.load(open('model.pkl', 'rb'))

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

# Rota para previsões
@app.route('/predict', methods=['POST'])
def predict():
    # Recuperar os dados do formulário
    int_features = [int(x) for x in request.form.values()]
    
    # Certificar-se de que há 7 características como no treinamento
    if len(int_features) != 7:
        return render_template('index.html', prediction_text='Erro: Forneça os dados corretos.')

    # Adicionar 'SG' com valor 0 (zero)
    int_features.append(0)

    final_features = pd.DataFrame([int_features], columns=['Pts', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG'])

    # Fazer a previsão
    prediction_proba = model.predict_proba(final_features)
    
    # Considerar desempenho maior que 50% como "bom" e menor ou igual a 50% como "ruim"
    if prediction_proba[0][1] > 0.5:
        prediction_text = 'Bom desempenho'
    else:
        prediction_text = 'Ruim desempenho'

    # Renderizar a página com os resultados
    return render_template('index.html', prediction_text=f'O desempenho previsto é {prediction_text}.')

if __name__ == '__main__':
    app.run(debug=True)
