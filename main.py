import discord
from discord.ext import commands
import os
import time
import pprint
from keep_alive import keep_alive
from binary import convert_binary
from dictionary import meaning
from flip_coin import flip_coin
import random_wiki
from replit import db
from image_search import find_image
from plot_function import draw_graph

COMMANDS = """
.help: displays all commands
.hello: displays a greeting
.binary: convert text to binary
.flipcoin: flips a coin
.define: defines words
.clear: clears chat
.users: shows all users
.randwiki: displays a random wikipedia article
.img: displays an image of the search keywords
.calc: displays the result of a math expression
.graph: graphs a given function
"""
#__________________

players = {}
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(intents=intents, command_prefix='.', help_command=None)

# shows when bot is logged in
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# displays a greeting
@client.command()
async def hello(ctx): # name the function the name of the command
  await ctx.send("Hello")

@client.command()
async def help(ctx):
  embed = discord.Embed(title="Help menu", description=COMMANDS, color=0x008000)
  await ctx.send(embed=embed)

# converts text to binary
@client.command()
async def binary(ctx, *, msg):
  await ctx.send(convert_binary(msg))

# finds defenition of a word
@client.command()
async def define(ctx, *, msg):
  await ctx.send(meaning(msg))

@client.command()
async def flipcoin(ctx):
  author = str(ctx.message.author)
  coin = flip_coin()
  if coin == 1:
    side = "Heads"
    amount = 500
    description = f"{author} has won $500"
  elif coin == 0:
    side = "Tails"
    amount = -500
    description = f"{author} has lost $500"
  
  embed = discord.Embed(title=side, description=description, color=0x0000FF)
  if author in db.keys():
    db[author] += amount
  else:
    db[author] = amount
  await ctx.send(embed=embed)

@client.command()
async def stats(ctx):
  data = ''
  for key in db.keys():
    data += key + ": " + str(db[key]) + "\n"
  embed = discord.Embed(title="Stats", description = data, color=0x0000FF)
  await ctx.send(embed=embed)

# displays all user names
@client.command()
async def users(ctx):
    people = ''
    for guild in client.guilds:
        for member in guild.members:
            people += str(member) + '\n'
    await ctx.send(people)

# clears the chat, must be admin
@client.command()
async def clear(ctx, amount=1):
  role = discord.utils.get(ctx.guild.roles, name="Admin")
  if role in ctx.author.roles:
    await ctx.channel.purge(limit=amount)
  else:
    embed = discord.Embed(title="Need Permission", description="Only admins can clear the chat", color=0xFF0000)
    await ctx.channel.send(embed=embed)

@client.command()
async def randwiki(ctx):
  topic = random_wiki.random_wiki_topic()
  url = random_wiki.random_wiki_url(topic)
  image = random_wiki.get_wiki_image(topic)

  embed = discord.Embed(title="Random Article", description=url)
  embed.set_thumbnail(url=image)
  await ctx.send(embed=embed)

@client.command()
async def calc(ctx, *, expression):
  result = eval(expression, {"__builtins__": {}}, {})
  await ctx.send(result)

@client.command(aliases=['img', 'images'])
async def image(ctx, *, topic):
  url = find_image(topic=topic)
  embed = discord.Embed(title=topic)
  embed.set_image(url=url)
  await ctx.send(embed=embed)

@client.command(aliases=['plot'])
async def graph(ctx, *, function):
  FILE_NAME = 'graph.png'
  draw_graph(function, FILE_NAME)
  embed = discord.Embed(title="ƒ(x) = " + function, color=0x7F00FF)
  file = discord.File(FILE_NAME, filename=FILE_NAME)
  embed.set_image(url="attachment://"+FILE_NAME)
  await ctx.send(file=file, embed=embed)


mySecretToken = os.getenv("TOKEN")  # gets the token key from the secrets tab
keep_alive()  # pings the server continuously

client.run(mySecretToken)
