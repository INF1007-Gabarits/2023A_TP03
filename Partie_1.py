from random import normalvariate, randint

def lire_classement(path):
    pass

def lire_match(path):    
    pass

def ecrire_classement(classement, path):
    pass 

def jouer_match(dif_vis, dif_dom):
    pass

def trouver_equipe_division(equipe, classement):
    pass

def trier_classement(classement):
    pass

def mis_a_jour_classement(equipe, stats, division, classement):
    pass

def simuler_rencontres(matchs, classement):
    pass

def equipes_qualifiees(classement):
    pass

if __name__ == '__main__':
    path_classement = './database/classement2019.txt'
    ligue_classement = lire_classement(path_classement)
    
    path_match = './database/matchs2019.txt'
    ligues_rencontres = lire_match(path_match)
    
    simuler_rencontres(ligues_rencontres, ligue_classement)
    
    path_classement_final = "./database/classement_final.txt"
    ecrire_classement(ligue_classement, path_classement_final)

    equipes_series = equipes_qualifiees(ligue_classement)
    print("Équipes qualifiées pour la conférence Est :", equipes_series['Est'])
    print("Équipes qualifiées pour la conférence Ouest :", equipes_series['Ouest'])
