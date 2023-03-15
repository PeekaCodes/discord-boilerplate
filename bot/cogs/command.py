from discord.ext import commands
from discord import app_commands
import discord
import requests
from discord.app_commands import Choice
import datetime
import cogs.modules.config_json as cfg
from typing import Optional










class command_class(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Declare that this command is a hybrid command.
    @commands.hybrid_command(name="command_name", description="Command descriptions", aliases=["c"])
    # Can be role id or role name.
    @commands.has_any_role(*cfg.getAdminRoles())
    # Describe the command's parameter.
    @app_commands.describe(input="Input description.")
    # Sync command to a server. Remove this if you want to make it global.
    @app_commands.guilds(*cfg.getGuildId())
    async def command(self, ctx: commands.Context,input:str):
        await ctx.send("Message !")
        
        

    @command.error
    async def error(self, ctx, error: commands.CommandError):
        # Triggers when user omitted an argument.
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send('Missing argument. `?c <input>')
        # Triggers if user does not have the required role.
        if isinstance(error, commands.MissingAnyRole):
            await ctx.send("**Oh you don't have the right , oh you don't have the right.**")


async def setup(bot: commands.Bot):
    await bot.add_cog(command_class(bot))