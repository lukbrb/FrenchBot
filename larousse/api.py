from .frenchscrapper import Larousse


def get_translation(word, langage):
    page = Larousse()
    result = page.get_element(mot=word, methode="trad", langage=langage)
    if result:
        traduction = [item.text for item in result]
        return "\n".join(traduction)
    return f"Pas de traduction trouvée pour {word}."


def get_definition(word):
    page = Larousse()
    result = page.get_element(mot=word, methode="def")
    if result:
        definitions = [item.text for item in result]
        return "\n".join(definitions)
    return f"Pas de définition trouvée pour {word}."


def get_conjugaison(verbe, temps="présent"):
    # page = Larousse()
    # result = page.get_element(mot=verbe, methode="conj")
    # return result
    return f"https://www.larousse.fr/conjugaison/francais/{verbe}"