import discord
from discord import app_commands

from dotenv import load_dotenv
import os

load_dotenv()
discord_token = os.getenv("discord_token")

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

# Comando /olá-mundo
@bot.tree.command(
    name="olá-mundo",
    description="Primeiro comando do bot."
)
async def ola_mundo(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Olá {interaction.user.mention}!"
    )
    
# Comando /calc
@bot.tree.command(
    name="calc",
    description="Faz cálculos com duas entradas."
)
@app_commands.describe(
    operacao="Escolha a operação que deseja fazer",
    numero1="Primeiro número",
    numero2="Segundo número"
)
@app_commands.choices(
    operacao=[
        app_commands.Choice(name="adição", value="add"),
        app_commands.Choice(name="subtração", value="sub"),
        app_commands.Choice(name="multiplicação", value="mul"),
        app_commands.Choice(name="divisão", value="div")
    ]
)
async def calc(interaction: discord.Interaction, operacao: app_commands.Choice[str], numero1: float, numero2: float):

    if operacao.value == "add":
        resultado = numero1 + numero2

    elif operacao.value == "sub":
        resultado = numero1 - numero2

    elif operacao.value == "mul":
        resultado = numero1 * numero2

    elif operacao.value == "div":
        if numero2 == 0:
            await interaction.response.send_message(
                "Não tem como dividir por zero, né…",
                ephemeral=True
            )
            return
        resultado = numero1 / numero2

    await interaction.response.send_message(
        f"Resultado da operação **{operacao.name}**: `{resultado}`"
    )
    
# Comando /embed
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

bot.run(discord_token)
