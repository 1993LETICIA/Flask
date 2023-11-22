import pickle

# Carregar o modelo treinado
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Verificar se a função predict está definida no modelo
if hasattr(model, "predict"):
    print("Função predict encontrada no modelo.")
else:
    print("Função predict não encontrada no modelo.")
