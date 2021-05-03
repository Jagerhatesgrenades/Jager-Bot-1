import discord
from discord.ext import commands
from discord.ext.commands import has_any_role
from functions import defaultColor, embedAuthor, staffID, donatorTierVID, emojis, regionalIndicators
import datetime

class polls(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @has_any_role(staffID, donatorTierVID)
  async def poll(self, ctx, ping, question, *args):
    questionsList = "\n".join(f"{regionalIndicators[i]} {answer}" for i, answer in enumerate(args))

    pollEmbed = discord.Embed(
      title=question,
      description=questionsList,
      color=defaultColor
    )

    pollEmbed.set_author(**embedAuthor)
    pollEmbed.timestamp = datetime.datetime.utcnow()
    pollEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    if ping.lower() == "ping":
      await ctx.trigger_typing()
      await ctx.send("<@&820074738406916106>")
      pollMsg = await ctx.send(embed=pollEmbed)

    else:
      await ctx.trigger_typing()
      pollMsg = await ctx.send(embed=pollEmbed)

    for i in range(0, len(args)):
      await pollMsg.add_reaction(emojis[i])

def setup(bot):
  bot.add_cog(polls(bot))