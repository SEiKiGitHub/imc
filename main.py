import random

poids = random.randint(50,150)
taille = random.randint(150,203)

def imc(poids, taille, name):
    formule = poids / (taille / 100) ** 2

    if formule > 25:
        print(name)
        print(formule)
        print("Vous etes en surpoids")
        print("-" * 25)
    elif 18 < formule < 25:
        print(name)
        print(formule)
        print("Vous etes normal")
        print("-" * 25)
    elif formule < 18:
        print(name)
        print(formule)
        print("Vous etes en situation de maigreur")
        print("-" * 25)


imc(59,176,"Farrah")
imc(53,175,"Tom")
imc(58,172,"Wino")
imc(500,178,"L'homme le plus gros du monde")

imc(poids,taille,"Random")
print(poids, taille)
