import requests
from bs4 import BeautifulSoup


def get_html(url):
    """ Fonction qui envoie une requếte à l'url entrée en argument.
        Renvoie un objet BeautifulSoup (du contenu HTML retravaillé en gros) si la requête a été fructueuse.
        Renvoie None et affiche un message d'erreur dans le cas contraire.
    """
    # On vérifie d'abord que l'url est valide

    r = requests.get(url)  

    if r.ok:  # équivalent à r.status_code == 200
        return BeautifulSoup(r.content, "lxml")
    else:
        print(f"Erreur d'accès, code: {r.status_code}")
        return None


def get_translation(word, fr=True):
    """ Function that will take a French word as an argument
    and return the translation in German.
    """

    # TODO: Have a function to do the translation in the other way.
    if fr == True:
        base_url = "https://www.larousse.fr/dictionnaires/francais-allemand/"
        tag = "a"
        classe = "lienarticle2"
    else:
        base_url = "https://www.larousse.fr/dictionnaires/allemand-francais/"
        tag = "span"
        classe = "Traduction"
        
    research = base_url + word 
    print("Traduction de", word, "...")
    html = get_html(research)
    trad_word = html.find(tag, {"class": classe})
    if trad_word != None:
        return trad_word.text
    
    else:
        return "Traduction non trouvée"


def get_definition(word):
    """ Function that will take a French word 
        and returns its defintion.
    """
    base_url = "https://www.larousse.fr/dictionnaires/francais/"
    research = base_url + word 
    print("Définition de", word)
    return  get_html(research)

def get_conjugaison(verb):
    """ Function that will take the infinitive of 
        a verb and return all the 'conjugaison'    
    """
    base_url = "https://www.larousse.fr/conjugaison/francais/"
    research = base_url + verb
    print("Conjugaison de", verb)
    return  get_html(research)