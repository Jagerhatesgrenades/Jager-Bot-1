import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.utils import get
from functions import defaultColor
import datetime

class modMail(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.guildID = 769576914460475454
    self.mailCategoryID = 847422359577034772
    self.logChannelID = 847422385782784020

  async def newMailChannel(self, user: discord.Member):
    guild = self.bot.get_guild(self.guildID)
    mailCategory = get(guild.categories, id=self.mailCategoryID)
    logChannel = self.bot.get_channel(self.logChannelID)

    newChannel = await guild.create_text_channel(f"{user.name}-{user.discriminator}", category=mailCategory, topic=str(user.id), reason=f"New ticket by {user}")

    logEmbed = discord.Embed(
      title="New ticket",
      description=newChannel.mention,
      color=defaultColor
    )

    logEmbed.set_author(name=user, icon_url=user.avatar_url)
    logEmbed.timestamp = datetime.datetime.utcnow()

    newChannelEmbed = discord.Embed(
      title="New Ticket",
      description="Send a message starting with `--` to send it in this channel and not to the user\n`j!close [reason]` to close the ticket",
      color=defaultColor
    )

    await logChannel.send(embed=logEmbed)

    await newChannel.send(embed=newChannelEmbed)
    
    return newChannel

  @commands.Cog.listener()
  async def on_message(self, msg):
    if not msg.author.bot:
      guild = self.bot.get_guild(self.guildID)
      mailCategory = get(guild.categories, id=self.mailCategoryID)
      if isinstance(msg.channel, discord.channel.DMChannel):
        for channel in mailCategory.channels:
          if channel.topic == str(msg.author.id):
            existingChannel = True
            mailChannel = channel
            break

          existingChannel = False

        if not existingChannel:
          mailChannel = await self.newMailChannel(msg.author)

          receiveEmbed = discord.Embed(
            title="Message received",
            description=msg.content,
            color=discord.Color.green()
          )

          receiveEmbed.set_author(name=msg.author, icon_url=msg.author.avatar_url)
          receiveEmbed.timestamp = datetime.datetime.utcnow()

          sendEmbed = discord.Embed(
            title="Message sent",
            description=msg.content,
            color=discord.Color.orange()
          )

          sendEmbed.set_author(name=msg.author, icon_url=msg.author.avatar_url)
          sendEmbed.timestamp = datetime.datetime.utcnow()

          await mailChannel.send(embed=receiveEmbed)
          await msg.author.send(embed=sendEmbed)
          
          if msg.attachments:
            await mailChannel.send(msg.attachments[0].url)
            await msg.author.send(msg.attachments[0].url)

      elif msg.channel in mailCategory.channels and msg.channel.name != "log":
        if not msg.content.startswith("--") and not msg.content.startswith("j!close"):
          user = self.bot.get_user(int(msg.channel.topic))

          receiveEmbed = discord.Embed(
            title="Message received",
            description=msg.content,
            color=discord.Color.green()
          )

          receiveEmbed.set_author(name=msg.author, icon_url=msg.author.avatar_url)
          receiveEmbed.timestamp = datetime.datetime.utcnow()

          sendEmbed = discord.Embed(
            title="Message sent",
            description=msg.content,
            color=discord.Color.orange()
          )

          sendEmbed.set_author(name=msg.author, icon_url=msg.author.avatar_url)
          sendEmbed.timestamp = datetime.datetime.utcnow()

          await msg.channel.send(embed=sendEmbed)
          await user.send(embed=receiveEmbed)

          if msg.attachments:
            await msg.channel.send(msg.attachments[0].url)
            await msg.author.send(msg.attachments[0].url)

          await msg.delete()

  @commands.command()
  async def close(self, ctx, *reason):
    guild = self.bot.get_guild(self.guildID)
    mailCategory = get(guild.categories, id=self.mailCategoryID)
    logChannel = self.bot.get_channel(self.logChannelID)

    if reason:
      reason = " ".join(reason)

    else:
      reason = None

    if ctx.channel in mailCategory.channels:
      deleteEmbed = discord.Embed(
        title="Ticket closed",
        description=f"Reason: {reason}",
        color=defaultColor
      )

      deleteEmbed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
      deleteEmbed.timestamp = datetime.datetime.utcnow()

      await logChannel.send(embed=deleteEmbed)
      await self.bot.get_user(int(ctx.channel.topic)).send(embed=deleteEmbed)

      await ctx.channel.delete(reason=f"Ticket closed by {ctx.author}")

    else:
      await ctx.trigger_typing()
      await ctx.send("This isn't a ticket channel")

def setup(bot):
  bot.add_cog(modMail(bot))