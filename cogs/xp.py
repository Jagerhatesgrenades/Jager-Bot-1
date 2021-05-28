import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, is_owner
from discord.utils import get
from replit import db
import random
from xpInfo import xpLevelDict
from functions import defaultColor, embedAuthor, levelRoles
import datetime
import math

class xp(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.toxicID = 769599121626497034

  async def syncRoles(self, userID):
    userXP = db["xp"][str(userID)][0]
    for lvl, xp in xpLevelDict.items():
      if userXP < xp:
        userLevel = lvl - 1
        break
 
    for i, lvl in enumerate(levelRoles.keys()):
      if userLevel < lvl:
        levelRoleID = levelRoles[list(levelRoles.keys())[i - 1]]
        break

    guild = self.bot.get_guild(769576914460475454)
    user = get(guild.members, id=int(userID))
    levelRole = get(guild.roles, id=levelRoleID)

    userLevelRoles = [role for role in user.roles if role.id in levelRoles.values()]

    if len(userLevelRoles) != 1 or levelRoleID != userLevelRoles[0]:
      for role in userLevelRoles:
        await user.remove_roles(role)

      await user.add_roles(levelRole)
      return True

    else:
      return False

  def addXP(self, user, amount):
    amount = int(amount)
    if user in db["xp"]:
      if str(amount)[0] != "-":
        currentXp = db["xp"][user][0]
        newAmount = currentXp + amount
        db["xp"][user][0] = newAmount
        return True

      else:
        amount = abs(amount)
        currentXp = db["xp"][user][0]
        if amount > currentXp:
          amount = currentXp

        newAmount = currentXp - amount
        db["xp"][user][0] = newAmount
        return False

    else:
      if amount > 0:
        db["xp"][user] = [amount, 60]
        return True

      else:
        return False

  def getMultiplier(self, returnType, user: discord.Member):
    xpMultiplierDict = dict(db["xpMulti"])
    guild = self.bot.get_guild(769576914460475454)
    userRoleIDs = [str(role.id) for role in user.roles]

    multiplierRoles = {k: v for k, v in xpMultiplierDict.items() if k in userRoleIDs}

    if multiplierRoles:
      multiplierRoles = [k for k, v in multiplierRoles.items() if v == max(multiplierRoles.values())]

      if len(multiplierRoles) == 1:
        if returnType == "role":
          return guild.get_role(int(multiplierRoles[0]))

        elif returnType == "val":
          return float(xpMultiplierDict[str(multiplierRoles[0])])

        else:
          return None
        

      else:
        multiplierRoles = [int(role.id) for role in reversed(user.roles) if str(role.id) in multiplierRoles]
        multiplierRole = guild.get_role(multiplierRoles[0])
        multiplier = float(xpMultiplierDict[str(multiplierRoles[0])])

        if returnType == "role":
          return multiplierRole

        elif returnType == "val":
          return multiplier

        else:
          return None

    else:
      return None

  def checkLevelUp(self, xp1, xp2):
    for i in xpLevelDict:
      if xp1 < xpLevelDict[i]:
        level1 = i - 1
        break
    
    for i in xpLevelDict:
      if xp2 < xpLevelDict[i]:
        level2 = i - 1
        break
    
    if level1 < level2:
      return level2

    else:
      return False
     
  @commands.command(aliases=["r", "level"])
  async def rank(self, ctx, user: discord.Member=None):
    if user is None:
      user = ctx.author

    xpDB = db["xp"]

    userID = str(user.id)
    if userID in xpDB:
      userXpDB = xpDB[userID]
      currentXp = userXpDB[0]
      cooldown = userXpDB[1]

      for i in xpLevelDict:
        if currentXp < xpLevelDict[i]:
          currentLevel = i - 1
          break
 
      remainingXP = xpLevelDict[currentLevel + 1] - currentXp
      reqXP = xpLevelDict[currentLevel + 1]
      xpDistance = xpLevelDict[currentLevel + 1] - xpLevelDict[currentLevel]
      percentage = (xpDistance - remainingXP) / xpDistance * 100
      bar = "".join("\_" if x > percentage else "█" for x in range(5, 101, 5))

      curLvlXp = xpLevelDict[currentLevel]
      nextLvlXp = xpLevelDict[currentLevel + 1]

      xpLine = f"**{'{:,}'.format(curLvlXp)}** {'-' * 25} **{'{:,}'.format(nextLvlXp)}**"
  
      multiplier = self.getMultiplier("val", user)
      multiplierRole = self.getMultiplier("role", user)

      multiplier = f"{multiplierRole.mention if multiplierRole is not None else None} | {multiplier if multiplier is not None else 1.0}x"

      xpDB = {k: v[0] for k, v in db["xp"].items()}
      statDB = {k: v for k, v in sorted(xpDB.items(), key=lambda item: item[1])}

      positions = {i + 1: int(k) for i, (k, v) in enumerate(reversed(statDB.items()))}
      position = list(positions.keys())[list(positions.values()).index(user.id)]

      levelEmbed = discord.Embed(
        color=[role.color for role in reversed(user.roles) if str(role.color) != "#000000"][0]
      )

      levelEmbed.add_field(
        name="XP",
        value=f"{'{:,}'.format(currentXp)}\nlvl. {currentLevel}",
        inline=True
      )

      levelEmbed.add_field(
        name="Next Level",
        value=f"{'{:,}'.format(reqXP)} XP\n{'{:,}'.format(remainingXP)} more",
        inline=True
      )

      levelEmbed.add_field(
        name="Cooldown",
        value=f"{cooldown} sec" if cooldown > 0 else "None",
        inline=True
      )

      levelEmbed.add_field(
        name="Multiplier",
        value=multiplier,
        inline=True
      )


      levelEmbed.add_field(
        name="Progress",
        value=f"{bar} ({round(percentage, 2)}%)\n{xpLine}\n\n{position} / {len(positions)}",
        inline=False
      )

      levelEmbed.set_thumbnail(url=user.avatar_url)
      levelEmbed.set_author(name=user, icon_url=user.avatar_url)
      levelEmbed.timestamp = datetime.datetime.utcnow()
      levelEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

      await ctx.trigger_typing()
      await ctx.send(embed=levelEmbed)

    else:
      await ctx.trigger_typing()
      await ctx.send(f"I can't find **{user}** in the database, this could be because you haven't sent a message yet")

  @commands.command(aliases=["givexp", "xpadd"])
  @has_permissions(manage_guild=True)
  async def addxp(self, ctx, user: discord.Member, xpAmount: int):
    currentXp = db["xp"][str(user.id)][0]
    xpAdd = self.addXP(str(user.id), xpAmount)
    if xpAdd:
      await ctx.trigger_typing()
      await ctx.send(f"Gave **{xpAmount}** XP to **{user.display_name}**")
      lvlUp = self.checkLevelUp(currentXp, currentXp + xpAmount)
      if lvlUp:
        await ctx.send(f"Holy Jäger! **{user.display_name}** just leveled up!\nYou are now level **{lvlUp}**")

    else:
      await ctx.trigger_typing()
      await ctx.send(f"Took **{abs(xpAmount)}** XP from **{user.display_name}**")

    await self.syncRoles(str(user.id))

  @commands.command(aliases=["t", "leaderboard"])
  async def top(self, ctx, page: int=1):
    if page is None:
      page = 1

    xpDB = {k: v[0] for k, v in db["xp"].items()}
    statDB = {k: v for k, v in sorted(xpDB.items(), key=lambda item: item[1])}
    indexStart = page * 10 - 10

    def getLevel(xp):
      for i in xpLevelDict:
        if xp < xpLevelDict[i]:
          return i - 1
    
      return 500

    def getUser(userID):
      return get(ctx.guild.members, id=int(userID))

    leaderboard = [f"**{i + 1}.** lvl. **{getLevel(v)}** {getUser(k).mention if getUser(k) else k} ({'{:,}'.format(v)} XP)" for i, (k, v) in enumerate(reversed(statDB.items()))]

    if (indexStart + 10) <= (len(leaderboard) - 1):
      indexEnd = indexStart + 10
    else:
      indexEnd = len(leaderboard)

    maxPages = len(leaderboard) / 10
    maxPages = math.ceil(maxPages)
    if page <= maxPages:
      leaderboard = "\n".join([leaderboard[i] for i in range(indexStart, indexEnd)])

      topEmbed = discord.Embed(
        description=f"""
          {leaderboard}

          Page {page} / {maxPages}
        """,
        color=defaultColor
      )

      topEmbed.set_author(name="Jäger Army XP Leaderboard", icon_url=ctx.guild.icon_url)
      topEmbed.timestamp = datetime.datetime.utcnow()
      topEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

      await ctx.trigger_typing()
      await ctx.send(embed=topEmbed)

    else:
      await ctx.trigger_typing()
      await ctx.send("That page doesn't exist")

  @commands.group(name="multipliers", invoke_without_command=True)
  async def multipliers(self, ctx):
    multiDB = db["xpMulti"]
    try:
      multipliersList = "\n".join(reversed([f"{discord.utils.get(ctx.guild.roles, id=int(k)).mention} | {v}x" for k, v in sorted(multiDB.items(), key=lambda item: item[1])]))

      if not multipliersList:
        multipliersList = "No multipliers set"

      multiEmbed = discord.Embed(
        title="XP Multipliers",
        description=multipliersList,
        color=defaultColor
      )

      multiEmbed.set_author(**embedAuthor)
      multiEmbed.timestamp = datetime.datetime.utcnow()
      multiEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

      await ctx.trigger_typing()
      await ctx.send(embed=multiEmbed)

    except:
      await ctx.trigger_typing()
      await ctx.send("I couldn't find any multipliers")

  @multipliers.command(name="set")
  @has_permissions(manage_channels=True)
  async def set_subcommand(self, ctx, role: discord.Role, multiplier):
    try:
      multiplier = float(multiplier)
      if multiplier < 0:
        await ctx.trigger_typing()
        await ctx.send("The multiplier can't be a negative number")

      elif multiplier == 1.0:
        del db["xpMulti"][str(role.id)]

      else:
        db["xpMulti"][str(role.id)] = str(multiplier)
      
      mulEmbed = discord.Embed(
        description=f"Set the multiplier for the role {role} to {multiplier}x",
        color=role.color
      )
       
      await ctx.trigger_typing()
      await ctx.send(embed=mulEmbed) 

    except ValueError:
      await ctx.trigger_typing()
      await ctx.send(f"**{multiplier}** isn't a valid multiplier")

  @commands.command()
  @is_owner()
  async def resetxp(self, ctx):
    await ctx.send("Are you sure? Type `confirmreset` to continue")

    try:
      msg = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=15.0)

      if msg.content == "confirmreset":
        await ctx.trigger_typing()
        await ctx.send("Confirmation correct, resetting xp...")
        del db["xp"]
        db["xp"] = {}

        await ctx.trigger_typing()
        await ctx.send("xp is reset")

      else:
        await ctx.trigger_typing()
        await ctx.send("Confirmation incorrect, xp reset canceled")

    except TimeoutError:
      await ctx.trigger_typing()
      await ctx.send(f"You ran out of time, xp reset canceled")

  @commands.group(name="sync", invoke_without_command=True)
  async def sync(self, ctx):
    await self.syncRoles(str(ctx.author.id))
    await ctx.trigger_typing()
    await ctx.send("Synced level roles")

  @sync.command(name="all")
  @has_permissions(manage_roles=True)
  async def all_subcommand(self, ctx):
    i = 0
    j = 0

    await ctx.trigger_typing()
    await ctx.send(f"Syncing level roles for **{len(ctx.guild.members)}** users...")

    for member in ctx.guild.members:
      sync = await self.syncRoles(str(member.id))
      if sync:
        i += 1
      
      else:
        j += 1

    await ctx.trigger_typing()
    await ctx.send(f"Synced level roles for **{i}** users (**{j}** already synced)")

  @commands.group(name="disabledchannels", invoke_without_command=True)
  async def disabledchannels(self, ctx):
    channelsList = "\n".join([f"**{i + 1}**. {get(ctx.guild.text_channels, id=channelID).mention}" for i, channelID in enumerate(db["xpDisabledChannels"])])

    channelsEmbed = discord.Embed(
      title="Disabled channels",
      description=channelsList,
      color=defaultColor
    )

    channelsEmbed.set_author(**embedAuthor)
    channelsEmbed.timestamp = datetime.datetime.utcnow()
    channelsEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing()
    await ctx.send(embed=channelsEmbed)

  @disabledchannels.command(name="add")
  @has_permissions(manage_channels=True)
  async def add_subcommand(self, ctx, channel: discord.TextChannel):
    if channel.id not in db["xpDisabledChannels"]:
      db["xpDisabledChannels"].append(channel.id)

      await ctx.trigger_typing()
      await ctx.send(f"Disabled XP in {channel.mention}")

    else:
      await ctx.trigger_typing()
      await ctx.send("XP in that channel is already disabled")

  @disabledchannels.command(name="remove", aliases=["delete"])
  @has_permissions(manage_channels=True)
  async def remove_subcommand(self, ctx, channel: discord.TextChannel):
    if channel.id in db["xpDisabledChannels"]:
      db["xpDisabledChannels"].remove(channel.id)

      await ctx.trigger_typing()
      await ctx.send(f"XP in {channel.mention} is now allowed")

    else:
      await ctx.trigger_typing()
      await ctx.send("XP in that channel is not disabled")

  @commands.command()
  @has_permissions(manage_channels=True)
  async def xprate(self, ctx, minRate, maxRate):
    try:
      minRate = int(minRate)
      maxRate = int(maxRate)
      if minRate <= maxRate:
        oldMin = db["xpRate"][0]
        oldMax = db["xpRate"][1]

        db["xpRate"] = [minRate, maxRate]

        rateEmbed = discord.Embed(
          description=f"Set the XP rate from **{oldMin}** - **{oldMax}** to **{minRate}** - **{maxRate}**",
          color=defaultColor
        )

        rateEmbed.timestamp = datetime.datetime.utcnow()
        rateEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

        await ctx.trigger_typing()
        await ctx.send(embed=rateEmbed)

      else:
        await ctx.trigger_typing()
        await ctx.send("The minimum xp can't be more than the max xp")

    except ValueError:
      await ctx.trigger_typing()
      await ctx.send("The values have to be numbers")

  @commands.Cog.listener()
  async def on_message(self, msg):
    if not isinstance(msg.channel, discord.channel.DMChannel):
      if msg.channel.id not in db["xpDisabledChannels"] and not msg.author.bot and self.toxicID not in [role.id for role in msg.author.roles]:
        user = str(msg.author.id)
        minVal = int(db["xpRate"][0])
        maxVal = int(db["xpRate"][1])
        xpAmount = random.randint(minVal, maxVal)
        multiplier = self.getMultiplier("val", msg.author)
        if multiplier is not None:
          xpAmount *= multiplier

        if user in db["xp"]:
          currentXp = db["xp"][user][0]
          cooldown = db["xp"][user][1]
          if cooldown == 0:
            self.addXP(user, int(xpAmount))
            db["xp"][user][1] = 60
            lvlUp = self.checkLevelUp(currentXp, currentXp + xpAmount)

          else:
            lvlUp = False

        else:
          self.addXP(user, xpAmount)
          lvlUp = self.checkLevelUp(0, xpAmount)

        if lvlUp:
          await self.syncRoles(user)
          await msg.channel.send(f"Holy Jäger! **{msg.author.display_name}** just leveled up!\nYou are now level **{lvlUp}**")

def setup(bot):
  bot.add_cog(xp(bot))