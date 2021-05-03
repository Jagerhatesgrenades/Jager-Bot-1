import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_role, has_permissions
from functions import checkFor, updateDictDB, updateListDB, defaultColor, embedAuthor, staffID, sotwRoleID, formerSotwRoleID
from statistics import mode as mathMode
from replit import db
from collections import Counter
import datetime

class sotw(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def nominate(self, ctx, nominatedUser: discord.Member):
    nominatorUser = ctx.author
    isVoting = db["isVoting"]

    if not isVoting:
      if not await checkFor(nominatorUser.mention, "nominators"):
        await updateListDB("nominations", nominatedUser.mention)
        await updateListDB("nominators", nominatorUser.mention)
        await updateDictDB("nominationsPerUser", nominatorUser.mention, nominatedUser.mention)
        await ctx.trigger_typing()
        await ctx.send(f"**{nominatorUser.display_name}** nominated **{nominatedUser.display_name}**")
      
      else:
        await ctx.trigger_typing()
        await ctx.send("You already nominated someone!")

    else:
      await ctx.trigger_typing()
      await ctx.send("You can't nominate during the voting process!")

  @commands.command()
  async def vote(self, ctx, votedUser: discord.Member):
    voterUser = ctx.author
    isVoting = db["isVoting"]

    if isVoting:
      if not await checkFor(voterUser.mention, "voters"):
        if await checkFor(votedUser.mention, "nominations"):
          await updateListDB("votes", votedUser.mention)
          await updateListDB("voters", voterUser.mention)
          await updateDictDB("votesPerUser", voterUser.mention, votedUser.mention)
          await ctx.trigger_typing()
          await ctx.send(f"**{voterUser.display_name}** voted for **{votedUser.display_name}**")

        else:
          await ctx.trigger_typing()
          await ctx.send("You have to vote for a nominated user!")
      
      else:
        await ctx.trigger_typing()
        await ctx.send("You already voted for someone!")
      
    else:
      await ctx.trigger_typing()
      await ctx.send("You can't vote right now!")
  
  @commands.command()
  @has_role(staffID)
  async def startvote(self, ctx):
    isVoting = db["isVoting"]
    nominees = "\n".join(db["nominations"])

    if not isVoting:
      db["isVoting"] = True
      
      votingEmbed = discord.Embed(
        title="Vote for SOTW",
        description=f"""
          `j!vote <user>`

          {nominees}
        """,
        color=defaultColor
      )

      votingEmbed.set_author(**embedAuthor)
      votingEmbed.timestamp = datetime.datetime.utcnow()
      votingEmbed.set_footer(**embedAuthor, icon_url=ctx.author.avatar_url)
      
      await ctx.trigger_typing()
      await ctx.send(embed=votingEmbed)
      await ctx.trigger_typing()
      await ctx.send("<@820074719419695154>")

    else:
      await ctx.trigger_typing()
      await ctx.send("The voting process has already begun!")

  @commands.command()
  @has_role(staffID)
  async def finishvote(self, ctx):
    isVoting = db["isVoting"]

    if isVoting:
      db["isVoting"] = False

      votesList = []

      countDict = Counter(db["votes"])

      dupes = {}

      for i, (k, v) in enumerate(countDict):
        for x in countDict:
          if countDict.index(x) > i and v == countDict[x]:
            dupes[k] = v

      if dupes:
        db["dupes"] = dupes

        letterEmojis = ("🇦", "🇧", "🇨", "🇩", "🇪")

        letters = [
          ":regional_indicator_a:",
          ":regional_indicator_b:",
          ":regional_indicator_c:",
          ":regional_indicator_d:",
          ":regional_indicator_b:"
        ]


        dupeNames = ", ".join([k for k in dupes])
        
        poll = "\n".join([f"{letters[i]} {dupes[i]}" for i in range(0, len(dupes))])

        for k, v in dupes:
          voteAmount = v
          break

        sotwPollEmbed = discord.Embed(
          title="It's a tie!",
          description=f"""
            It's a tie between
            {dupeNames}

            They both got **{voteAmount}** Votes!

            Vote for the next SOTW in the poll below!

            {poll}

            Duplicate votes won't count!
          """,  
          color=defaultColor
        )

        sotwPollEmbed.set_author(**embedAuthor)
        sotwPollEmbed.timestamp = datetime.datetime.utcnow()

        await ctx.trigger_typing()
        pollMsg = await ctx.send(embed=sotwPollEmbed)

        for i in range(0, len(dupes)):
          await pollMsg.add_reaction(letterEmojis[i])
      
      else:
        newSOTW = mathMode(db["votes"])

        for item in countDict:
          votesList.append(f"{item}: **{countDict[item]}**")

        votesList = "\n".join(votesList)
      
        finishEmbed = discord.Embed(
          title="New SOTW",
          description=f"""
            Our new SOTW is **{newSOTW}**!

            Votes:
            {votesList}
            """,
          color=defaultColor
        )

        finishEmbed.set_author(**embedAuthor)
        finishEmbed.timestamp = datetime.datetime.utcnow()

        del db["nominations"]
        del db["nominators"]
        del db["votes"]
        del db["voters"]
        del db["nominationsPerUser"]
        del db["votesPerUser"]

        sotwRole = ctx.guild.get_role(sotwRoleID)
        formerSotwRole = ctx.guild.get_role(formerSotwRoleID)
    
        if sotwRole.members:
          for member in sotwRole.members:
            oldSOTW = member
            break
        
        oldSOTW.remove_roles(sotwRole)
        oldSOTW.add_roles(formerSotwRole)
      
        newSOTW = newSOTW[3:-1]
        newSOTW = self.get_member(int(newSOTW))

        newSOTW.add_roles(sotwRole)
      
        await ctx.trigger_typing()
        await ctx.send(embed=finishEmbed)
        await ctx.trigger_typing()
        await ctx.send("<@&820074719419695154>")

    else:
      await ctx.trigger_typing()
      await ctx.send("You can't finish voting if we aren't voting sussy baka!")

  @commands.command()
  @has_permissions(manage_channels=True)
  async def forcesotw(self, ctx, newSotw: discord.Member):
    oldSotwList = [member for member in ctx.guild.members if self.bot.get_role(771887695654944799) in member.roles]

    if len(oldSotwList) <= 1:
      if len(oldSotwList) == 1:
        oldSotw = oldSotwList[0]

        newSotw.add_roles(self.bot.get_role(771887695654944799))
        oldSotw.remove_roles(self.bot.get_role(771887695654944799))
        oldSotw.add_roles(self.bot.get_role(772257145018122293))

      del db["nominations"]
      del db["nominators"]
      del db["votes"]
      del db["voters"]
      del db["nominationsPerUser"]
      del db["votesPerUser"]

      if len(oldSotwList) == 1:
        await ctx.trigger_typing()
        await ctx.send(f"**{newSotw}** SOTW")

    else:
      await ctx.trigger_typing()
      await ctx.send("I found multiple people with SOTW. What the fuck")

  @commands.command()
  @has_permissions(manage_channels=True)
  async def resetsotw(self, ctx):
    await ctx.trigger_typing()
    await ctx.send("This will clear the SOTW database\nAre you sure? Send \"yes\" to continue")

    def check(author):
      return author == ctx.author

    while True:
      try:
        message = self.bot.wait_for("message", check=check, timeout=5)

        if message.content.lower() == "yes":
          del db["nominations"]
          del db["nominators"]
          del db["votes"]
          del db["voters"]
          del db["nominationsPerUser"]
          del db["votesPerUser"]

          await ctx.trigger_typing()
          await ctx.send("Cleared the SOTW database")

      except:
        await ctx.trigger_typing()
        await ctx.send("You took too long to respond")

def setup(bot):
 bot.add_cog(sotw(bot))