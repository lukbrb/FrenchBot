from sys import argv
from .frenchscrapper import get_translation, get_definition, get_conjugaison


commands = {
    "--trad": get_translation,
    "--conj": get_conjugaison,
    "--def" : get_definition
}


# TODO: améliorer l'app avec le module pour CLI

def main():
    """ 
        Command-line interface for the FrenchBot. 

        Loads the command name and parameters from :py:data: `argv`.
    """
    
    if len(argv) == 3:
        command_name = argv[1]
        mot = argv[2]

        if command_name in commands.keys():
            return commands[command_name](mot)
        else:
            print("Invalid command")

    else:
        print("Enter one of the command:")
        print("--trad")
        print("--conj")
        print("--def")
        print("and the word to work with")



if __name__ == "__main__":
    main()