import discord
import requests
from discord.ext import commands

intents = discord.Intents.default()

from botduck import get_duck_image_url

intents.message_content = True

bot = commands.Bot(command_prefix='*', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado como  {bot.user}')


@bot.command()
async def hi(ctx):
    await ctx.send("""
    hola Bienvenido a este bot creado por creasto. """)

@bot.command()
async def normas(ctx):
    await ctx.send("""
1 - Respetar al admi de discord.
2 - No acoses a ningun miembro de la comunidad.
3 - No hacer spam o seras expusado.
4 - Evita las conversaciones políticas o religiosas.
5 - No está permitido el contenido NSFW o +18.
6 - Se prohíbe tener comportamientos molestos o hacer ruidos.
Si quieres unas dudas sobre este bot escribe *dudas.
  """)


@bot.command()
async def dudas(ctx):
    await ctx.send("""
- Esta servidor es para conocer personas.
- jugar , cod , fortnite, minecraft, ect.
- y pasar el rato con unos amigos
  """)


@bot.command()
async def entro(ctx, member: discord.Member = None):
    """informacion cuando se unio."""
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    if member is None:
        member = ctx.author
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send('Mensajes eliminados', delete_after=3)

@bot.command()
async def poke(ctx, arg):
    try:
        pokemon = arg.split(" ",1)[0]
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not found":
            await ctx.send("pokemon no se encontro")
        else:
            image_url = result.json()['sprites']['front_default']
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error:  ", e)

@poke.error
async def error_type(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument ):
        await ctx.send("tienes que pasarme un pokemon")

#prt2

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']



