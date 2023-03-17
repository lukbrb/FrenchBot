import requests
from bs4 import BeautifulSoup


class Larousse:
    def __init__(self) -> None:
        self.requests_types = {
            'trad': 
            {   
                "FR":
                {
                    "class": "lienarticle2",
                    "tag": "a",
                    "URL": "https://www.larousse.fr/dictionnaires/francais-allemand/",
                    "fullname": "traduction"
                },
                "DE":
                {
                    "class": "Traduction",
                    "tag": "span",
                    "URL": "https://www.larousse.fr/dictionnaires/allemand-francais/",
                    "fullname": "traduction"
                }
            },

            'def':
            {
                "class": "Definitions",
                "tag": "ul",
                "URL": "https://www.larousse.fr/dictionnaires/francais/",
                "fullname": "définition"
            },

            'conj': 
            {
                "URL": "https://www.larousse.fr/conjugaison/francais/",
                "fullname": "conjugaisons"
            }
        }


    def get_html(self, url):
        """ Fonction qui envoie une requếte à l'url entrée en argument.
            Renvoie un objet BeautifulSoup si la requête a été fructueuse.
            Renvoie None et affiche un message d'erreur dans le cas contraire.
        """
        r = requests.get(url)  

        if r.ok:  # équivalent à r.status_code == 200
            return BeautifulSoup(r.content, "lxml")
        else:
            return None

    def get_element(self, methode: str, mot: str, langage="FR"):
        methode = methode.lower()
        assert methode in self.requests_types.keys(), f"{methode} is not a valid method. Accepted methods are 'trad', 'def' and 'conj'"

        # We first get the correct URL based on the method
        if methode == 'trad':
            methode_dico = self.requests_types[methode][langage]
        else:
            methode_dico = self.requests_types[methode]

        base_url = methode_dico.get("URL")

        url = base_url + mot   # we construct the URL for research

        try:
            html = self.get_html(url)
            result = html.find_all(methode_dico.get('tag'), {"class": methode_dico.get('class')})
            return result

        except Exception as e:
            return f"Pas de {methode_dico.get('fullname')} trouvée(s) en raison de:\n{e}"
