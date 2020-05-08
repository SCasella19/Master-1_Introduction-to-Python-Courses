from math import sqrt


# 1
Critiques={'Lisa':{'Lady':2.5,'Snakes':3.5,'Luck':3.0,'Superman':3.5,'Dupree':2.5,'Night':3.0},
           'Gene':{'Lady':3.0,'Snakes':3.5,'Luck':1.5,'Superman':5.0,'Dupree':3.5,'Night':3.0},
           'Michael':{'Lady':2.5,'Snakes':3.0,'Superman':3.5,'Night':4.0},
           'Claudia':{'Snakes':3.5,'Luck':3.0,'Superman':4.0,'Dupree':2.5,'Night':4.5},
           'Mick':{'Lady':3.0,'Snakes':4.0,'Luck':2.0,'Superman':3.0,'Dupree':2.0,'Night':3.0},
           'Jack':{'Lady':3.0,'Snakes':4.0,'Superman':5.0,'Dupree':3.5,'Night':3.0},
           'Toby':{'Snakes':4.5,'Superman':4.0,'Dupree':1.0},
           'Anne':{'Lady':1.5,'Luck':4.0,'Dupree':2.0}}


# 2
def sim_manhattan(person1, person2):

    distance = 0
    cleperson1 = person1.keys()
    cleperson2 = person2.keys()

    for cledico in cleperson1:
        if cledico in cleperson2:
            # abs is used to return the absolute value of a number.
            distance = distance+abs(person1[cledico]-person2[cledico])
    return distance


def sim_ouclidienne(person1, person2):

    distance = 0
    cleperson1 = person1.keys()
    cleperson2 = person2.keys()

    for cledico in cleperson1:
        if cledico in cleperson2:
            distance = distance + (sqrt(abs(person1[cledico]-person2[cledico]))**2)

    return sqrt(distance)


# 3
def computeNearestNeighbor(nouveauCritique, Critiques):

    distances = []

    for critique in Critiques:
        if critique != nouveauCritique:
            distance = sim_manhattan(Critiques[critique], Critiques[nouveauCritique])
            distances.append((distance, critique))
    distances.sort()
    return distances


def recommendProche(nouveauCritique, Critiques):

    List = computeNearestNeighbor(nouveauCritique, Critiques)
    Personneproche = (List[0])[1]
    film = []

    for cledico in Critiques[Personneproche]:
        if cledico not in Critiques[nouveauCritique]:
            film.append(((Critiques[Personneproche])[cledico], cledico))
    return film


# Question 4
def C(a, Critiques):
    """
    Retourne le liste des critiques qui ont vu le film <a>
    """
    ca = [critique for critique, films in Critiques.items() if a in films]
    return ca


def sPrime(a, Critiques, critique):
    """
    Calcule s'(a) en une seule fonction
    """
    total, s, ca = 0, 0, C(a, Critiques)

    for c in ca:
        term = 1/(1+sim_manhattan(Critiques[c], Critiques[critique]))
        s += term
        total += term * Critiques[c][a]

    return total/s
## sample to use sPrime('Night', Critiques, 'Anne')

def Bestrecommend(movies, Critiques, critique):
    """
    Recommande le film avec le plus score parmi les éléments de <movies>
    """
    # compute the scores
    scores = [(a, sPrime(a, Critiques, critique)) for a in movies]

    # sort the list by score
    scores.sort(key=lambda x: -x[1])
    bestMovie = scores[0][0]

    return bestMovie
## sample to use Bestrecommend(['Luck','Superman'], Critiques, 'Anne')

# Question 5
def rankUnwatched(table):
    """
    """

    # ensemble de tout les films
    movies = set()
    for values in table.values():
        movies = movies.union(set(values.keys()))

    recommandations = {}

    for critique, watched in table.items():
        unwatched = set(movies) - set(watched)

        sPrimeRecommand = [(a, sPrime(a, table, critique)) for a in unwatched]
        proche = recommendProche(critique, table)

        # sorting
        sPrimeRecommand.sort(key=lambda x: -x[1])
        proche.sort(key=lambda x: -x[0])

        # ne garde que les noms des film
        sPrimeRecommand = [a for a, s in sPrimeRecommand]
        proche = [a for s, a in proche]

        recommandations[critique] = {0: sPrimeRecommand,
                                     1: proche}

    return recommandations


# exemple d'execution
if __name__ == '__main__':

    # question 4, exemple d'utilisation
    best = Bestrecommend(['Snakes', 'Superman', 'Night'], Critiques, 'Anne')
    print('Best Recommantation pour Anne:', best)

    table = {'Angelica': {'Blues Traveler': 3.5, 'Broken Bells': 2, 'Norah Jones': 4.5, 'Phoenix': 5, 'Slightly Stoopid': 1.5, 'The Strokes': 2.5, 'Vampire Weekend': 2},
             'Bill': {'Blues Traveler': 2, 'Broken Bells': 3.5, 'Deadmau5': 4, 'Phoenix': 2, 'Slightly Stoopid': 1, 'Vampire Weekend': 3},
             'Chan': {'Blues Traveler': 5, 'Broken Bells': 1, 'Deadmau5': 1, 'Norah Jones': 3, 'Phoenix': 5, 'Slightly Stoopid': 1},
             'Dan': {'Blues Traveler': 3, 'Broken Bells': 4, 'Deadmau5': 4.5, 'Phoenix': 3, 'Slightly Stoopid': 4.5, 'The Strokes': 4, 'Vampire Weekend': 2},
             'Hailey': {'Broken Bells': 4, 'Deadmau5':1, 'Norah Jones': 4, 'The Strokes': 4, 'Vampire Weekend': 1},
             'Jordyn': {'Broken Bells': 4.5, 'Deadmau5':4, 'Norah Jones': 5, 'Phoenix': 5, 'Slightly Stoopid': 4.5, 'The Strokes': 4, 'Vampire Weekend': 4},
             'Sam': {'Blues Traveler': 5, 'Broken Bells': 2, 'Norah Jones': 3, 'Phoenix': 5, 'Slightly Stoopid': 4, 'The Strokes': 5},
             'Veronica': {'Blues Traveler': 3, 'Norah Jones': 5, 'Phoenix': 4, 'Slightly Stoopid': 2.5, 'The Strokes': 3}}

    # question 5, exemple d'utilisation
    resultat = rankUnwatched(table)

    for critique, value in resultat.items():
        print(f'\nRecommandation pour {critique} selon:')
        print(f"  - best recommend (mannhatan): {', '.join(value[0])}")
        print(f"  - recommend proche (euclidienne): {', '.join(value[1])}")
