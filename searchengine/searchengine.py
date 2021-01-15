from redbot.core import commands
from datetime import datetime
import discord

from redbot.core import commands
from redbot.core.i18n import Translator, cog_i18n

_ = Translator("SearchEngine", __file__)

@cog_i18n(_)
class SearchEngine(commands.Cog):
  """Search multiple websites for queries."""
  
  def __init__(self, bot):
    self.bot = bot

  async def red_delete_data_for_user(self, **kwargs):
      """
      Nothing to delete
      """
      return
    
  @commands.command()
  async def google(self, ctx, *, search_query):
    """Search google."""
    querytemplate = f"https://www.google.co.uk/search?source=hp&ei=z07WX6SiGrXVgwfdpa3wAQ&q={search_query.capitalize()}"
    querytemplate = querytemplate.replace(' ', '%20')
    e = discord.Embed(description=(
      f"[Click here for search results]({querytemplate})"
    ), colour=discord.Colour.red(), timestamp=ctx.message.created_at)
    e.add_field(name="Engine", value="Google", inline=True)
    e.add_field(name="Author", value=ctx.author.name, inline=True)
    e.add_field(name="Search Query", value=search_query, inline=False)
    await ctx.send(embed=e)

  @commands.command()
  async def pinterest(self, ctx, *, search_query):
    """Search pinterest."""
    querytemplate = f"https://www.pinterest.co.uk/search/pins/?q={search_query.capitalize()}"
    querytemplate = querytemplate.replace(' ', '%20')
    e = discord.Embed(description=(
      f"[Click here for search results]({querytemplate})"
    ), colour=discord.Colour.red(), timestamp=ctx.message.created_at)
    e.add_field(name="Engine", value="Pinterest", inline=True)
    e.add_field(name="Author", value=ctx.author.name, inline=True)
    e.add_field(name="Search Query", value=search_query, inline=False)
    await ctx.send(embed=e)

  @commands.command()
  async def redbubble(self, ctx, *, search_query):
    """Search redbubble."""
    querytemplate = f"https://www.redbubble.com/shop/?query={search_query.capitalize()}"
    querytemplate = querytemplate.replace(' ', '%20')
    e = discord.Embed(description=(
      f"[Click here for search results]({querytemplate})"
    ), colour=discord.Colour.red(), timestamp=ctx.message.created_at)
    e.add_field(name="Engine", value="RedBubble", inline=True)
    e.add_field(name="Author", value=ctx.author.name, inline=True)
    e.add_field(name="Search Query", value=search_query, inline=False)
    await ctx.send(embed=e)


