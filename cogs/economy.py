import discord
from discord.ext import commands

from database import get_user, add_balance


class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def balance(self, ctx, member: discord.Member = None):
        """Check your or another user's balance."""

        member = member or ctx.author

        balance, bank = get_user(member.id)

        embed = discord.Embed(
            title=f"{member.display_name}'s Balance",
            description=(
                f"💰 Wallet: **${balance:,}**\n"
                f"🏦 Bank: **${bank:,}**"
            ),
            color=discord.Color.green()
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def daily(self, ctx):
        """Claim your daily reward."""

        reward = 1000

        add_balance(ctx.author.id, reward)

        await ctx.send(
            f"🎁 {ctx.author.mention}, you received **${reward:,}**!"
        )

    @commands.command()
    async def work(self, ctx):
        """Work to earn money."""

        reward = 500

        add_balance(ctx.author.id, reward)

        await ctx.send(
            f"💼 {ctx.author.mention}, you earned **${reward:,}**!"
        )


async def setup(bot):
    await bot.add_cog(Economy(bot))
