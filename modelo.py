import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

# Substitua 'seu_arquivo_brasileirao.csv' pelo nome real do seu arquivo do Brasileirão
brasileirao_data = pd.read_csv('Jogos.csv')

# Substituindo o caractere especial por um sinal de menos padrão
brasileirao_data['SG'] = brasileirao_data['SG'].replace('−', '-')

# Convertendo a coluna 'SG' para valores numéricos
brasileirao_data['SG'] = pd.to_numeric(brasileirao_data['SG'], errors='coerce')

# Adicionando a coluna 'Desempenho' baseada na mediana dos pontos
mediana_pontos = brasileirao_data['Pts'].median()
brasileirao_data['Desempenho'] = brasileirao_data['Pts'] > mediana_pontos

# Convertendo a coluna 'Desempenho' para valores booleanos
brasileirao_data['Desempenho'] = brasileirao_data['Desempenho'].astype(bool)

# Certifique-se de incluir todas as features necessárias
features = ['Pts', 'J', 'V', 'E', 'D', 'GP', 'GC', 'SG']
target = 'Desempenho'  # Coluna que representa o desempenho

# Se suas colunas forem diferentes, ajuste de acordo
X = brasileirao_data[features]
y = brasileirao_data[target]

# Dividindo os dados em conjunto de treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo
clf = DecisionTreeClassifier()
clf = clf.fit(X_treino, y_treino)

# Avaliando o modelo no conjunto de teste
preditos = clf.predict(X_teste)
accuracy = accuracy_score(y_teste, preditos)
print("Acuracia:", accuracy)

# Salvando o modelo treinado
pickle.dump(clf, open('model.pkl', 'wb'))
