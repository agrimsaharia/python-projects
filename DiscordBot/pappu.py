import asyncio
import discord
from dotenv import load_dotenv
import os
import time
import api
import random

intro_message = 'Discordwasiyo! Mai pappu hu\nseedhi baat kahu to mai bakwaas karne ke liye bana hu\nkuch commands se mai trigger hota hu\n\nMere se Hello sunke khudko meri tarah V.I.P samajhna chahte ho... \nto pehle mujhe "hello pappu" bolna padega\n\nMai dad jokes maar leta hu... roj mummy se seekhta hu\nJoke sunna hai to bolo --> "pappu joke suna"\n(waise mujhe pasand nahi agar tum mere jokes pe feedback na do to)\n\nKoi aapko attention dena pasand karta hai ya nahi(basically kaun kaun online hai) \njaanne ke liye dabaayein --> "koi hai?"\n...\n...\n...\n...\n...\nAccha accha theek hai...\nWaise to mai bahut charming hu, but mujhe kabhi alvida kehna ho to "bye pappu" kardena\nwaise bhi mujhe bhi to aaraam chahiye hota hai!'

vatsalya = ['vatsy', 'vatsalya', 'batsy']
vatsalya_insults = ['why do you have to mention a kidnapper in this \'safe for kids\' chat', 'vatsy...\tuhh!... \nhis name makes me puke everytime']
feedback = ['chutiya --> 1', 'badiya --> 2']

goodbyes_italian = ['Arrivederci!', 'Ciao! Ciao!', 'Accha chalta hu... voting me yaad rakhna']

load_dotenv()

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    msg = message.content.lower()
    channel = message.channel

    if msg == 'pappu?':
        await channel.send(intro_message)

    # greet our bot
    elif msg.startswith('hello pappu'):
        await channel.send('Hello! ' + message.author.name)

    elif msg.startswith('koi hai?'):
        time.sleep(3)
        online_members = []
        for member in channel.members:
            if member.status == discord.Status.online and (not member.bot) and member != message.author:
                online_members.append(member.display_name)
        
        if len(online_members) == 0:
            await channel.send('sannata chha gaya hai...\npar mai hu na!')
        else:
            await channel.send(', '.join(online_members) + "\tye sab hai...\naur mai to hamesha hu hi is desh ki janta ke liye")

    # get dad_joke from api file and reply based on the feedback given
    elif msg.startswith('pappu joke suna'):
        joke_body = api.get_dad_joke()
        await channel.send(joke_body['setup'])
        time.sleep(3)
        await channel.send(joke_body['punchline'])
        time.sleep(2)
        await channel.send("Joke kaisa laga!?\n" + '\n'.join(feedback))
        
        def check(m):
            return m.author != client.user and m.channel == channel
        try:
            reply = await client.wait_for('message', timeout=10.0, check=check)
            if reply.content == '1':
                await channel.send("because you deserve stupid jokes my friend.\n{.author.name} Gaand mara!".format(reply))
            elif reply.content == '2':
                await channel.send("mummy ko batata hu khush ho jayengi!")
            else:
                await channel.send("itni jaldi kya hai\nek reply hi to maang raha tha, baad me chat karlete :unamused: ")
        except asyncio.TimeoutError:
            await channel.send("nikal liye kya?? kuch pucha tha maine!! :unamused:\nsaala koi seriously hi nahi leta mujhe!") 

    # insult vatsalya
    elif any(word in msg for word in vatsalya):
        insult = random.choice(vatsalya_insults)
        await channel.send(insult)

    # get rid of the bot
    elif msg.startswith('bye pappu'):
        await channel.send(random.choice(goodbyes_italian))
        await client.close()


client.run(os.getenv('TOKEN'))