import discord
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions
import random
from replit import db

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@', '#', '$', '%', '^', '&', '(', ')']

class randomxp(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.xpEvent.start()

  @tasks.loop(minutes=60.0)
  async def xpEvent(self):
    genChannel = self.bot.get_channel(819746637894778930)
    randomN = random.randint(0, 3)

    if randomN == 0:
      xpAmount = random.randint(1000, 15000)

      code = []

      for i in range(0, 10):
        randomN = random.randint(0, len(chars) - 1)
        code.append(chars[randomN])

      code = "".join(code)

      await genChannel.trigger_typing()
      await genChannel.send(f"**XP EVENT**\nThe first person to send **{code}** gets {xpAmount} XP!")

      def check(msg):
        return msg.channel == genChannel and msg.content == code

      msg = await self.bot.wait_for("message", check=check, timeout=60.0)

      winner = msg.author

      if str(winner.id) in db["xp"]:
        currentXP = db["xp"][str(winner.id)][0]
        
        currentXP += xpAmount

        db["xp"][str(winner.id)][0] = currentXP

      else:
        db["xp"][str(winner.id)] = [xpAmount, 0]

      await genChannel.trigger_typing()
      await genChannel.send(f"Congrats {winner.mention}! You have won {xpAmount} XP!")

  @commands.command()
  @has_permissions(manage_channels=True)
  async def testxp(self, ctx):
    logChannel = self.bot.get_channel(837701500779888670)

    xpAmount = random.randint(1000, 15000)

    code = []

    for i in range(0, 10):
      randomN = random.randint(0, len(chars))
      code.append(chars[randomN])

    code = "".join(code)

    await ctx.send(f"""
    **XP EVENT**
    The first person to send **{code}** gets {xpAmount} XP!
    """)

    def check(msg):
      return msg.content == code

    msg = await self.bot.wait_for("message", check=check)

    winner = msg.author

    await logChannel.send(f"{winner} | `{winner.id}` has earned {xpAmount} XP (This is a test by {ctx.author})")
    await ctx.send(f"Congrats {winner.mention}! You have won {xpAmount} XP!")

def setup(bot):
  bot.add_cog(randomxp(bot))