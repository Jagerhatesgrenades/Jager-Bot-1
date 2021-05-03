import discord
import datetime
from functions import defaultColor, embedAuthor


async def logTagCreate(user, tagName, tagReply):
  logEmbed = discord.Embed(
    title="Tag created",
    description=f"""
      Command: **{tagName}**
      Reply: **{tagReply}**
    """,
    color=defaultColor
  )

  logEmbed.set_author(**embedAuthor)
  logEmbed.timestamp = datetime.datetime.utcnow()
  logEmbed.set_footer(text=user, icon_url=user.avatar_url)

  return logEmbed

async def logTagEdit(user, oldReply, newReply):
  logEmbed = discord.Embed(
    title="Tag edited",
    description=f"""
      Old reply: **{oldReply}**
      New reply: **{newReply}**
    """,
    color=defaultColor
  )

  logEmbed.set_author(**embedAuthor)
  logEmbed.timestamp = datetime.datetime.utcnow()
  logEmbed.set_footer(text=user, icon_url=user.avatar_url)

  return logEmbed

async def logTagDelete(user, tagName, tagReply):
  logEmbed = discord.Embed(
    title="Tag deleted",
    description=f"""
      Command: **{tagName}**
      Reply: **{tagReply}**
    """,
    color=defaultColor
  )

  logEmbed.set_author(**embedAuthor)
  logEmbed.timestamp = datetime.datetime.utcnow()
  logEmbed.set_footer(text=user, icon_url=user.avatar_url)

  return logEmbed


async def logRuleAdd(user, ruleN, rule):
  logEmbed = discord.Embed(
    title="Rule added",
    description=f"""
      Rule N.: **{ruleN}**
      Rule: **{rule}**
    """,
    color=defaultColor
  )

  logEmbed.set_author(**embedAuthor)
  logEmbed.timestamp = datetime.datetime.utcnow()
  logEmbed.set_footer(text=user, icon_url=user.avatar_url)

  return logEmbed

async def logRuleEdit(user, ruleN, oldRule, newRule):
  logEmbed = discord.Embed(
    title="Rule edited",
    description=f"""
      Rule N.: **{ruleN}**
      Old rule: **{oldRule}**
      New rule: **{newRule}**
    """,
     color=defaultColor
  )

  logEmbed.set_author(**embedAuthor)
  logEmbed.timestamp = datetime.datetime.utcnow()
  logEmbed.set_footer(text=user, icon_url=user.avatar_url)

  return logEmbed

async def logRuleDelete(user, ruleN, rule):
  logEmbed = discord.Embed(
    title="Rule deleted",
    description=f"""
      Rule N.: **{ruleN}**
      rule: **{rule}**
    """,
    color=defaultColor
  )

  logEmbed.set_author(**embedAuthor)
  logEmbed.timestamp = datetime.datetime.utcnow()
  logEmbed.set_footer(text=user, icon_url=user.avatar_url)

  return logEmbed
