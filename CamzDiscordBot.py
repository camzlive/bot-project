import discord
from discord.ext import commands
TOKEN = 'NTcwMDIyMjg0NDY3ODk2MzQx.XL5U2Q.XRBDEPW-eTdSQz3y5Hu4EN5aLF8'
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def whymydolphinstopworkinglmao(ctx):
    await ctx.send('HAHAHHAHAHAHAHAHAH')

@bot.command()
async def clear(ctx, amount=100):
	await ctx.channel.purge(limit=amount)
    

bot.run(TOKEN)