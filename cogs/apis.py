import discord
from discord.ext import commands
import json
import requests
import random
from functions import regionalIndicators, emojis, embedAuthor
import datetime
import html

class apis(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def trivia(self, ctx):
    URL = requests.get("https://opentdb.com/api.php?amount=1")
    questionDict = json.loads(URL.text)
    questionDict = questionDict["results"][0]

    category = html.unescape(questionDict["category"])
    difficulty = html.unescape(questionDict["difficulty"])
    question = html.unescape(questionDict["question"])
    correctAnswer = html.unescape(questionDict["correct_answer"])
    incorrectAnswers = questionDict["incorrect_answers"]

    incorrectAnswers = [html.unescape(answer) for answer in incorrectAnswers]

    allAnswers = [answer for answer in incorrectAnswers]
    allAnswers.append(correctAnswer)

    random.shuffle(allAnswers)

    answerList = "\n".join([f"{regionalIndicators[i]} {allAnswers[i]}" for i in range(0, len(allAnswers))])

    answerDict = {}

    for i, answer in answerList:
      answerDict[emojis[i]] = answer

    triviaEmbed = discord.Embed(
      title=question,
      description=f"""
        Category: **{category}**
        Difficulty: **{difficulty}**

        {answerList}

        React to this message to answer
      """,
    )

    triviaEmbed.set_author(**embedAuthor)
    triviaEmbed.timestamp = datetime.datetime.utcnow()
    triviaEmbed.set_footer(text=ctx.author, icon_url=ctx.author.avatar_url)

    await ctx.trigger_typing
    triviaPoll = await ctx.send(embed=triviaEmbed)

    for i in range(0, len(allAnswers)):
      await triviaPoll.add_reaction(emojis[i])

    def triviaCheck(reaction, user):
      return user == ctx.author

    while True:
      try:
        reaction, user = await self.bot.wait_for('reaction_add', timeout= 15.0, check=triviaCheck)

        if reaction in answerDict:
          userAnswer = answerDict[reaction]
          if userAnswer == correctAnswer:
            await ctx.trigger_typing
            await ctx.send(f"{ctx.author.mention}, Correct!")
            break

          else:
            await ctx.trigger_typing
            await ctx.send(f"{ctx.author.mention}, That isn't correct!\nThe correct answer was **{correctAnswer}**")
            break

      except:
        await ctx.trigger_typing
        await ctx.send(f"{ctx.author.mention}, You took too long!\nThe answer was **{correctAnswer}**")
        break

  @commands.command()
  async def test(self, ctx):
    await ctx.trigger_typing
    await ctx.send("test")


def setup(bot):
  bot.add_cog(apis(bot))