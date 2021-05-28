import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
from functions import defaultColor, embedAuthor, sotwRoleID, formerSotwRoleID, emojis, regionalIndicators, lockChannel, unlockChannel
from replit import db
from collections import Counter
import datetime

class sotw(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  def checkFor(self, value, key, keyVal):
    if key in db.keys():
      if keyVal == "key":
        if value in db[key].keys():
          return True

        else:
          return False

      elif keyVal == "val":
        if value in db[key].values():
          return True

        else:
          return False

    else:
      return False

  @commands.command()
  async def nominate(self, ctx, user: discord.Member):
    if not db["isVoting"]:
      if not self.checkFor(str(ctx.author.id), "nominations", "key"):
        if not user.bot:
          if formerSotwRoleID not in list([role.id for role in user.roles]):
            db["nominations"][str(ctx.author.id)] = str(user.id)

            nomEmbed = discord.Embed(
              description=f"{user.mention} has been nominated by {ctx.author.mention}",
              color=defaultColor
            )

            await ctx.trigger_typing()
            await ctx.send(embed=nomEmbed)

          else:
            await ctx.trigger_typing()
            await ctx.send("You can't nominate someone who has the former SOTW role")

        else:
          await ctx.trigger_typing()
          await ctx.send("You can't nominate a bot")

      else:
        await ctx.trigger_typing()
        await ctx.send("You already nominated someone")

    else:
      await ctx.trigger_typing()
      await ctx.send("You can't nominate while voting")

  @commands.command()
  async def vote(self, ctx, user: discord.Member):
    if db["isVoting"]:
      if not self.checkFor(str(ctx.author.id), "votes", "key"):
        if self.checkFor(str(user.id), "nominations", "val"):
          db["votes"][str(ctx.author.id)] = str(user.id)

          voteEmbed = discord.Embed(
            description=f"**{ctx.author.display_name}** has voted for **{user.display_name}**",
            color=defaultColor
          )

          await ctx.trigger_typing()
          await ctx.send(embed=voteEmbed)

        else:
          await ctx.trigger_typing()
          await ctx.send("You have for a nominated user")

      else:
        await ctx.trigger_typing()
        await ctx.send("You already voted for someone")

    else:
      await ctx.trigger_typing()
      await ctx.send("You can't vote while nominating")

  @commands.command()
  @has_permissions(manage_roles=True)
  async def startvote(self, ctx):
    if not db["isVoting"]:
      db["isVoting"] = True

      nominationIDs = []
      for userID in db["nominations"].values():
        if userID not in nominationIDs:
          nominationIDs.append(userID)

      nominations = "\n".join([f"**{i}.** {get(ctx.guild.members, id=int(user))}" for i, user in enumerate(nominationIDs)])

      startVoteEmbed = discord.Embed(
        title="Vote for SOTW",
        description=f"""
        Vote for the next SOTW with `j!vote <user>`

        Nominations
        {nominations}

        """,
        color=defaultColor
      )

      await ctx.trigger_typing()
      await ctx.send("<@&820074719419695154>")
      await ctx.send(embed=startVoteEmbed)

    else:
      await ctx.trigger_typing()
      await ctx.send("Voting has already started")

  @commands.command()
  @has_permissions(manage_roles=True)
  async def finishvote(self, ctx):
    if db["isVoting"]:
      votes = Counter(db["votes"].values())
      votes = dict(reversed(sorted(votes.items(), key=lambda kv: kv[1])))
      highestIDs = [userID for userID, count in votes.items() if count == max(votes.values())]
      if len(highestIDs) == 1:
        newSotw = get(ctx.guild.members, id=int(highestIDs[0]))
  
        finishEmbed = discord.Embed(
          title="New SOTW",
          description=f"The new SOTW is {newSotw.mention}!",
          color=defaultColor
        )
  
        sotwRole = get(ctx.guild.roles, id=sotwRoleID)
        formerSotwRole = get(ctx.guild.roles, id=formerSotwRoleID)
  
        oldSotw = sotwRole.members[0]
  
        await newSotw.add_roles(sotwRole)
        await oldSotw.add_roles(formerSotwRole)
        await oldSotw.remove_roles(sotwRole)
  
        db["isVoting"] = False
  
        db["nominations"] = {}
        db["votes"] = {}

        await ctx.trigger_typing()
        await ctx.send("<@&820074719419695154>")
        await ctx.send(embed=finishEmbed)

      else:
        poll = "\n".join([f"{regionalIndicators[i]} {get(ctx.guild.members, id=int(userID)).mention}" for i, userID in enumerate(highestIDs)])

        votePollEmbed = discord.Embed(
          title="SOTW Tie",
          description=poll,
          color=defaultColor
        )

        db["isVoting"] = False

        await lockChannel(ctx.guild, 771911980922961950)

        await ctx.trigger_typing()
        await ctx.send("<@&820074719419695154>")
        pollMsg = await ctx.send(embed=votePollEmbed)

        for i in range(0, len(highestIDs)):
          await pollMsg.add_reaction(emojis[i])

    else:
      await ctx.trigger_typing()
      await ctx.send("Voting hasn't started yet")

  @commands.command()
  @has_permissions(manage_channels=True)
  async def setSotw(self, ctx, newSotw: discord.Member):
    newSotwRoleIDs = [role.id for role in newSotw.roles]

    if formerSotwRoleID not in newSotwRoleIDs:
      sotwRole = get(ctx.guild.roles, id=sotwRoleID)
      formerSotwRole = get(ctx.guild.roles, id=formerSotwRoleID)

      oldSotw = sotwRole.members[0]

      newSotw.add_roles(sotwRole)
      oldSotw.add_roles(formerSotwRole)
      oldSotw.remove_roles(sotwRole)

      await unlockChannel(ctx.guild, 771911980922961950)

      await ctx.trigger_typing()
      await ctx.send(f"Set **{newSotw.display_name}** as SOTW and reset the system")

    else:
      await ctx.trigger_typing()
      await ctx.send("You can't give SOTW to a former SOTW")

  @commands.command()
  async def votes(self, ctx):
    votes = Counter(db["votes"].values())

    votes = sorted(votes.items(), key=lambda kv: kv[1])

    voteList = "\n".join([f"**{i + 1}**. {get(ctx.guild.members, id=int(userID)).mention} => **{count}** votes" for i, (userID, count) in enumerate(reversed(votes))])

    votesEmbed = discord.Embed(
      title="Votes",
      description=voteList,
      color=defaultColor
    )

    votesEmbed.set_author(**embedAuthor)
    votesEmbed.timestamp = datetime.datetime.utcnow()
    votesEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing()
    await ctx.send(embed=votesEmbed)

  @commands.command()
  async def nominations(self, ctx):
    nominations = []
    for name in db["nominations"].values():
      if name not in nominations:
        nominations.append(name)

    nominations.sort()

    nominationsList = "\n".join([f"**{i + 1}**. {get(ctx.guild.members, id=int(userID)).mention}" for i, userID in enumerate(reversed(nominations))])

    nominationsEmbed = discord.Embed(
      title="Nominations",
      description=nominationsList,
      color=defaultColor
    )

    nominationsEmbed.set_author(**embedAuthor)
    nominationsEmbed.timestamp = datetime.datetime.utcnow()
    nominationsEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing()
    await ctx.send(embed=nominationsEmbed)

  @commands.command()
  @has_permissions(manage_channels=True)
  async def resetsotw(self, ctx):
    await ctx.trigger_typing()
    await ctx.send("Resetting sotw...")

    db["isVoting"] = False
  
    db["nominations"] = {}
    db["votes"] = {}

    await ctx.trigger_typing()
    await ctx.send("Reset the system")

def setup(bot):
 bot.add_cog(sotw(bot))