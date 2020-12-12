import discord
from redbot.core import commands

class ChristmasCard(commands.Cog):
  """Send someone a christmas card!"""
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def card(self, ctx: commands.Context, user_id: int, *, message: str):
    """Send a christmas card to someone!"""
    destination = self.bot.get_user(user_id)
    if destination is None or destination.bot:
        await ctx.send("Invalid ID, user not found, or user is a bot.")
    description = ("Christmas Card from {}").format(ctx.author)
    content = ("Send christmas cards using {}card!").format(ctx.clean_prefix)
    #author = ctx.author.name
    e = discord.Embed(colour=discord.Colour.red(), description=message)
    e.set_footer(text=content)
    #e.set_author(author)
    try:
      await destination.send(embed=e)
    except discord.HTTPException:
      await ctx.send("Sorry, I couldn't send a card to {}").format(destination)
    else:
        await ctx.send("Message delivered to {}").format(destination)
    response = "{}\nMessage:\n\n{}".format(description, message)
    try:
        await destination.send("{}\n{}".format(box(response), content))
    except discord.HTTPException:
        await ctx.send("Sorry, I couldn't deliver your message to {}").format(destination)
    else:
        await ctx.send("Message delivered to {}").format(destination)
