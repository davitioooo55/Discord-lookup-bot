import discord
from discord import *
from datetime import datetime
from time import sleep
import requests
import json
from datetime import datetime
from extensions import on_start_screen

from discord.ext import commands
client = discord.Client(intents=discord.Intents.default())
bot = commands.Bot(command_prefix="/",intents=discord.Intents.default())

def time_now():
    time = datetime.now()
    current_time = time.strftime("%y-%m-%d %H:%M:%S")
    now = current_time + " >"
    return now


TOKEN = "your Discord token here"


@bot.event
async def on_ready():
    print(f"{time_now()} Logged in as {bot.user}")
 
 
@bot.slash_command(name="commands",description="Sends list of commands" ) 
async def command(interaction: discord.Interaction,  ):
    await interaction.response.send_message(f"""\nAvailable Commands are
[+]  /Spam (Spams to the desired user)
[+]  /lookup (Uses ID to look up person's Username,Badges,Flags and avatar picture)
[+]  /lookupip (uses IP to send The location of the Desired Person)


""")

      
   
@bot.slash_command(name="spam",description="spams Messages to the Desired User" ) 
async def Spam(interaction: discord.Interaction, person_id,messagetospam,messagesquantity,speed ):
    await interaction.response.send_message("Sending messages...")
    user = await bot.fetch_user(person_id)
    i=0
    while i<int(messagesquantity): 
        
      
        
        i= i+1 
        await user.send("<@" + str(person_id) + ">"+ messagetospam)
        print(f"{time_now()} Spammed {person_id} with {messagetospam}")
        sleep(float(speed))      
    
   
@bot.slash_command(name="lookup",description="looks up desired user" ) 
async def lookup(interaction: discord.Interaction, user_id ):
    a=requests.get(f"https://discordlookup.mesavirep.xyz/v1/{user_id}", headers={"Authorization": "your Discord token here"})
    r=requests.get(f"https://discord.com/api/v9/users/{user_id}", headers={"Authorization": "Bot your Discord token here"})
    r=r.json()
    a=a.json()
    badges = a['badges']
    username = r['username'  ] + "#"+ r['discriminator']
    avatar = ["https://cdn.discordapp.com/avatars/" + user_id + "/" +r['avatar'] + ".png"]
    public_flags =  r['public_flags']
    await interaction.response.send_message(f"""\n[+] Username: {username}
[+] Avatar: {avatar}
[+] public_flags: {public_flags}
[+] badges: {badges}


""")
@bot.slash_command(name="lookupip",description="looks up ip" ) 
async def lookupip(interaction: discord.Interaction, user_ip ):
     
    r=requests.get(f"https://ipinfo.io/{user_ip}?token=ip info api token here", headers={"Authorization": "your Discord token here"})
    r=r.json()
    ip = r['ip'] 
    city = r['city']
    country = r['country']
    location = r['loc']
    organisation = r['org'] 
    timezone= r['timezone']
    await interaction.response.send_message(f"""\n[+] ip: {ip}
[+] city: {city}
[+] country: {country}
[+] country: {location}
[+] country: {organisation}
[+] country: {timezone}

""")

bot.run(TOKEN)