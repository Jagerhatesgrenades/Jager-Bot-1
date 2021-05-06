import discord
from discord.ext import commands
from functions import embedAuthor, defaultColor, staffRolesDict
import datetime

class info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def roleinfo(self, ctx, role: discord.Role):
    roleEmbed = discord.Embed(
      title=role.name,
      description=f"`{role.id}`",
      color=role.color
    )

    roleInfo = {
      "Color": f"`{role.color}`",
      "Shown in member list": f"`{role.hoist}`",
      "Integration": f"`{role.managed}`",
      "Bot role": f"`{role.is_bot_managed()}`",
      "Booster Role": f"`{role.is_premium_subscriber()}`",
      "Permissions": f"`{role.permissions.value}`",
      "Amount of members with this role": f"`{len(role.members)}`"
    }

    for name, val in roleInfo.items():
      roleEmbed.add_field(
        name=name,
        value=val,
        inline=True
      )

    roleEmbed.set_author(**embedAuthor)
    roleEmbed.timestamp = datetime.datetime.utcnow()
    roleEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing()
    await ctx.send(embed=roleEmbed)

  @commands.command()
  async def userinfo(self, ctx, user: discord.Member):
    boosterRoles = {1: 773375163303591948, 2: 833328572600942689}

    userColor = [role.color for role in reversed(user.roles) if str(role.color) != "#000000"][0]

    userStaff = False
    userBooster = False

    userStaffRole = None
    userBoosterRole = None

    for role in user.roles:
      for name, roleId in staffRolesDict.items():
        if role.id == roleId:
          userStaffRole = discord.utils.get(ctx.guild.roles, id=roleId).mention
          userStaff = True

    for role in user.roles:
      for name, roleId in boosterRoles.items():
        if role.id == roleId:
          userBoosterRole = discord.utils.get(ctx.guild.roles, id=roleId).mention
          userBooster = True

    userEmbed = discord.Embed(
      title=user,
      description=f"`{user.id}`",
      color=userColor
    )

    userInfo = {
      "Nickname": f"`{user.display_name}`",
      "Color": f"`{userColor}`",
      "Staff": f"`{userStaff}`",
      "Staff role": userStaffRole,
      "Bot": f"`{user.bot}`",
      "Booster": f"`{userBooster}`",
      "Booster role": userBoosterRole,
      "Account creation date": user.created_at,
      "Join date": user.joined_at
    }

    inlines = {
      "Nickname": True,
      "Color": False,
      "Staff": True,
      "Staff role": True,
      "Bot": False,
      "Booster": True,
      "Booster role": True,
      "Account creation date": False,
      "Join date": False
    }

    for name, val in userInfo.items():
      userEmbed.add_field(
        name=name,
        value=val,
        inline=inlines[name]
      )

    userEmbed.set_thumbnail(url=user.avatar_url)
    userEmbed.set_author(**embedAuthor)
    userEmbed.timestamp = datetime.datetime.utcnow()
    userEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing()
    await ctx.send(embed=userEmbed)

  @commands.command()
  async def serverinfo(self, ctx):
    server = ctx.guild
    staffRoles = [
      810585594638893096,
      769577839313551360,
      810586176515080223,
      769579500752863243
      ]
    
    coOwnerRoleID = 834184731193114714

    serverAdmins = []
    serverMods = []

    for member in server.members:
      for role in member.roles:
        if role.id in staffRoles:
          if staffRoles.index(role.id) in [0, 1]:
            serverAdmins.append(member.mention)

          elif staffRoles.index(role.id) in [2, 3]:
            serverMods.append(member.mention)

    serverAdmins = "\n".join(serverAdmins)
    serverMods = "\n".join(serverMods)

    i = 0

    for member in server.members:
      if member.bot:
        i += 1

    for member in server.members:
      for role in member.roles:
        if role.id == coOwnerRoleID:
          serverCoOwner = member.mention

    serverEmbed = discord.Embed(
      title=server,
      description=f"`{server.id}`",
      color=defaultColor
    )

    serverInfo = {
      "Members": f"`{len(server.members)}`",
      "Roles": f"`{len(server.roles)}`",
      "Text Channels": f"`{len(server.text_channels)}`",
      "Voice channels": f"`{len(server.voice_channels)}`",
      "Bots": f"`{i}`",
      "Owner": server.owner.mention,
      "Co-Owner": serverCoOwner,
      "Admins": serverAdmins,
      "Mods": serverMods,
      "Boosters": '\n'.join([user.mention for user in server.premium_subscribers])
    }

    inlines = {
      "Members": False,
      "Roles": False,
      "Text Channels": True,
      "Voice channels": True,
      "Bots": False,
      "Owner": True,
      "Co-Owner": True,
      "Admins": False,
      "Mods": False,
      "Boosters": False
    }

    for name, val in serverInfo.items():
      serverEmbed.add_field(
        name=name,
        value=val,
        inline=inlines[name]
      )

    serverEmbed.set_thumbnail(url=server.icon_url)
    serverEmbed.set_author(**embedAuthor)
    serverEmbed.timestamp = datetime.datetime.utcnow()
    serverEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing()
    await ctx.send(embed=serverEmbed)


def setup(bot):
  bot.add_cog(info(bot))