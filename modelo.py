import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Dados fornecidos
dados_desempenho = {
    'Posicao': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'Estado': ['Minas Gerais', 'Rio de Janeiro', 'São Paulo', 'Ceará', 'São Paulo', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Goiás', 'São Paulo', 'Ceará', 'Rio Grande do Sul', 'São Paulo', 'Paraná', 'Mato Grosso', 'Rio Grande do Sul', 'Rio Grande do Sul', 'Bahia', 'Pernambuco', 'Santa Catarina'],
    'Time': ['Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'América Mineiro', 'Atlético Goianiense', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico Paranaense', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense'],
    'Pontos': [84, 71, 66, 58, 57, 56, 54, 53, 53, 50, 50, 48, 48, 47, 47, 46, 43, 43, 38, 15],
    'Jogos': [38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38],
    'Vitorias': [26, 21, 20, 17, 15, 14, 15, 13, 13, 12, 11, 12, 11, 13, 10, 11, 12, 11, 9, 1],
    'Empates': [6, 8, 6, 7, 12, 14, 9, 14, 14, 14, 17, 12, 15, 8, 17, 13, 7, 10, 11, 12],
    'Derrotas': [6, 9, 12, 14, 11, 10, 14, 11, 11, 12, 10, 14, 12, 17, 11, 14, 19, 17, 18, 25],
    'GolsMarcados': [67, 69, 58, 44, 40, 55, 38, 41, 33, 35, 39, 44, 31, 41, 34, 36, 44, 42, 24, 27],
    'GolsSofridos': [34, 36, 43, 45, 36, 46, 38, 37, 36, 40, 38, 42, 39, 45, 37, 44, 51, 51, 37, 67],
    'SaldoGols': [33, 33, 15, -1, 4, 9, 0, 4, -3, -5, 1, 2, -8, -4, -3, -8, -7, -9, -13, -40],
    'Obs': ['Fase de grupos da Copa Libertadores de 2022[a]', '', '', '', '', '', 'Segunda fase da Copa Libertadores de 2022', '','Fase de grupos da Copa Sul-Americana de 2022', '', '', '', '', 'Fase de grupos da Copa Libertadores de 2022[a]', 'Fase de grupos da Copa Sul-Americana de 2022', '', 'Rebaixados à Série B de 2022', '']
}

# Criar DataFrame
df = pd.DataFrame(dados_desempenho)

# Selecionando as colunas relevantes
features = ['Pontos', 'Jogos', 'Vitorias', 'Empates', 'Derrotas', 'GolsMarcados', 'GolsSofridos']
target = 'Desempenho'  # Nome da coluna para prever o desempenho

# Extraindo os recursos (features) e os rótulos (labels)
x = df[features]
y = df[target]

# Treinando um classificador de árvore de decisão
clf = DecisionTreeClassifier()
clf = clf.fit(x, y)

# Salvando o modelo treinado em um arquivo
pickle.dump(clf, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))
