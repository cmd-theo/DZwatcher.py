# Work with Python 3.6
import discord
from urllib.request import urlopen, Request
import re
import math

        


    
TOKEN = 'ODYwOTc4OTA4ODQ1MzEwMDEz.YODHGA.SiNI_4oLrWQykrGvO0Oad0-O40s'

client = discord.Client()

@client.event

async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!rasselband'):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
        reg_url = "https://www.battlemetrics.com/servers/dayz/5374647"
        req = Request(url=reg_url, headers=headers) 
        html = urlopen(req).read() 

        string = str(html)
        a = re.search(r'\b(players)\b', string)
        x = str(html)
        p = str(a)
        u = p[30:34]
        j = p[36:40]
        players = x[int(j)+2:int(j)+4]
        
       
        m = ' il y a ' + str(players) + ' joueurs '
        msg = m.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #Oui
client.run(TOKEN)
