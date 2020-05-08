a1 = { 'rac' : 4,
        'g' :{'rac' : 2,
                'g' : {},
                'd' : { 'rac' : 3, 'g' : {}, 'd' : {}}},
        'd' : {'rac' : 7,
                'g' : {'rac' : 5, 'g' : {}, 'd' : {'rac' : 6, 'g' : {}, 'd' : {}}},
                'd' : {'rac' : 10,
                        'g' : {'rac' : 9, 'g' : {}, 'd' : {}},
                        'd' : {'rac' : 14, 'g' : {}, 'd' : {}}}}}


def est_abr(a):
    if type(a)==dict:
        if a == {}:
            return True
        if list(a.keys())==['rac','g','d']:
            return(est_abr(a['g'])and est_abr(a['d']))
        else:
            return False
    else:
      return False

def build_abr (r,g,d):
    return {'rac' : r,
            'g' : g,
            'd' : d}

def est_vide(a):
    if a=={}:
        return True
    else:
        return False 

def racine(a):
    return a['rac']

def gauche(a):
    return a['g']

def droit(a):
    return a['d']

def hauteur(a):
    if est_vide(a):
        return 0
    else:
        return 1 + max(hauteur(gauche(a),droit(a)))

def est_feuille(a):
    if est_vide(a):
        return False
    else:
        return est_vide(gauche(a))and est_vide(droit(a))

 
def nb_noeuds_internes(a):
    if est_vide(a): 
        return 0
    elif est_feuille(a):
        return 0
    else:
        return 1 + nb_noeuds_internes(gauche(a)) + nb_noeuds_internes(droit(a))

def infixe (a):
    if est_vide(a):
        return []
    elif est_feuille(a):
        return [racine(a)]
    else:
        return infixe(gauche(a)) + [racine(a)] + infixe(droit(a))

def prefixe (a):
    if est_vide(a):
        return []
    elif est_feuille(a1):
        return [racine(a)]
    else:
        return [racine(a)]+ prefixe(gauche(a)) + prefixe(droit(a))

def suffixe(a):
    if est_vide(a):
        return []
    elif est_feuille(a):
        return [racine(a)]
    else:
        return suffixe(gauche(a)) + suffixe(droit(a)) + [racine(a)]
