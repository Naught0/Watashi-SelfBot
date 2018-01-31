import discord
from asyncurban import urbandictionary
from discord.ext import commands


class UrbanDictionary:
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.user_color
        self.ud_client = urbandictionary.UrbanDictionary(session=bot.aiohttp_session)

    @commands.group(invoke_without_command=True, aliases=['ud', 'urbandict'])
    async def urban(self, ctx, *, query: str):
        """ Check UrbanDictionary for the meaning of a word """
        word = await self.ud_client.get_word(query)
        em = discord.Embed(color=self.color)
        em.set_author(name="\U0001f4d6 Urban Dictionary")
        em.add_field(name="Word", value=word.word, inline=False)
        em.add_field(name="Definition", value=word.definition, inline=False)
        em.add_field(name="Example(s)", value=word.example, inline=False)
        await ctx.message.edit(embed=em, content=None)

    @urban.command(aliases=['-r'])
    async def random(self, ctx):
        """ Get a Random Word and its Meaning from UrbanDictionary """
        word = await self.ud_client.get_random()
        em = discord.Embed(color=self.color)
        em.set_author(name="\U0001f4d6 Urban Dictionary")
        em.add_field(name="Word", value=word.word)
        em.add_field(name="Definition", value=word.definition)
        em.add_field(name="Example(s)", value=word.example)
        await ctx.message.edit(embed=em, content=None)


def setup(bot):
    bot.add_cog(UrbanDictionary(bot))
