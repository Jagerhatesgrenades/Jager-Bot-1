import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from functions import staffRoles, staffRolesDict, staffID
from actLogging import logPromotion, logDemotion

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

def setup(bot):
  bot.add_cog(staff(bot))