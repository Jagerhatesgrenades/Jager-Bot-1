import discord
from discord.ext import commands
from discord.ext.commands import has_role
from functions import defaultColor, embedAuthor, racistWords, staffID, dababyReactions
import datetime
from replit import db
import random

class wordDetection(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.dmChannelID = 847408971967234058

  @commands.Cog.listener()
  async def on_message(self, msg):
    if not msg.author.bot:
      tagsDict = db["tags"]

      lowerMessage = msg.content.lower().split()

      if any(word in lowerMessage for word in racistWords):
        logChannel = self.bot.get_channel(769668422631424030)

        racistEmbed = discord.Embed(
          title="N word detection",
          description=f"`{msg.author}` | `{msg.author.display_name}` | `{msg.author.id}`",
          color=defaultColor
        )

        racistEmbed.add_field(
          name="Message",
          value=f"`{msg.content}`",
          inline=False
        )
        
        racistEmbed.timestamp = datetime.datetime.utcnow()
        racistEmbed.set_author(**embedAuthor)
        racistEmbed.set_footer(text=msg.author, icon_url=msg.author.avatar_url)

        await msg.channel.send(f"{msg.author.mention}, nice N word bro!")
        await logChannel.send(embed=racistEmbed)
        await msg.delete()

      elif any(word in lowerMessage for word in ["dababy"]):
        await msg.add_reaction("<:JA_DaCar:810326691548233738>")
        await msg.channel.send(dababyReactions[random.randint(0, len(dababyReactions) - 1)])

      else:
        for tag, tagReply in tagsDict.items():
          if msg.content == f"j!{tag}":
            await msg.channel.trigger_typing()
            await msg.channel.send(tagReply)

def setup(bot):
  bot.add_cog(wordDetection(bot))