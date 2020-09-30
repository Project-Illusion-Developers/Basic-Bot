# Recommend to be used on Arch Linux Kernel 5.8.5

#     Coded by Reedeht#0001 in under 1 hour, if you have any issues do not report it to github.

# GITHUB LinK: https://github.com/Reedeht/Basic-Bot
# GITHUB License General Public License

####################CONTROL PANEL####################

token = 'ENTER TOKEN HERE' #Get a token here: https://discord.com/developers/applications
prefix = 'b' #Change prefix here

####################CONTROL PANEL####################

#                Arch ASCII Art
#                    -`
#                   .o+`
#                  `ooo/
#                 `+oooo:
#                `+oooooo:
#                -+oooooo+:
#              `/:-:++oooo+:
#             `/++++/+++++++:
#            `/++++++++++++++:
#           `/+++ooooooooooooo/`
#          ./ooosssso++osssssso+`
#         .oossssso-````/ossssss+`
#        -osssssso.      :ssssssso.
#       :osssssss/        osssso+++.
#      /ossssssss/        +ssssooo/-
#    `/ossssso+/:-        -:/+osssso+-
#   `+sso+:-`                 `.-/+oso:
#  `++:.                           `-/+/
#               Arch ASCII Art

import discord #discord.py
from discord.ext import commands #commands
import sqlite3 #sqlite3

client = commands.Bot(command_prefix=prefix)
client.remove_command('help')

@client.command()
async def help(ctx):
    global prefix
    embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
    embed.add_field(name=f"{prefix}start", value="Starts your game", inlne=False)
    embed.add_field(name=f"{prefix}buy", value="Allows purchasing", inlne=False)
    embed.add_field(name=f"{prefix}name", value="Renames your nation", inlne=False)
    embed.add_field(name=f"{prefix}update", value="Gets your funds", inlne=False)
    embed.add_field(name=f"{prefix}stats", value="Displays your stats", inlne=False)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    global prefix
    print("online")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"{prefix}help | 1 hour challenge ⏱"))

@client.command()
async def start(ctx):
    data = sqlite3.connect('db.sqlite')
    cur = data.cursor()
    cur.execute(f"SELECT id FROM main WHERE id = {ctx.message.author.id}")
    result = cur.fetchone()
    if result is None:
        msg = ctx.message.content
        prefix_used = ctx.prefix
        alias_used = ctx.invoked_with
        text = msg[len(prefix_used) + len(alias_used):]
        cur.execute(f"INSERT INTO main(id) VALUES ({ctx.message.author.id})")
        query = """Update main set name = ? where id = ?"""
        entry = (text, ctx.message.author.id)
        cur.execute(query, entry)
        await ctx.send('Welcome to Baisc Bot\nYour Basic Bot has been created')
    if result is not None:
        await ctx.send('You already have a Basic in Basic Bot')
    data.commit()
    cur.close()
    data.close()

@client.command()
async def name(ctx):
    data = sqlite3.connect('db.sqlite')
    cur = data.cursor()
    msg = ctx.message.content
    prefix_used = ctx.prefix
    alias_used = ctx.invoked_with
    text = msg[len(prefix_used) + len(alias_used):]
    cur.execute(f"SELECT id FROM main WHERE id = {ctx.message.author.id}")
    result = cur.fetchone()
    if result is not None:
        query = """Update main set name = ? where id = ?"""
        entry = (text, ctx.message.author.id)
        cur.execute(query, entry)
        await ctx.send(f"Updated your name to {text}")
    if result is None:
        await ctx.send("Lol you don't exist ")
    data.commit()
    cur.close()
    data.close()

@client.command()
async def update(ctx):
    data = sqlite3.connect('db.sqlite')
    cur = data.cursor()
    cur.execute(f"SELECT id FROM main WHERE id = {ctx.message.author.id}")
    result = cur.fetchone()
    if result is not None:
        cur.execute(f"SELECT money FROM main WHERE id = {ctx.message.author.id}")
        bux = cur.fetchone()
        bux = str(bux)
        bux = bux[2:-3]
        cur.execute(f"SELECT income FROM main WHERE id = {ctx.message.author.id}")
        mone = cur.fetchone()
        mone = str(mone)
        mone = mone[2:-3]
        damndaniel = bux + mone
        query = """Update main set name = ? where id = ?"""
        entry = (damndaniel, ctx.message.author.id)
        cur.execute(query, entry)
        await ctx.send(f"You have gained ${damndaniel}.00!")
    if result is None:
        await ctx.send("Lol you don't exist ")
    data.commit()
    cur.close()
    data.close()

