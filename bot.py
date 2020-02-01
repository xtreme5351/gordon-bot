import discord
import threading, time
import datetime
from discord.ext import commands
from discord.ext import timers
from discord.utils import get
import random

client = commands.Bot(command_prefix = 'g.')
c = discord.Client()
client.remove_command('help')
version = 0.9

responses= ['OK GAMER', 'How about no?', 'Fuck off', 'K']


def LinSearch(arr, x): 
  
    for i in range(len(arr)): 
  
        if arr[i] == x: 
            return i 
  
    return -1
 
 

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Hehe"))
    print('Online')


@client.command()
async def help(ctx):
    await ctx.send(random.choice(responses))

    embed = discord.Embed(
            colour = discord.Color.red()
        )
    embed.set_author(name='Help')
    embed.add_field(name='Dont spam pls, it might kill pc', value='lmao', inline=False)
    embed.add_field(name='g.ping', value='Ur bad internet lmao', inline=False)
    embed.add_field(name='g.remind', value='To remind gamers at a given time. Format = g.remind [time_in_minutes] [role] [message]  NOTE: ROLES HAVE TO CAPITALISED WITH CORRECT SPELLING', inline=False)
    embed.add_field(name='g.secret', value='Use at own risk', inline=False)

    await ctx.author.send(embed=embed)


@client.command()
async def ping(ctx):
    print(client.latency)
    await ctx.send('Pongolous champ! {} ms'.format(round(client.latency * 1000)))


client.timer_manager = timers.TimerManager(client)

@client.event
async def on_reminder(ctx, channel_id, r, text):
    roleList = [role.mention for role in ctx.guild.roles if role.mentionable]
    actualRole = ["Racists", "CSGO", "Sammy", "candidate", "W.E.E.B", "Eminem", "Wizard101", "Marco", "Luigi", "Giovanni", "Giuseppe", "Yasindu", "Yahya", "Shreyas", "Shamith", "Sammy", "Sam", "Reda", "Eliyas", "Prince", "Pranav", "Nimer", "Matthew", "Manik", "Leroi", "Josh K", "Kavya", "Karolis", "Irfan", "Frazer", "Henry", "Eliot", "Denis", "Clement", "Arya", "Andy", "Ashwin", "Arnav", "Adnan", "Aarnie", "Vegans", "Saiyajin", "Lowest of the Low", "Level 100 Boss", "R6 Bois", "EPIC GAMERS", "Hreh", "Underground Society", "gay", "Bronobo", "Ambassador of Dubai", "French Toast", "Overlord", "Supreme Weeb", "Tony", "Don Cheadle", "Wong-sama", "Noble Scribe", "Indian Tech Support", "xQc Addict", "Pensioners", "Mods"]
    
    result = LinSearch(actualRole, r)
    print(result, len(actualRole))
    if result != -1: 
        print ("Role is present at index % d" % result)
        role_id = roleList[result]
        # role = get(ctx.guild.roles, id=role_id)
        print(role_id)
        await ctx.send("Bruh {} remember to: {}".format(role_id, text))

    else: 
        print ("Role is not present in array") 
        await ctx.send("{} doesnt really exist lmao".format(r))


@client.command()
async def remind(ctx, time, r, *, text):
    tim = int(time) * 60
    author = ctx.author.id
    client.timer_manager.create_timer("reminder", tim, args=(ctx, ctx.channel.id, r, text))
    x = datetime.datetime.now()
    print("Timer set at", x.strftime('%X'))
    print(r)
    print(text)
    t = threading.Timer(tim, on_reminder, args=(ctx, ctx.channel.id, r, text))
    t.start()
    await ctx.send("Ok, timer set by <@{}>".format(author))
   

@client.command()
async def secret(ctx):
    author = ctx.author.id
    print(author)
    for i in range(20):
        await ctx.send('i told you <@{}>'.format(author))


@client.command()
async def testing123(ctx):
    mentions = [role.mention for role in ctx.guild.roles if role.mentionable]
    print(mentions)


client.run(Token)
