import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} foi ligado com sucesso.")
    try:
        await bot.tree.sync()
        print("Slash commands sincronizados com sucesso.")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")


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
    embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/4712/4712109.png")

    await interaction.response.send_message(embed=embed)
    
bot.run(discord_token)
