import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from replit import db
from functions import defaultColor, embedAuthor, updateDictDB
from actLogging import logTagCreate, logTagDelete, logTagEdit
import datetime

class tags(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.loggingChannel = self.bot.get_channel(838724538220937307)

  @commands.group(name="tags", invoke_without_command=True)
  @has_permissions(manage_channels=True)
  async def tags(self, ctx):
    tagsDict = db["tags"]
    if tagsDict:
      await ctx.trigger_typing()
      await ctx.send("\n".join([f"**{i + 1}.** {tag}: {func}" for i, (tag, func) in enumerate(tagsDict.items())]))

    else:
      await ctx.trigger_typing()
      await ctx.send(f"")

  @tags.command(name="add")
  @has_permissions(manage_channels=True)
  async def add_subcommand(self, ctx, tagName, *tagReply):
    tagsDict = db["tags"]
    if tagName not in tagsDict:
      tagReply = " ".join(tagReply)

      tagCreationEmbed = discord.Embed(
        title="Tag created",
        description=f"""
        Name: **{tagName}**

        Reply: **{tagReply}**
        """,
        color=defaultColor
      )

      tagCreationEmbed.set_author(**embedAuthor)
      tagCreationEmbed.timestamp = datetime.datetime.utcnow()
      tagCreationEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

      await updateDictDB("tags", tagName, tagReply)
      await ctx.trigger_typing()
      await ctx.send(embed=tagCreationEmbed)
      logMsg = await logTagCreate(ctx.author, tagName, tagReply)
      await self.loggingChannel.send(embed=logMsg)

    else:
      await ctx.trigger_typing()
      await ctx.send(f"The tag **{tagName}** already exits. You can edit it with `j!tags edit {tagName} <new reply>`")

  @tags.command(name="delete")
  @has_permissions(manage_channels=True)
  async def delete_subcommand(self, ctx, tagName):
    tagsDict = db["tags"]
    if tagName in tagsDict:
      tagReply = tagsDict[tagName]
      del tagsDict[tagName]
      db["tags"] = tagsDict
      await ctx.trigger_typing()
      await ctx.send(f"Deleted the tag **{tagName}**")
      logMsg = await logTagDelete(ctx.author, tagName, tagReply)
      await self.loggingChannel.send(embed=logMsg)

    else:
      await ctx.trigger_typing()
      await ctx.send(f"Couldn't find a tag with the name **{tagName}**")

  @tags.command(name="edit")
  @has_permissions(manage_channels=True)
  async def edit_subcommand(self, ctx, tagName, *tagReply):
    tagsDict = db["tags"]
    if tagName in tagsDict:
      oldTagReply = tagsDict[tagName]
      tagReply = " ".join(tagReply)
      db["tags"][tagName] = tagReply
      await ctx.trigger_typing()
      await ctx.send(f"Set the reply for the tag **{tagName}** to \"{tagReply}\"")
      logMsg = await logTagEdit(ctx.author, oldTagReply, tagReply)
      await self.loggingChannel.send(embed=logMsg)

    else:
      await ctx.trigger_typing()
      await ctx.send(f"Couldn't find a tag with the name **{tagName}**")

def setup(bot):
  bot.add_cog(tags(bot))