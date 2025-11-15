import discord
from discord import app_commands

class MeuPrimeiroBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="b!",
            intents=intents
        )
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O Bot {self.user} foi ligado com sucesso.")

bot = MeuPrimeiroBot()

@bot.tree.command(name="olá-mundo",description="Primeiro comando do Bot")
async def olamundo(interaction:discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}!")

@bot.tree.command(name="soma",description="Some dois números distintos")
@app_commands.describe(
    numero1="Primeiro numero a somar",
    numero2="Segundo número a somar"
)
async def olamundo(interaction:discord.Interaction,numero1:int,numero2:int):
    numero_somado = numero1 + numero2
    await interaction.response.send_message(f"O numero somado é {numero_somado}.",ephemeral=True)

bot.run("SEU_TOKEN")


        