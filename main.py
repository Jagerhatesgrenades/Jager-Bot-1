from discord.ext import commands, tasks
import discord
import os
from replit import db
from functions import categoryRoles, NoPermErrorMessages
import time
import random

intents = discord.Intents.default()
intents.members = True
intents.bans = True

bot = commands.Bot(
  command_prefix="j!",
  help_command=None,
  intents=intents
)

@tasks.loop(minutes=60)
async def updateCategories():
  for member in bot.get_guild(769576914460475454).members:
    if not member.bot:
      userTopRole = [role for role in reversed(member.roles) if role.id not in categoryRoles][0]
      for role in bot.get_guild(769576914460475454).roles:
        if role < userTopRole and role.id in categoryRoles and role not in member.roles:
          await member.add_roles(role)
          print(f"Gave the role {role.name} to {member}")
          time.sleep(0.3)
        if role > userTopRole and role.id in categoryRoles and role in member.roles:
          await member.remove_roles(role)
          print(f"Removed the role {role.name} from {member}")
          time.sleep(0.3)

  print("Updated categories")

@tasks.loop(seconds=1.0)
async def updateCooldowns():
  xpDB = db["xp"]
  for user in xpDB:
    cooldown = xpDB[user][1]
    if cooldown > 0:
      cooldown -= 1
      db["xp"][user][1] = cooldown

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

  if "xp" not in db.keys():
	  db["xp"] = {}

  if "xpMulti" not in db.keys():
	  db["xpMulti"] = {}

  if "nominations" not in db.keys():
	  db["nominations"] = {}

  if "votes" not in db.keys():
    db["votes"] = {}

  if "xpDisabledChannels" not in db.keys():
    db["xpDisabledChannels"] = []

  if "xpRate" not in db.keys():
    db["xpRate"] = [500, 1000]

  for filename in os.listdir("./cogs"):
	  if filename.endswith(".py"):
  		bot.load_extension(f"cogs.{filename[:-3]}")

  updateCooldowns.start()
  updateCategories.start()

  print("Started, waiting for categories...")

@bot.event  
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.trigger_typing()
    await ctx.send(NoPermErrorMessages[random.randint(0, len(NoPermErrorMessages) - 1)])

  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.trigger_typing()
    await ctx.send("You're missing required arguments, see j!help for more info")

  elif isinstance(error, commands.NotOwner):
    await ctx.trigger_typing()
    await ctx.send("You have to be the bot owner to use this command")

  elif isinstance(error, commands.MissingRole):
    await ctx.trigger_typing()
    await ctx.send(f"You need the role {error.MissingRole.name} to use this command")

bot.run(os.getenv("TOKEN"))