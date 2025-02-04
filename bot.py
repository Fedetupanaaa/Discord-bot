import discord
import os
from bot_logic import gen_pass
from bot_logic import gen_emoji
from bot_logic import coin_flip
import random
from discord.ext import commands
import time
import requests



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_image():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


def get_fox_image_image():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

@bot.event
async def on_ready():
    print(f'entramos como: {bot.user}')

@bot.command()
async def gen(ctx):
    await ctx.send(f"Tu contraseña generada es: {gen_pass(10)}")

@bot.command()
async def joined(ctx, member: discord.Member):
    
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def emoji(ctx):
    await ctx.send(f" {gen_emoji()}")

@bot.command()
async def numero(ctx):
    numero_aleatorio = random.randint(1, 10)
    await ctx.send(f'El número aleatorio es: {numero_aleatorio}')
    

@bot.command()
async def coinflip(ctx):
    await ctx.send(f"la moneda dice: {coin_flip()}")    


@bot.command()
async def mem(ctx):
    memes= os.listdir("images")
    azar= random.choice(memes)
    with open (f'images/{azar}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command('duck')
async def duck(ctx):
  
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('dog')
async def god(ctx):
    
    image_url = get_dog_image_image()
    await ctx.send(image_url)


@bot.command('fox')
async def god(ctx):
    
    image_url = get_fox_image_image()
    await ctx.send(image_url)





bot.run("TOKEN")
