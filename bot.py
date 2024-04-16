import discord
import config
import random
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from io import StringIO
from keep_alive import keep_alive
from datetime import datetime, timedelta

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print('ログインしました')
    new_activity = f"テスト起動中"
    await client.change_presence(activity=discord.Game(new_activity))
    await tree.sync()

@tree.command(name='dice', description='Roll a dice with given number of sides')
async def roll_dice(interaction: discord.Interaction, sides: int = 6):
    if sides < 2:
        await interaction.response.send_message('サイコロの面数は2以上で指定してください。')
        return
    result = random.randint(1, sides)
    await interaction.response.send_message(f'サイコロを振った結果: {result}')

keep_alive()
client.run(config.DISCORD_TOKEN)
