import os
import matplotlib.pyplot as plt
import numpy as np
import random
import discord
from scipy.stats import mode
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from discord.ext import commands
from dotenv import load_dotenv


from board import getboard
from words import getwords
from maps import getmap

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

start_flag = 0
captain_blue = ''
captain_red = ''
game_flag = 0
bot = commands.Bot(command_prefix='!')


@bot.command(name='start', help='Starts a game')
async def start(ctx):
    global start_flag
    global captain_blue
    global captain_red
    start_flag = 1
    captain_blue = ''
    captain_red = ''
    await ctx.send('Game started')


@bot.command(name='captain_blue', help='Type to be blue captain')
async def captain_blue(ctx):
    global start_flag
    global captain_blue
    if (start_flag == 0):
        await ctx.send("Game not started")
    else:
        if (len(str(captain_blue)) > 0):
            await ctx.send('Captain already selected')
        else:
            captain_blue = ctx.author
            await ctx.send('{} is blue captain now'.format(captain_blue))


@bot.command(name='captain_red', help='Type to be red captain')
async def captain_blue(ctx):
    global start_flag
    global captain_red
    if (start_flag == 0):
        await ctx.send("Game not started")
    else:
        if (len(str(captain_red)) > 0):
            await ctx.send('Captain already selected')
        else:
            captain_red = ctx.author
            await ctx.send('{} is red captain now'.format(captain_red))


@bot.command(name='end', help='ends game')
async def end(ctx):
    global start_flag
    global captain_red
    global captain_blue
    global game_flag
    game_flag = 0
    start_flag = 0
    captain_red = ''
    captain_blue = ''
    await ctx.send('Game ended')


@bot.command(name='board', help='Generate and send board to captains')
async def board(ctx):
    global captain_blue
    global captain_red
    if (len(str(captain_red)) > 0 and len(str(captain_blue)) > 0):
        global starting
        global board
        board = getboard()
        starting = mode(getboard(), axis=None)[0][0]
        await captain_blue.send(file=discord.File('board.png'))
        await captain_red.send(file=discord.File('board.png'))
        await ctx.send('Board sended')
    else:
        await ctx.send('Captains not found')


@bot.command(name='words', help='Generate set of words')
async def words(ctx):
    if start_flag == 1:
        global wor
        global guesses
        wor = getwords()
        guesses = np.full((5, 5), -2)
        getmap(wor, guesses)
        await ctx.send('words generated')
        await ctx.send(file=discord.File('game_board.png'))
    else:
        ctx.send("Game not started")


@bot.command(name='tap', help=' ')
async def tap(ctx, word):
    if start_flag == 1:

        global starting
        if starting == -1:
            cur = captain_blue
            await ctx.send("Blues turn")
        else:
            cur = captain_red
            await ctx.send("Reds turn")

        if (ctx.author == cur):
            global guesses
            if word in wor:
                x = wor[word][0]
                y = wor[word][1]
                guesses[y][x] = board[y][x]
                getmap(wor, guesses)
                await ctx.send(file=discord.File('game_board.png'))
                if (board[y][x] == starting):
                    await ctx.send("It's still your turn")
                else:
                    starting = -starting
                    await ctx.send("You failed")
                if (board[y][x] == 2):
                    await ctx.send("Game over, you hit assasin")
            else:
                await ctx.send("Not such word")
        else:
            await ctx.send("not your turn")
    else:
        ctx.send("Game not started")

# end od command lines
bot.run(TOKEN)
