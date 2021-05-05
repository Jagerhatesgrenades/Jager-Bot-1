import discord
from discord.ext import commands
import random
from functions import defaultColor, embedAuthor, gunsList, titleList
import time

class fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def sus(self, ctx, user: discord.Member=None):
    n = random.randint(0, 100)

    if user:
      user = user
    else:
      user = ctx.author

    if n < 100:
      await ctx.trigger_typing()
      await ctx.send(f"{user.display_name} is {n}% sus!")
    else:
      await ctx.trigger_typing()
      await ctx.send(f"""
        {user.display_name} is {n}% sus!
        Impostor 😳😳😳
      """)

  @commands.command()
  async def sexy(self, ctx, user: discord.Member=None):
    n = random.randint(0, 100)

    if user:
      user = user
    else:
      user = ctx.author

    await ctx.trigger_typing()
    await ctx.send(f"{user.display_name} is {n}% sexy!")

  @commands.command()
  async def shoot(self, ctx, user: discord.Member):
    shootEmbed = discord.Embed(
      title=titleList[random.randint(0, len(titleList))],
      description=f"{ctx.author.mention} shot {user.mention} with {gunsList[random.randint(0, len(gunsList))]}",
      color=defaultColor
    )

    shootEmbed.set_author(**embedAuthor)

    await ctx.trigger_typing()
    await ctx.send(embed=shootEmbed)

  @commands.command()
  async def randomchoice(self, ctx, n: int, *choices):
    if n == 0:
      await ctx.trigger_typing()
      await ctx.send(f"{ctx.author.mention}, i chose nothing!")

    elif n == 1:
      await ctx.trigger_typing()
      await ctx.send(f"{ctx.author.mention}, selecting 1 random item...")
      time.sleep(1)
      item = random.sample(choices, n)
      item = "".join(item)
      await ctx.trigger_typing()
      await ctx.send(f"{ctx.author.mention}, I selected `{item}`")

    else:
      await ctx.trigger_typing()
      await ctx.send(f"{ctx.author.mention}, selecting {n} random items...")
      time.sleep(1)
      items = random.sample(choices, n)
      items = "`, `".join(items)
      await ctx.trigger_typing()
      await ctx.send(f"{ctx.author.mention}, I selected `{items}`")

  @commands.command()
  async def rps(self, ctx, userChoice):
    userChoice = userChoice.lower()
    rpsList = ["rock", "paper", "scissors"]
    winDict = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if userChoice in rpsList:
      botChoice = rpsList[random.randint(0,2)]
      winMsg = f"I chose **{botChoice}**, I win!"
      tieMsg = f"I chose **{botChoice}**, it's a tie!"
      loseMsg = f"I chose **{botChoice}**, You win!"

      if winDict[userChoice] == botChoice:
        await ctx.trigger_typing()
        await ctx.send(loseMsg)

      elif userChoice == botChoice:
        await ctx.trigger_typing()
        await ctx.send(tieMsg)

      elif winDict[userChoice] != botChoice:
        await ctx.trigger_typing()
        await ctx.send(winMsg)

    else:
      await ctx.trigger_typing()
      await ctx.send(f"{userChoice} isn't a valid choice!")

  @commands.command()
  async def ping(self, ctx):
    await ctx.trigger_typing()
    await ctx.send(f"Ping: {round(self.bot.latency * 1000)} ms")

def setup(bot):
  bot.add_cog(fun(bot))