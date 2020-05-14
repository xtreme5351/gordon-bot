import discord
import threading, time
import datetime
from discord.ext import commands
from discord.ext import timers
from discord.utils import get
import random

client = commands.Bot(command_prefix = 'g.')
c = discord.Client()
# Removing the default help command so we can create our own
client.remove_command('help')
version = "1.3.3"


# Random responses said when g.help is called
responses= ['OK GAMER', 'How about no?', 'Ok boomer', 'K', 'Bruh', 'xd', 'Lmao ok']


# Linear search for the reminder command
def LinSearch(arr, x): 
    for i in range(len(arr)): 
        if arr[i] == x: 
            return i 
    return -1
 
 
# Console output to acknowledge the bot's status
# Cannot be called
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Hehe"))
    print('Online')


# Just the list of commands, sent to the caller's DM
# Called = g.help
@client.command()
async def help(ctx):
    await ctx.send(random.choice(responses))

    embed = discord.Embed(
            colour = discord.Color.red()
        )
    embed.set_author(name='Help')
    embed.add_field(name='Dont spam pls', value='lmao', inline=False)
    embed.add_field(name='g.ping', value='Ur internet lmao', inline=False)
    embed.add_field(name='g.remind', value='To remind gamers at a given time. Format = g.remind [time_in_minutes] [role] [message]  NOTE: ROLES HAVE TO CAPITALISED WITH CORRECT SPELLING', inline=False)
    embed.add_field(name='g.secret', value='Use at own risk', inline=False)
    embed.add_field(name='g.error', value='Pls report an error. Format = g.error [error msg]', inline=False)

    await ctx.author.send(embed=embed)


# Error feedback from other members in the server, pings the bot admin with the error / bug they found.
# Called = g.error [msg]
@client.command()
async def error(ctx, *, text):
    # The discord ID of the person in charge of this bot
    director = "[ID]"
    await ctx.send("Ok, thanks for the feedback")
    await ctx.send("<@{}>, theres an error - {}".format(director, text))
   

# Checks the ping of the user
# Called = g.ping
@client.command()
async def ping(ctx):
    print(client.latency)
    await ctx.send('Pongolous champ! {} ms'.format(round(client.latency * 1000)))


# Counts the total number of msgs since the particular channel has been created.
# Counts the msgs in the channel the command was called
# Called = g.countpls
@client.command()
async def countpls(ctx, channel: discord.TextChannel=None):
    await ctx.send("Ok, please wait this might take a while")
    author = ctx.author.id
    channel = channel or ctx.channel
    count = 0
    async for _ in channel.history(limit=None):
        count += 1
    print(count, "msgs in the channel")
    await ctx.send("<@{}> There were {} messages in {}".format(author, count, channel.mention))


# timer setup dw
client.timer_manager = timers.TimerManager(client)


# Secondary remind command that uses a linear search (inefficient yes ik but there's not that many roles search through anyway) to find the role and match it to a role ID.
# The role list is a list of role IDs
# actualRole is a list of the names of the roles, in order from bottom up.
# Because each index (in both arrays) has a specific value and ID, the roles have to be in order from bottom up, from the server. Otherwise, it will mismatch the roles
# Will need to be updated everytime a new, callable role is created. 
# Not callable by a user
@client.event
async def on_reminder(ctx, channel_id, r, text):
    roleList = [role.mention for role in ctx.guild.roles if role.mentionable]
    # Fill this with the names of every callable role. Index 0 = the bottom most role
    actualRole = ["r1", "r2", ".etc"]

    result = LinSearch(actualRole, r)
    print(result, len(actualRole))
    # Checks if search was successful
    if result != -1: 
        print ("Role is present at index % d" % result)
        role_id = roleList[result]
        print(role_id)
        await ctx.send("Bruh {} remember to: {}".format(role_id, text))

    else: 
        print ("Role is not present in array") 
        await ctx.send("{} doesnt really exist lmao".format(r))


# Main remind command that creates a thread with a timer on it, the thread is executed once the timer finishes and calles the command above. 
# Also sends a verification to the person who requested the timer
# Note: Its probably good to kill the threads after they're done running (do this if you're running this locally on a computer that is used for other things or on a raspberry pi)
# To kill the thread, add t.sleep(secs) and t.stop() below
# Called = g.remind [time in minutes] [role with correct spelling and caps] [text]
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
    # t.sleep(secs)
    # t.stop()
  
    
# Secret troll command that just pings the caller 20 times
# Called = g.secret
@client.command()
async def secret(ctx):
    author = ctx.author.id
    print(author)
    for i in range(20):
        await ctx.send('i told you <@{}>'.format(author))


# Command to view all the callable / mentionable roles in the server. Warning: This also pings all the roles so be careful!
# Called = g.testRoles
@client.command()
async def testRoles(ctx):
    mentions = [role.mention for role in ctx.guild.roles if role.mentionable]
    print(mentions)


# Easter egg command
# Called = g.selfdistruct
@client.command()
async def selfdistruct(ctx):
    await ctx.send("No u")


client.run('token')
# Insert bot token from Discord Bot Applications
