import discord
import tryhardTiem as tt
import extras as ex
import stringShenanigans as ss
import chars as c
from discord.ext import commands

client = discord.Client()

token = "NjQ5Njg5MTM1MTc4ODQyMTUx.XeFPsA.EnzqLZeZyf00nSI2HMyG1Opw3xA"

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    await client.change_presence(activity=discord.Game(name="timetables |  /help"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        embed.add_field(name="HWAH", value="Hello!", inline=True)
        await message.channel.send(embed=embed)


@client.event
async def on_message(message):
    server = message.guild

    if message.author == client.user:
        return

    if message.content == "/help":
        embed = discord.Embed(color=0xddb11a)
        newMessage = ex.helper()
        embed.add_field(name="Help!", value=newMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "/gen classpect":
        embed = discord.Embed(color=0xddb11a)
        newMessage = ex.gogtiergen()
        embed.add_field(name="Classpect!", value=newMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "/gen invite":
        embed = discord.Embed(color=0xddb11a)
        newMessage = tt.invite()
        embed.add_field(name="Invite!", value=newMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/vibe "):
        embed = discord.Embed(color=0xddb11a)
        newMessage = message.content[6:]
        vibeMessage = ex.vibe_check(newMessage)
        embed.add_field(name="Vibe Check!", value=vibeMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/scritch "):
        embed = discord.Embed(color=0xddb11a)
        newMessage = message.content[9:]
        scritchMessage = ex.scritches(newMessage)
        embed.add_field(name="Scritches!", value=scritchMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/chars add"):
        embed = discord.Embed(color=0xddb11a)
        newMessage = message.content.split("/chars add ")
        charsNames = newMessage[-1]
        outMessage = c.charsadd(server, charsNames)
        embed.add_field(name="Characters!", value=outMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/chars list"):
        embed = discord.Embed(color=0xddb11a)
        outMessage = c.charslist(server)
        embed.add_field(name="Characters!", value=outMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/chars remove"):
        embed = discord.Embed(color=0xddb11a)
        newMessage = message.content.split("/chars remove ")
        charsNames = newMessage[-1]
        outMessage = c.charsremove(server, charsNames)
        embed.add_field(name="Characters!", value=outMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/chars random"):
        embed = discord.Embed(color=0xddb11a)
        outMessage = c.charsrandom(server)
        embed.add_field(name="Characters!", value=outMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/") and " " in message.content and "add" not in message.content and "remove" not in message.content and "list" not in message.content:
        embed = discord.Embed(color=0xddb11a)
        newMessage = message.content[1:]
        diceMessage = tt.multiroll(newMessage)
        embed.add_field(name="Multi Dice!", value=diceMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/") and "d" not in message.content:
        embed = discord.Embed(color=0xddb11a)
        newMessage = message.content[1:]
        diceMessage = ex.mathdice(newMessage)
        embed.add_field(name="Math!", value=diceMessage, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith("/") and "d" in message.content and " " not in message.content:
        embed = discord.Embed(color=0xddb11a)
        newMessage = message.content[1:]
        diceMessage = ss.dicemaxmin2(newMessage)
        embed.add_field(name="Dice!", value=diceMessage, inline=False)
        await message.channel.send(embed=embed)

client.run(token)
