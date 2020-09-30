# Recommend to be used on Arch Linux Kernel 5.8.5

#     Coded by Reedeht#0001 in under 1 hour, if you have any issues do not report it to github.

# GITHUB LinK: https://github.com/Reedeht/Basic-Bot
# GITHUB License General Public License

# Discord Server Invite: https://discord.gg/Nf5gpN2

####################CONTROL PANEL####################
####################CONTROL PANEL####################
####################CONTROL PANEL####################

token = 'YOUR TOKEN HERE' #Get a token here: https://discord.com/developers/applications
prefix = 'b' #Change prefix here

####################CONTROL PANEL####################
####################CONTROL PANEL####################
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
    embed.add_field(name=f"{prefix}start", value="Starts your game", inline=False)
    embed.add_field(name=f"{prefix}buy", value="Allows purchasing", inline=False)
    embed.add_field(name=f"{prefix}name", value="Renames yourself", inline=False)
    embed.add_field(name=f"{prefix}update", value="Gets your funds", inline=False)
    embed.add_field(name=f"{prefix}stats", value="Displays your stats", inline=False)
    embed.add_field(name=f"{prefix}buy-factory / factory", value="Adds more factories", inline=False)
    await ctx.send(embed=embed)

@client.event
async def on_ready():
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
        bux = bux[1:-2]
        bux = int(bux)
        cur.execute(f"SELECT income FROM main WHERE id = {ctx.message.author.id}")
        mone = cur.fetchone()
        mone = str(mone)
        mone = mone[1:-2]
        mone = int(mone)
        damndaniel = mone + bux
        query = """Update main set money = ? where id = ?"""
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
        bux = bux[1:-2]
        bux = int(bux)
        cur.execute(f"SELECT income FROM main WHERE id = {ctx.message.author.id}")
        income = cur.fetchone()
        income = str(income)
        income = income[1:-2]
        income = int(income)
        newbux = bux - 1000
        if newbux <bux:
            await ctx.send("Don't have enough Money's")
        else:
            newfac = income + 1
            query = """Update main set money = ? where id = ?"""
            entry = (newbux, ctx.message.author.id)
            cur.execute(query, entry)
            query = """Update main set income = ? where id = ?"""
            entry = (newfac, ctx.message.author.id)
            cur.execute(query, entry)
            await ctx.send("You have gained 1 factory and lost 1000 money")
    if result is None:
        await ctx.send("Lol you don't exist ")
    data.commit()
    cur.close()
    data.close()

@client.command()
async def stats(ctx):
    data = sqlite3.connect('db.sqlite')
    cur = data.cursor()
    cur.execute(f"SELECT id FROM main WHERE id = {ctx.message.author.id}")
    result = cur.fetchone()
    if result is not None:

        cur.execute(f"SELECT name FROM main WHERE id = {ctx.message.author.id}")
        nam = cur.fetchone()
        nam = str(nam)
        nam = nam[2:-3]
        cur.execute(f"SELECT money FROM main WHERE id = {ctx.message.author.id}")
        bux = cur.fetchone()
        bux = str(bux)
        bux = bux[1:-2]
        cur.execute(f"SELECT income FROM main WHERE id = {ctx.message.author.id}")
        income = cur.fetchone()
        income = str(income)
        income = income[1:-2]
        cur.execute(f"SELECT population FROM main WHERE id = {ctx.message.author.id}")
        pop = cur.fetchone()
        pop = str(pop)
        pop = pop[1:-2]
        await ctx.send(f"**Name**\n{nam}\n\n**Money**\n{bux}\n\n**Income**\n{income}\n\n**Population**\n{pop}")
    if result is None:
        await ctx.send("Lol you don't exist ")
    data.commit()
    cur.close()
    data.close()

client.run(token)
