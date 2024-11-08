import discord
import random
 # type: ignore
# import * - es una forma rápida de importar todos los archivos de la biblioteca
from discord.ext import commands
from bots import gen_pass
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios

bot = commands.Bot(command_prefix='*', intents=intents)

bot.run("toke")

@bot.event
async def on_ready():
    print(f'hemos iniciado con {bot.user}')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def normas(ctx):
    await ctx.send("""
1 - No molestar a nadie
2 - Repestar a los demas 
3 - Tener resperto
  """)
    
@bot.command()
async def borrar(ctx):
    await ctx.channel.purge()
    await ctx.send('Mensajes eliminados', delete_after=3)


@bot.command()
async def xd(ctx, count_heh = 30):
    await ctx.send("xd" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member = None):
    """informacion cuando se unio."""
    if member is None:
        member = ctx.author
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def repeat(ctx, times: int, content='you are the king?'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


#bot_logic.py
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>5585885112456jjajhsfeyyeuqonbmdlpahde"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

