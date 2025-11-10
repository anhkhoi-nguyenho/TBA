
def invteDeCommande():
    command = input()
    return command

# dicos ou tuples nommés ou même class
chambreMapping = {
    "batiment1" : chambreCommand1
    "batiment2" : chambreCommand2
    "batiment3" : chambreCommand3
    "batiment4" : chambreCommand4
    "batiment5" : chambreCommand5
}

chambreCommand1 = {
    "chambre1" : ["Command1", "Command2", "Command3", "Command4"]
    "chambre2" : ["Command1", "Command2", "Command3", "Command4"]
}

chambreCommand2 = {
    "chambre1" : ["Command1", "Command2", "Command3", "Command4"]
    "chambre2" : ["Command1", "Command2", "Command3", "Command4"]
}

chambreCommand3 = {
    "chambre1" : ["Command1", "Command2", "Command3", "Command4"]
    "chambre2" : ["Command1", "Command2", "Command3", "Command4"]
}

chambreCommand4 = {
    "chambre1" : ["Command1", "Command2", "Command3", "Command4"]
    "chambre2" : ["Command1", "Command2", "Command3", "Command4"]
}

chambreCommand5 = {
    "chambre1" : ["Command1", "Command2", "Command3", "Command4"]
    "chambre2" : ["Command1", "Command2", "Command3", "Command4"]
}


# Command mapping
# On utilise un autre fichier si nécessaire


def commandePossible(tuple pos_Joueur): # (batiment, chambre)
    
    batiment, chambre = pos_Joueur

    try:
        dicoCommande = chambreMapping[batiment]
    except:
        print("Erreur inattendue : position du joueur invalide")
        print("{} n'existe pas".format(batiment))
        # exit

    try:
        listeCommande = dicoCommande[chambre]
    except:
        print("Erreur inattendue : position du joueur invalide")
        print("{} n'est pas dans {}".format(chambre, batiment))
        # exit
    
    # Pour déboggage 
    # print(listeCommande)

    return listeCommande

def validiteDeCommande(str command, tuple pos_Joueur):
    command = command.lower()

    listeCommande = commandePossible(pos_Joueur)
    
    if command not in listeCommande :
        # print("Commande invalide, merci de sélectionner une autre")
        return False
    
    return True

def executionCommande(command):


if __name = "__main___":
    # debugging session