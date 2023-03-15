import discord


from discord.ext import commands
import glob
import configLoader
from cogs.modules.config_json import *

from typing import Optional
TOKEN = configLoader.getToken()
MY_GUILD = discord.Object(id=getGuildId())





ignoredCogs = ['ignored modules']
ignoredCogs = [f'{cog}.py' for cog in ignoredCogs]





class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="$",
            intents=discord.Intents.all(),
            application_id=1067119740201480315,
            strip_after_prefix=True,
        )

    async def setup_hook(self) -> None:
        print(f"{self.user} has connected to Discord!")
        
        
        await self.load_extension("jishaku")
        

        # Load extensions that are inside your Cogs folder.
        for cog in glob.glob("cogs/**/*.py", recursive=True):
            if(cog in ignoredCogs):continue
            await self.load_extension(
                cog.replace("\\", ".").replace("/", ".").removesuffix(".py")
            )
            print(f"{cog[5:]} Has Succesfully Loaded!")

    # Close bot and connections.
    async def close(self) -> None:
        await super().close()
        

if __name__ == "__main__":
    bot = MyBot()
    bot.run(TOKEN, reconnect=True)



