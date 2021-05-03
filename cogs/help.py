import discord
from discord.ext import commands
import datetime
from functions import embedAuthor, defaultColor

class help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def help(self, ctx, cat=None):
    if not cat:
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          `help` | Default help menu
          ┡`sotw` | SOTW commands
          ┡`fun` | Misc commands
          ┡`siege` | Siege commands
          ┡`info` | Info commands
          ┡`tags` | Tag commands
          ┡`rules` | Rule commands
          ┖`staff` | Staff only commands
        """,
        color=defaultColor
      )
      
    elif cat == "sotw":
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          `nominate <user>` | Nominate someone for SOTW
          `vote <user>` | Vote for someone
          `nominations` | See all the nominated users
          `votes` | See all the votes per user
        """,
        color=defaultColor
      )

    elif cat == "fun":
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          `sus <user>` | Calculate someone's sussiness!!
          `sexy <user>` | Sexy meter
          `shoot <user>` | Shoot someone
        """,
        color=defaultColor
      )

    elif cat == "siege":
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          `profile <operator>` | Get the profile of an operator
          ┖`profile random` | Get a random operator
          `siegememe` | Get a siege related meme
          `quote` | Get a random operator quote
        """,
        color=defaultColor
      )

    elif cat == "info":
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          `userinfo <user>` | Get info about a user
          `roleinfo <role>` | Get info about a role
          `serverinfo` | Get info about the server
          `color <format> <color code>` | Get info about a color
          ┡`color random` | Get a random color
          ┡`color hex DC696B` | Get color info via the HEX format
          ┡`color rgb 220,105,107` | Get color info via the RGB format
          ┡`color hsl 359,62,64` | Get color info via the HSL format
          ┡`color hsv 359,52,86` | Get color info via the HSV format
          ┖`color cmyk 0,52,51,14` | Get color info via the CMYK format

        """,
        color=defaultColor
      )

    elif cat == "staff":
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          These commands are staff only

          `startvote` | Start the voting process
          `finishvote` | Finish the voting process
          `role <action> <role> <user>` | Give or remove a role to or from a user
          ┡`role give <role> <user>` | Give a role to user (Aliases: `add` `grant` )
          ┖`role remove <role> <user>` | Remove a role from a user (Aliases: `take`)
          `rolecolor <role> <color>` | Change the color of a role
          `rolename <role> <name>` | Change the name of a role
        """,
        color=defaultColor
      )
    
    elif cat == "rules":
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          `rules [action] *args` | Server rules
          ┡`rules add <text>` | Add a rule
          ┡`rules delete <rule>` | Remove a rule
          ┡`rules edit <rule> <text>` | Edit a rule
          ┖`rules update <rules msg id>` | Update the rules embed in the rules channel
        """,
        color=defaultColor
      )

    elif cat == "tags":
      helpEmbed = discord.Embed(
        title="Help Menu",
        description="""
          Prefix = `j!`

          `tags [action] *args` | List of all the tags
          ┡`tags add <tag name> <tag reply>` | Add a tag
          ┡`tags delete <tag name>` | Remove a tag
          ┖`tags edit <tag name> <new tag reply>` | Edit a tag
        """,
        color=defaultColor
      )

    helpEmbed.set_author(**embedAuthor)
    helpEmbed.timestamp = datetime.datetime.utcnow()
    helpEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)
    
    await ctx.trigger_typing()
    await ctx.send(embed=helpEmbed)

def setup(bot):
  bot.add_cog(help(bot))