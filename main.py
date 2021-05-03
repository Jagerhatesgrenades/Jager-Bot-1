from discord.ext import commands, tasks
import discord
import os
from replit import db
from functions import categoryRoles

intents = discord.Intents.default()
intents.members = True
intents.bans = True

bot = commands.Bot(
  command_prefix="j!",
  help_command=None,
  intents=intents
)

@tasks.loop(minutes=10.0)
async def updateCategories():
  print("Updating categories...")
  updated = False
  for member in bot.get_guild(769576914460475454).members:
    if not member.bot:
      userTopRole = [role for role in reversed(member.roles) if role.id not in categoryRoles][0]
      for role in bot.get_guild(769576914460475454).roles:
        if role < userTopRole and role.id in categoryRoles and role not in member.roles:
          await member.add_roles(role)
          print(f"Gave the role {role.name} to {member}")
          updated = True
        if role > userTopRole and role.id in categoryRoles and role in member.roles:
          await member.remove_roles(role)
          print(f"Removed the role {role.name} from {member}")
          updated = True

  if updated is False:
    print("No categories updated")

@bot.event
async def on_ready():
  print("Bot started")

  game = discord.Game("with Jäger")

  await bot.change_presence(
    status=discord.Status.online,
    activity=game
  )

  if "isVoting" not in db.keys():
    db["isVoting"] = False

  if "rules" not in db.keys():
    db["rules"] = []

  if "tags" not in db.keys():
    db["tags"] = {}

  bot.load_extension("cogs.fun")
  bot.load_extension("cogs.help")
  bot.load_extension("cogs.info")
  bot.load_extension("cogs.staff")
  bot.load_extension("cogs.siege")
  bot.load_extension("cogs.sotw")
  bot.load_extension("cogs.wordDetection")
  bot.load_extension("cogs.apis")
  bot.load_extension("cogs.embeds")
  bot.load_extension("cogs.randomxp")
  bot.load_extension("cogs.tags")
  bot.load_extension("cogs.polls")

  updateCategories.start()

  @bot.event  
  async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      missingPerms = ",  ".join(error.missing_perms)
      await ctx.trigger_typing()
      await ctx.send(f"You need the permission(s) **{missingPerms.upper()}** to use this command")

    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.trigger_typing()
      await ctx.send("You're missing required arguments, see j!help for more info")

bot.run(os.getenv("TOKEN"))