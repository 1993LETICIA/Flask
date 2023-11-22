import requests

url = 'http://localhost:5000/api'
data = {
    "Posicao": 1,
    "Estado": "Minas Gerais",
    "Time": "Atlético Mineiro",
    "Pontos": 84,
    "Jogos": 38,
    "Vitorias": 26,
    "Empates": 6,
    "Derrotas": 6,
    "GolsMarcados": 67,
    "GolsSofridos": 34,
    "SaldoGols": 33,
    "Obs": "Fase de grupos da Copa Libertadores de 2022[a]"
}

r = requests.post(url, json=data)

result = r.json()
if "is_desempenho" in result:
    if result["is_desempenho"]:
        print("Este time teve um bom desempenho!")
   
        
    else:
        print("Este time teve um desempenho ruim.")
    
else:
    print("Erro na resposta.")
