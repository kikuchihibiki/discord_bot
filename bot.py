import discord
import random
from discord.ext import commands
from discord import app_commands
from discord.utils import get
from io import StringIO
from keep_alive import keep_alive
from datetime import datetime, timedelta
import os
from test_spotyfy import search_sound

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

@tree.command(name='song', description='search song')
async def search_song(interaction: discord.Interaction, sides: str = "", artist_name: str = ""):
    if not sides and not artist_name:
        await interaction.response.send_message("曲名とアーティスト名を入力してください")
        return
    
    results = search_sound(sides, artist_name)
    if not results:
        await interaction.response.send_message("曲が見つかりませんでした")
        return
    
    embed = discord.Embed(title="Song Information", color=0x00ff00)
    for result in results:
        song_name, artist_name, preview_url, album_image_url = result
        embed.add_field(name="Song Name", value=song_name, inline=False)
        embed.add_field(name="Artist Name", value=artist_name, inline=False)
        embed.add_field(name="Preview URL", value=preview_url, inline=False)
        embed.set_image(url=album_image_url)

    # ループが終了した後に1度だけメッセージを送信
    await interaction.response.send_message(embed=embed)
TOKEN = os.getenv("DISCORD_TOKEN")
keep_alive()
client.run(TOKEN)