@client.command(aliases=['buy-factory'])
async def factory(ctx):
    data = sqlite3.connect('db.sqlite')
    cur = data.cursor()
    cur.execute(f"SELECT id FROM main WHERE id = {ctx.message.author.id}")
    result = cur.fetchone()
    if result is not None:
        cur.execute(f"SELECT money FROM main WHERE id = {ctx.message.author.id}")
        bux = cur.fetchone()
        bux = str(bux)
        bux = bux[2:-3]
        cur.execute(f"SELECT income FROM main WHERE id = {ctx.message.author.id}")
        income = cur.fetchone()
        income = str(income)
        income = income[2:-3]
        newbux = bux - 10
        newpop = pop + 1
        query = """Update main set money = ? where id = ?"""
        entry = (newbux, ctx.message.author.id)
        cur.execute(query, entry)
        query = """Update main set income = ? where id = ?"""
        entry = (newpop, ctx.message.author.id)
        cur.execute(query, entry)
    if result is None:
        await ctx.send("Lol you don't exist ")
    data.commit()
    cur.close()
    data.close()

@client.command(aliases=['buy-population'])
async def pop(ctx):
    data = sqlite3.connect('db.sqlite')
    cur = data.cursor()
    cur.execute(f"SELECT id FROM main WHERE id = {ctx.message.author.id}")
    result = cur.fetchone()
    if result is not None:
        cur.execute(f"SELECT money FROM main WHERE id = {ctx.message.author.id}")
        bux = cur.fetchone()
        bux = str(bux)
        bux = bux[2:-3]
        cur.execute(f"SELECT population FROM main WHERE id = {ctx.message.author.id}")
        pop = cur.fetchone()
        pop = str(pop)
        pop = pop[2:-3]
        newbux = bux - 5
        newpop = pop + 5
        query = """Update main set money = ? where id = ?"""
        entry = (newbux, ctx.message.author.id)
        cur.execute(query, entry)
        query = """Update main set population = ? where id = ?"""
        entry = (newpop, ctx.message.author.id)
        cur.execute(query, entry)
    if result is None:
        await ctx.send("Lol you don't exist ")
    data.commit()
    cur.close()
    data.close()

@client.command()
async def buy(ctx):
    global prefix
    await ctx.send(f"You need a target for purchase\n{prefix}buy-population/pop\n{prefix}buy-factory")

@client.command()
async def stats(ctx):
    data = sqlite3.connect('db.sqlite')
    cur = data.cursor()
    cur.execute(f"SELECT id FROM main WHERE id = {ctx.message.author.id}")
    embed = discord.Embed(color=ctx.author.color, timestamp=ctx.message.created_at)
    result = cur.fetchone()
    if result is not None:
        embed.add_field(name="Ruler", value=f"<@{ctx.message.author.id}>")
        cur.execute(f"SELECT name FROM main WHERE id = {ctx.message.author.id}")
        nam = cur.fetchone()
        nam = str(nam)
        nam = nam[1:-2]
        embed.add_field(name="Name", value=nam, inline=False)
        cur.execute(f"SELECT money FROM main WHERE id = {ctx.message.author.id}")
        bux = cur.fetchone()
        bux = str(bux)
        bux = bux[2:-3]
        embed.add_field(name="Money", value=bux, inline=False)
        cur.execute(f"SELECT income FROM main WHERE id = {ctx.message.author.id}")
        income = cur.fetchone()
        income = str(income)
        income = income[1:-2]
        embed.add_field(name="Income", value=income, inline=False)
        cur.execute(f"SELECT population FROM main WHERE id = {ctx.message.author.id}")
        pop = cur.fetchone()
        pop = str(pop)
        pop = pop[1:-2]
        embed.add_field(name="Population", value=pop, inline=False)
        embed.set_footer(text="help I am suffering")
        await ctx.send(embed=embed)
    if result is None:
        await ctx.send("Lol you don't exist ")
    data.commit()
    cur.close()
    data.close()


client.run(token)
