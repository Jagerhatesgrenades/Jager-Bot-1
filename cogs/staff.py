import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions, is_owner, has_role
from functions import staffRoles, staffRolesDict, staffID, defaultColor
from actLogging import logPromotion, logDemotion
from replit import db

class staff(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.loggingChannel = self.bot.get_channel(838724538220937307)

  @commands.command()
  @has_permissions(manage_roles=True)
  async def role(self, ctx, action, role: discord.Role, user: discord.Member):
    if action in ["give", "add", "grant"]:
      if role < ctx.author.top_role or ctx.author == ctx.guild.owner:
        await user.add_roles(role)
        await ctx.trigger_typing()
        await ctx.send(f"Gave the role **{role.name}** to **{user.display_name}**")
        
      else:
        await ctx.trigger_typing()
        await ctx.send("You don't have the permission to do this!")

    elif action in ["remove", "take"]:
      if role < ctx.author.top_role or ctx.author == ctx.guild.owner:
        await user.remove_roles(role)
        await ctx.trigger_typing()
        await ctx.send(f"Took the role **{role.name}** from **{user.display_name}**")

      else:
        await ctx.trigger_typing()
        await ctx.send("You don't have the permission to do this!!")

  @commands.command()
  @has_permissions(manage_roles=True)
  async def rolecolor(self, ctx, role: discord.Role, color: discord.Color):
    if role < ctx.author.top_role or ctx.author == ctx.guild.owner:
      await role.edit(color=color)
      await ctx.trigger_typing()
      await ctx.send(f"Set the color of the role **{role.name}** to **{color}**")

    else:
      await ctx.trigger_typing()
      await ctx.send("You don't have the permission to do this!")

  @commands.command()
  @has_permissions(manage_roles=True)
  async def rolename(self, ctx, role: discord.Role, name: str):
    if role < ctx.author.top_role or ctx.author == ctx.guild.owner:
      await role.edit(name=name)
      await ctx.trigger_typing()
      await ctx.send(f"Set the name of the role **{role.name}** to **{name}**")

    else:
      await ctx.trigger_typing()
      await ctx.send("You don't have the permission to do this!")

  @commands.group(name="keys", invoke_without_command=True)
  @is_owner()
  async def keys(self, ctx, key=None):
    if key is None:
      keys = "\n".join(key for key in db.keys())
    
    else:
      keys = db[key]
      
    keysEmbed = discord.Embed(
      description=keys,
      color=defaultColor
    )

    await ctx.trigger_typing()
    await ctx.send(embed=keysEmbed)

  @keys.command(name="delete")
  @is_owner()
  async def delete_subcommand(self, ctx, key):
    if key in db.keys():
      del db[key]

      await ctx.trigger_typing()
      await ctx.send(f"Deleted the key **{key}**")

    else:
      await ctx.trigger_typing()
      await ctx.send(f"I couldn't find the key **{key}**")

  @commands.command()
  @has_permissions(manage_messages=True)
  async def lock(self, ctx):
    perms = ctx.channel.overwrites_for(ctx.guild.default_role)
    print(perms.send_messages)
    if perms.send_messages in [None, True]:
      perms.send_messages = False
      await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms, reason=f"{ctx.author} Locked the channel")

      await ctx.trigger_typing()
      await ctx.send(f"Locked {ctx.channel.mention}")

    else:
      await ctx.trigger_typing()
      await ctx.send("Channel is already locked")

  @commands.command()
  @has_permissions(manage_messages=True)
  async def unlock(self, ctx):
    perms = ctx.channel.overwrites_for(ctx.guild.default_role)
    if not perms.send_messages:
      perms.send_messages = None
      await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=perms, reason=f"{ctx.author} unlocked the channel")

      await ctx.trigger_typing()
      await ctx.send(f"Unlocked {ctx.channel.mention}")

    else:
      await ctx.trigger_typing()
      await ctx.send("Channel is already unlocked")

  @commands.command()
  @has_permissions(manage_roles=True)
  async def promote(self, ctx, user: discord.Member):
    if ctx.author.id != user.id:
      authorHighestRole = [role for role in reversed(ctx.author.roles) if role.id in staffRoles][0]
      userHighestRole = [role for role in reversed(user.roles) if role.id in staffRoles][0]
      if authorHighestRole > userHighestRole:
        staffRole = get(ctx.guild.roles, id=staffID)

        userRoleIDs = [role.id for role in user.roles]

        oldRole = userHighestRole

        if staffID not in userRoleIDs:
          await user.add_roles(staffRole)
          promotionRole = get(ctx.guild.roles, id=staffRoles[len(staffRoles) - 1])

        else:
          promotionRole = get(ctx.guild.roles, id=staffRoles[staffRoles.index(oldRole.id) - 1])

        await user.add_roles(promotionRole)
        await user.remove_roles(oldRole)

        promotionEmbed = discord.Embed(
          description=f"{ctx.author.mention} promoted {user.mention} from {oldRole.mention} to {promotionRole.mention}!",
          color=promotionRole.color
        )

        await ctx.trigger_typing()
        await ctx.send(embed=promotionEmbed)

      else:
        await ctx.trigger_typing()
        await ctx.send("You can't promote someone to a higher rank than yourself")

    else:
      await ctx.trigger_typing()
      await ctx.send("You can't promote yourself")

  @commands.command()
  @has_permissions(manage_roles=True)
  async def demote(self, ctx, user: discord.Member):
    if ctx.author.id != user.id:
      userRoleIDs = [role.id for role in user.roles]
      if staffID in userRoleIDs:
        authorHighestRole = [role for role in reversed(ctx.author.roles) if role.id in staffRoles][0]
        userHighestRole = [role for role in reversed(user.roles) if role.id in staffRoles][0]
        if authorHighestRole > userHighestRole:
          staffRole = get(ctx.guild.roles, id=staffID)   

          oldRole = userHighestRole

          if staffRoles.index(userHighestRole.id) == len(staffRoles) - 1:         
            demotionRole = None
            await user.remove_roles(staffRole)

          else:
            demotionRole = get(ctx.guild.roles, id=staffRoles[staffRoles.index(oldRole.id) + 1])
            await user.add_roles(demotionRole)

          await user.remove_roles(oldRole)

          promotionEmbed = discord.Embed(
            description=f"{ctx.author.mention} demoted {user.mention} from {oldRole.mention} to {demotionRole.mention if demotionRole else 'member'}!",
            color=demotionRole.color
          )

          await ctx.trigger_typing()
          await ctx.send(embed=promotionEmbed)

        else:
          await ctx.trigger_typing()
          await ctx.send("You can't demote someone who is the same rank or higher than you")

      else:
        await ctx.trigger_typing()
        await ctx.send("You can't demote someone who isn't staff")

    else:
      await ctx.trigger_typing()
      await ctx.send("You can't demote yourself")

  @commands.command()
  @has_permissions(manage_messages=True)
  async def sendmessage(self, ctx, channel: discord.TextChannel, *message):
    message = " ".join(message)
    await channel.trigger_typing()
    await channel.send(message)
    await ctx.message.delete()

def setup(bot):
  bot.add_cog(staff(bot))