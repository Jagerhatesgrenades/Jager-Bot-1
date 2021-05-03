import discord
from discord.ext import commands
from operators import embeds
from functions import operatorList, quotesList, defaultColor, embedAuthor
import random
import datetime

class siege(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def profile(self, ctx, operator):
    operator = operator.lower()

    if operator == "random":
      n = random.randint(0, len(operatorList))

      await ctx.trigger_typing()
      await ctx.send(embed=operatorList[n])

    else:
      await ctx.trigger_typing()
      await ctx.send(embed=embeds[operator])
  
  @commands.command()
  async def quote(self, ctx):
    n = random.randint(0, len(quotesList))
    quote = quotesList[n]

    quoteEmbed = discord.Embed(
      **quote,
      color=defaultColor
    )
    
    quoteEmbed.set_author(**embedAuthor)
    quoteEmbed.timestamp = datetime.datetime.utcnow()
    quoteEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing()
    await ctx.send(embed=quoteEmbed)

def setup(bot):
  bot.add_cog(siege(bot))