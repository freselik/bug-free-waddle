import discord
from random import randint
from discord.ext import commands

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="omg"))
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def rps(ctx, choice = None):
    if choice == None:
        await ctx.send("Please give a choice! (Rock, Paper, Scissors)")

    choice.lower()
    kpn = ["rock", "paper", "scissors"]
    komputer = kpn[randint(0, 2)]

    if choice == komputer:
        await ctx.send("Tie!")
    elif choice == "rock":
        if komputer == "paper":
            await ctx.send("U Lose!")
        else:
            await ctx.send("U Win!")
    elif choice == "paper":
        if komputer == "scissors":
            await ctx.send("U Lose!")
        else:
            await ctx.send("U Win!")
    elif choice == "scissors":
        if komputer == "rock":
            await ctx.send("U Lose!")
        else:
            await ctx.send("U Win!")
    else:
        await ctx.send("Please give a valid choice! (rock, paper, scissors")


client.run(str(os.environ.get('TOKEN')))
