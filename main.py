print("Bonjour...")
print("Je continue à modifier mon code")
# Portée des variable
#new*
def CalculerDouble(nombre):

    # Docstring : Définir ma fonction
    """
    Calcule le double d'un nombre
    :param nombre:
    :return: le double du nombre entré
    """
    # La portée de la variable « nombre » est limité à la fonction ou elle se trouve
    print(nombre)
    return nombre * 2

# Programme principal
# La variable « nombre_2 » à une portée globale (Elle est reconnu partout)
nombre_2 = 55
nombre = 60
resultat = CalculerDouble(2)

print("Résultat ", resultat)