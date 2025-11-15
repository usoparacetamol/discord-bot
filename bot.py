import discord
from discord import app_commands

class MeuPrimeiroBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O Bot {self.user} foi ligado com sucesso.")


bot = MeuPrimeiroBot()

# ===========================
# Comando /olá-mundo
# ===========================
@bot.tree.command(
    name="olá-mundo",
    description="Primeiro comando do bot."
)
async def ola_mundo(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Olá {interaction.user.mention}!"
    )


# ===========================
# Comando /soma
# ===========================
@bot.tree.command(
    name="soma",
    description="Soma dois números distintos."
)
@app_commands.describe(
    numero1="Primeiro número a somar",
    numero2="Segundo número a somar"
)
async def soma(interaction: discord.Interaction, numero1: int, numero2: int):
    resultado = numero1 + numero2
    await interaction.response.send_message(
        f"O número somado é {resultado}.",
        ephemeral=True
    )


# ===========================
# Comando /embed
# ===========================
@bot.tree.command(
    name="embed",
    description="Exibe um embed de exemplo."
)
async def embed_cmd(interaction: discord.Interaction):

    embed = discord.Embed(
        title="Meu Primeiro Embed",
        description="Isso aqui é um embed enviado pelo mesmo bot.",
        color=discord.Color.blurple()
    )

    embed.add_field(name="Campo 1", value="Valor do campo 1", inline=False)
    embed.add_field(name="Campo 2", value="Valor do campo 2", inline=True)
    embed.set_footer(text="Enviado com sucesso.")

    await interaction.response.send_message(embed=embed)


token = "SEU_TOKEN"