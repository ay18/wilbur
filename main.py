import os

from discord.ext import commands


def _get_prefix(bot, message):
    return commands.when_mentioned_or('b!')(bot, message)


class Blitz(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        self.remove_command("help")
        self._load_extensions()

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_disconnect(self):
        print('Signing off as', self.user)

    def _load_extensions(self):
        for file in os.listdir("cogs/"):
            try:
                if file.endswith(".py"):
                    self.load_extension(f'cogs.{file[:-3]}')
            except Exception as e:
                print(e)


if __name__ == "__main__":
    token = 'NTUyMDI2NzYxOTQxMjIxMzg2.XpqOvg.ppCGDWr5DHNKA42FL5WR1ZEu1lw'
    blitz = Blitz(_get_prefix)
    blitz.run(token)
