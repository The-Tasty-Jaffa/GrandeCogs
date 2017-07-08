from discord.ext import commands
import random
import discord

class Kiss:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def kiss(self, context, member: discord.Member):
        """Kiss your senpai/waifu!"""
        author = context.message.author.mention
        mention = member.mention
        
        kiss = "**{0} gave {1} a kiss!**"
        
        choices = ['http://i.imgur.com/0D0Mijk.gif', 'http://i.imgur.com/TNhivqs.gif', 'http://i.imgur.com/3wv088f.gif', 'http://i.imgur.com/7mkRzr1.gif', 'http://i.imgur.com/8fEyFHe.gif']
        
        image = random.choice(choices)
        
        embed = discord.Embed(description=kiss.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await self.bot.say(embed=embed)

def setup(bot):
    n = Kiss(bot)
    bot.add_cog(n)
