import discord
from discord.ext import commands
TOKEN = 'NTcwMDIyMjg0NDY3ODk2MzQx.XL5U2Q.XRBDEPW-eTdSQz3y5Hu4EN5aLF8'
bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("Online")

@bot.command()
async def webhooks(ctx):
    await ctx.send('Webhooks are fun!')


    bot.run(TOKEN)