import pickle

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

if hasattr(model, "predict"):
    print("Função predict encontrada no modelo.")
else:
    print("Função predict não encontrada no modelo.")
