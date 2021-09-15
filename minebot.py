import discord
import asyncio
import copy
from discord.ext import commands
from itertools import islice
from collections import defaultdict


TOKEN='ODUxODg5MjkxOTc3MjkzODg2.YL-1ug.G4mJOs2UBujkVjtOzAKM_Gp8gjk'

client = commands.Bot(command_prefix='.')

values=''
WorldCoord={}

@client.event
async def on_ready():
    print('Bot is ready')

@client.command(
    name="input",
    describtion="Allows user to input and save coordinates"
)


async def addCoord(ctx):
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send('Enter what you have found in form \n Dimintion/ Biome: Structure \n ex) Nether: Fortress')

    try:
        msg = await client.wait_for("message", check=check,timeout=30)
    except asyncio.TimeoutError:
        await ctx.send('Sorry you did not reply in time')

    location =msg.content

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send('Please enter the coordinates " (x,y,z) "')

    try:
        msg = await client.wait_for("message", check=check,timeout=30)
    except asyncio.TimeoutError:
        await ctx.send('Sorry you did not reply in time')
    
    coord=msg.content

    for key in WorldCoord.keys():
        if key in WorldCoord.keys():
            newDict=defaultdict(list)
            newDict[location]=defaultdict.append(f"{coord}")
        else:
            log={location:coord}
            WorldCoord.update(log)
    

@client.command(
    title="show",
    description="shows user the saved list coordinates"
)
async def show(ctx):
    count=0
    if len(WorldCoord)==0:
        await ctx.send("No coordinates saved")
    else:
         for key,value in WorldCoord.items():
            count+=1
            await ctx.send(f'{count}) {key} | {WorldCoord.get(key)}')

@client.command(
    title="remove",
    description="allows user to remove specific coordinates"
)
async def remove(ctx):
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send('Enter the coordinates you want to remove (x,y,z)')

    try:
        coord = await client.wait_for("message", check=check,timeout=30)

    except asyncio.TimeoutError:
        await ctx.send('Sorry you did not reply in time')

    for key in WorldCoord.keys():
        if coord.contents!=WorldCoord[key]:
            await ctx.send("Sorry I have not heard of these coordinates!")


    for key in WorldCoord.keys():
        if WorldCoord[key] == coord.content:
            await ctx.send(f"The coordinates {coord.content} ({key}) have been removed")
            del WorldCoord[key]


@client.command(
    title="clear",
    description="Deletes all coordinates"
)
async def clear(ctx):
    if len(WorldCoord)==0:
        await ctx.send("No coordinates to be cleared")

    else:
        WorldCoord.clear()
        await ctx.send("All coordinates have been removed")

@client.command(
    title="find",
    description="Prints the coords the user are searching  for"
)

async def search(ctx):
    sorted={}
    count=0
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send('What are you looking for?')

    try:
        location = await client.wait_for("message", check=check,timeout=30)

    except asyncio.TimeoutError:
        await ctx.send('Sorry you did not reply in time')

    
    for key,value in WorldCoord.items():
        if location.content!=key:
            await ctx.send("Sorry I can't find what your looking for")
        elif location.content==key:
            sorted.update({key:value})
            for key,value in sorted.items():
                count+=1
                await ctx.send(f'{count}) {key} | {value}')


client.run(TOKEN)