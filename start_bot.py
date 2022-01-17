import discord
import requests
import json
import random

TOKEN=''
client = discord.Client()

sad_words = ["triste", "déprimé", "malheureux", "angry", "miserable", "attristé"]

cheer_up = ["t'es qu'une merde", "tant pis", "ainsi va la vie",
"jsuis qu'un bot trouve toi des amis"]
def get_quote():
    reponse = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(reponse.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print('Connecté en tant que {0.user}'.format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('Bonjour'):
        await message.channel.send('Wesh ma caille')
    if message.content.startswith('Tranquille'):
        await message.channel.send('Trql et toi ma gueule ?')
    if message.content.startswith('mdr'):
        await message.channel.send('HAHA ON SE TAPE DES BARRES. Losers')
    if message.content.startswith('désolé'):
        await message.channel.send('Pas de problème Lulu')
    if message.content.startswith('$inspiration'):
        try: 
            quote = get_quote()
            await message.channel.send(quote)
        except Exception as e:
            await message.channel.send(f"Désolé pas d'inspi, à cause de {e}")
    if message.content.startswith('présent'):
        await message.channel.send("On est al t'as vu")
    if any(mot in message.content for mot in sad_words ):
        await message.channel.send(random.choice(cheer_up))
    

client.run(TOKEN)