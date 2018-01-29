import asyncio
import datetime
import random

import aiohttp
import discord
from discord.ext import commands
from io import BytesIO

from PIL import Image, ImageFilter, ImageSequence

class Gala:
    """Help yourself"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def iq(self, ctx, member: discord.Member = None):
        if member is None:
            return await ctx.send('A targeted user is required')
        iq = random.randrange(1, 1000)
        # like if its 1-300 would be green, 300-600 would be orange, 600-900 would be red and 900-1000 purple? if not just make it always red :p
        if iq <= 300:
            color = discord.Color.green()
        elif iq <= 600:
            color = discord.Color.orange()
        elif iq <= 900:
            color = discord.Color.red()
        else:
            color = discord.Color.purple()
        lastmsg = await ctx.history().get(author__id=member.id)
        embed = discord.Embed(color=color, description=f'{member.mention}\n\n"{lastmsg.clean_content}"\n\n{iq} IQ')
        embed.set_author(name='❗ IQ Analyzer ❗', icon_url=member.avatar_url_as(size=32))
        embed.set_footer(text=f'🔮 {lastmsg.created_at.strftime("%d/%m/%Y")}, #{ctx.channel.name} 🔮')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Gala(bot))
