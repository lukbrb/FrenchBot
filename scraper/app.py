import argparse
from .api import get_translation, get_definition, get_conjugaison


def get_commands():
    parser = argparse.ArgumentParser(description="Programme fournissant traductions (FR->DE, DE->FR), définitions et conjugaisons.")
    parser.add_argument(
    "mot",
    type=str,
    help="Mot/verbe à traduire, définir ou conjuguer."
    )

    parser.add_argument(
    "-t", "--traduction", 
    type=str, 
    choices=["FR", "DE"], 
    help="Traduction d'un mot du français vers l'allemand, ou vice-versa."
    )

    parser.add_argument(
    "-d", "--definition", 
    action="store_true",  
    help="Donne la définition du mot passé en argument."
    )

    parser.add_argument(
    "-c", "--conjugaison", 
    type=str,  
    nargs="?", 
    help="Cherche la conjugaison d'un verbe. Le temps peut être spécifié en argument."
    )

    parsed_args = parser.parse_args()

    return parsed_args


def main():
    """ 
        Command-line interface for the FrenchBot. 

        Loads the command name and parameters from :py:data: `argv`.
    """
    commande = get_commands()

    if commande.traduction:
        # commands.traduction est soit FR soit DE
        traduction = get_translation(commande.mot, commande.traduction)
        print(f"Traduction de {commande.mot}:", traduction)
    
    if commande.definition:
        definition = get_definition(commande.mot)
        print(f"Définitions de {commande.mot}:\n{definition}")
    
    if commande.conjugaison:
        conjugaisons = get_conjugaison(commande.mot)
        print(f"Conjugaisons de {commande.mot}:\n{conjugaisons}")


if __name__ == "__main__":
    main()
    