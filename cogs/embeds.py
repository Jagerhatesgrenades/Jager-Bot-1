import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from functions import defaultColor, embedAuthor, updateListDB
from actLogging import logRuleAdd, logRuleDelete, logRuleEdit
from replit import db

class embeds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.loggingChannel = self.bot.get_channel(838724538220937307)

  @commands.group(name="rules", invoke_without_command=True)
  async def rules(self, ctx):

    rulesEmbed = discord.Embed(
      title="Jäger Army Rules",
      description="Failure to follow the rules will result in punishment",
      color=defaultColor
    ) 

    for i, rule in enumerate(db["rules"]):
      rulesEmbed.add_field(
        name=f"{i + 1}.",
        value=rule,
        inline=False
      )

    rulesEmbed.set_author(**embedAuthor)

    await ctx.trigger_typing()
    await ctx.send(embed=rulesEmbed)

  @rules.command(name="add")
  @has_permissions(manage_channels=True)
  async def add_subcommand(self, ctx, *desc):
    rulesN = len(db["rules"])

    await updateListDB("rules", " ".join(desc))

    await ctx.trigger_typing()
    await ctx.send(f"Added rule {rulesN + 1} to the rules")
    logMsg = await logRuleAdd(ctx.author, rulesN + 1, " ".join(desc))
    await self.loggingChannel.send(embed=logMsg)

  @rules.command(name="remove")
  @has_permissions(manage_channels=True)
  async def remove_subcommand(self, ctx, rule: int):
    ruleIndex = rule - 1
    rulesN = len(db["rules"])

    if rule <= rulesN:
      rules = db["rules"]
      del rules[ruleIndex]
      db["rules"] = rules
      
      await ctx.trigger_typing()
      await ctx.send(f"Removed rule {rule}")
      logMsg = await logRuleDelete(ctx.author, rule, rules[ruleIndex])
      await self.loggingChannel.send(embed=logMsg)

    else:
      await ctx.trigger_typing()
      await ctx.send(f"There is no rule {rule}")

  @rules.command(name="edit")
  @has_permissions(manage_channels=True)
  async def edit_subcommand(self, ctx, rule: int, *content):
    ruleIndex = rule - 1
    rules = db["rules"]
    oldRule = rules[ruleIndex]
    rules[ruleIndex] = " ".join(content)
    db["rules"] = rules

    await ctx.trigger_typing()
    await ctx.send(f"Updated rule {rule}")
    logMsg = await logRuleEdit(ctx.author, rule, oldRule, " ".join(content))
    await self.loggingChannel.send(embed=logMsg)

  @rules.command(name="update")
  @has_permissions(manage_channels=True)
  async def update_subcommand(self, ctx, msgID):
    rulesMsg = await ctx.fetch_message(msgID)

    rulesEmbed = discord.Embed(
      title="Jäger Army Rules",
      description="Failure to follow the rules will result in punishment",
      color=defaultColor
    ) 

    for i, rule in enumerate(db["rules"]):
      rulesEmbed.add_field(
        name=f"{i + 1}.",
        value=rule,
        inline=False
      )

    rulesEmbed.set_author(**embedAuthor)

    await rulesMsg.edit(embed=rulesEmbed)

def setup(bot):
  bot.add_cog(embeds(bot))