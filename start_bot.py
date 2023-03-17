import sys
import discord
from larousse.api import get_conjugaison, get_definition, get_translation


TOKEN='OTI5MTE2NjE5MDE0Mjk5NzI5.YdipSA.yxGXJf0TFHlDjaDBene9E1IB8aM'
client = discord.Client()

@client.event
async def on_ready():
    print(f'Connecté en tant que {client.user}')

@client.event 
async def on_message(message):
    if message.author == client.user:
        return 
    
    if message.content.lower().startswith('!salut'):
        auteur = str(message.author)
        await message.channel.send(f"Salut {auteur.split('#')[0]}, comment ça va ?")

    if message.content.lower().startswith('!menu'):
        await message.channel.send("""Menu du frenchbot !
        =======================
        !trad 'mot': Traduction du français vers l'allemand
        !ubersetze 'mot': Traduction de l'allemand vers le français
        !def 'mot' : Définition du mot
        !conj 'verbe' : Conjugaison du verbe
        =======================
                                    """)

    if message.content.lower().startswith('!def'):
        liste_of_words = message.content.split()
        if len(liste_of_words) == 2:
            mot = liste_of_words[1]
            definition = get_definition(mot)
            await message.channel.send(f"Définition de {mot}:\n{definition}")
        else:
            await message.channel.send("Erreur !\nIl faut taper '!def mot_à_définir'.")

    if message.content.lower().startswith('!trad'):
        liste_of_words = message.content.split()
        if len(liste_of_words) == 2:
            mot = liste_of_words[1]
            translation = get_translation(mot, "FR")
            await message.channel.send(f"{mot} se dit '{translation}' en allemand !")
        else:
            await message.channel.send("Erreur !\nIl faut taper '!trad mot_à_traduire'.")
    
    if message.content.lower().startswith('!ubersetze'):
        liste_of_words = message.content.split()
        if len(liste_of_words) == 2:
            mot = liste_of_words[1]
            translation = get_translation(mot, "DE")
            await message.channel.send(f"'{mot}' se dit {translation} en français !")
        else:
            await message.channel.send("Error !\nSchreibe '!ubersetze zu_ubersetzendes_Wort'.")
    
    if message.content.lower().startswith('!conj'):
        liste_of_words = message.content.split()
        if len(liste_of_words) == 2:
            verbe = liste_of_words[1]
            conjugaison = get_conjugaison(verbe)
            await message.channel.send(f"Tu peux trouver toutes les conjugaisons du verbe {verbe} à cette adresse : {conjugaison}")
        else:
            await message.channel.send("Erreur !\nIl faut taper '!conj verbe_à_conjuguer'.")

    if message.content == "$STOP":
        sys.exit()

client.run(TOKEN)