import discord
import asyncio
import os

from discord.ext import commands
from discord import Game
from discord import Colour
from discord import Embed
from discord import Role
from discord import Emoji
from discord.utils import get
from fuzzywuzzy import process

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='-', intents=intents)

token = os.getenv("DISCORD_BOT_TOKEN")

@bot.event
async def on_ready():
  print("loading...")
  await asyncio.sleep(2)
  guild = bot.get_guild(782436793705693205)
  Playing=discord.Game(name=f"{guild.name} Transactions")
  await bot.change_presence(status=discord.Status.dnd, activity=Playing)
  print("loaded!")
  await asyncio.sleep(1)
  print(f"Client connected as @{bot.user.name}#{bot.user.discriminator}")

@bot.event
async def on_message(message):
  if message.content.startswith('<:ARI:826850476640698390> sign'):
    names = [
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Arizona Cardinals")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Arizona Cardinals`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:ARI:826850476640698390> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:ATL:826850472001667072> sign'):
    names = [
      "Arizona Cardinals",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Atlanta Falcons")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)



    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Atlanta Falcons`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:ATL:826850472001667072> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:BAL:826850459070758982> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Baltimore Ravens")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Baltimore Ravens`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:BAL:826850459070758982> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:BUF:826850454771859466> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Buffalo Bills")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)



    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Buffalo Bills`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:BUF:826850454771859466> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CAR:826850450820825128> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Carolina Panthers")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Carolina Panthers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:CAR:826850450820825128> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CHI:826850438946095174> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Chicago Bears")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Chicago Bears`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:CHI:826850438946095174> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CIN:826850434294612010> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Cincinnati Bengals")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
        pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Cincinnati Bengals`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:CIN:826850434294612010> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)


    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CLE:826850430163877909> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Cleveland Browns")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Cleveland Browns`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:CLE:826850430163877909> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)


    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:DAL:826850417606262806> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Dallas Cowboys")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Dallas Cowboys`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:DAL:826850417606262806> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:DEN:826850412949667841> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Denver Broncos")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Denver Broncos`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:DEN:826850412949667841> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:DET:826850408122548314> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Detroit Lions")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Detroit Lions`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:DET:826850408122548314> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:GB:826850397024026664> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Green Bay Packers")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Green Bay Packers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:GB:826850397024026664> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:HOU:826850392188518400> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Houston Texans")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Houston Texans`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:HOU:826850392188518400> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:IND:826850387071205387> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Indianapolis Colts")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Indianapolis Colts`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:IND:826850387071205387> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:JAX:826850373171806279> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Jacksonville Jaguars")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Jacksonville Jaguars`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:JAX:826850373171806279> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:KC:826850369002930206> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Kansas City Chiefs")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Kansas City Chiefs`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:KC:826850369002930206> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:LAC:826850365030531114> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Los Angeles Chargers")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Los Angeles Chargers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:LAC:826850365030531114> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:LAR:826850353168646154> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Los Angeles Rams")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Los Angeles Rams`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:LAR:826850353168646154> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:LV:826850347758780470> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Las Vegas Raiders")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Las Vegas Raiders`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:LV:826850347758780470> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:MIA:826850343534460969> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Miami Dolphins")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Miami Dolphins`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:MIA:826850343534460969> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:MIN:826850331093762079> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Minnesota Vikings")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Minnesota Vikings`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:MIN:826850331093762079> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:NE:826850326355247165> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New England Patriots")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New England Patriots`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:NE:826850326355247165> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)
  
  if message.content.startswith('<:NO:826850322340249620> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New Orleans Saints")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New Orleans Saints`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:NO:826850322340249620> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:NYG:826850310622281809> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New York Giants")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New York Giants`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:NYG:826850310622281809> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:NYJ:826850305584791552> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New York Jets")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New York Jets`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:NYJ:826850305584791552> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:PHI:826850301012607026> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Philadelphia Eagles")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Philadelphia Eagles`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:PHI:826850301012607026> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:PIT:826850288500998184> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Pittsburgh Steelers")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Pittsburgh Steelers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:PIT:826850288500998184> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:SEA:826850283590123520> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Seattle Seahawks")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Seattle Seahawks`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:SEA:826850283590123520> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:SF:826850279500283945> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="San Francisco 49ers")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`San Francisco 49ers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:SF:826850279500283945> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:TB:826850266564395079> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Tampa Bay Buccaneers")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Tampa Bay Buccaneers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:TB:826850266564395079> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:TEN:826850262601826373> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Tennessee Titans")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Tennessee Titans`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:TEN:826850262601826373> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:WAS:826850258256265216> sign'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Washington Football Team")

    if len(team_role.members) >= 25:
      embed=discord.Embed(title="Transaction Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} **Your Roster Cap Space is `Full`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      return await message.channel.send(embed=embed)


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Washington Football Team`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.add_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing", value=f"{member.mention} Signed to the <:WAS:826850258256265216> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Signing Error:", value=f"{member.mention} Already Signed to a \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:ARI:826850476640698390> release'):
    names = [
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Arizona Cardinals")

    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Arizona Cardinals`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:ARI:826850476640698390> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:ATL:826850472001667072> release'):
    names = [
      "Arizona Cardinals",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Atlanta Falcons")



    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Atlanta Falcons`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:ATL:826850472001667072> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:BAL:826850459070758982> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Baltimore Ravens")


    if team_role in message.author.roles:
      pass

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Baltimore Ravens`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:BAL:826850459070758982> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:BUF:826850454771859466> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Buffalo Bills")



    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Buffalo Bills`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:BUF:826850454771859466> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CAR:826850450820825128> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Carolina Panthers")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Carolina Panthers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:CAR:826850450820825128> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CHI:826850438946095174> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Chicago Bears")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Chicago Bears`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:CHI:826850438946095174> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CIN:826850434294612010> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Cincinnati Bengals")


    if team_role in message.author.roles:
        pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Cincinnati Bengals`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:CIN:826850434294612010> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)


    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:CLE:826850430163877909> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Cleveland Browns")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Cleveland Browns`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:CLE:826850430163877909> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)


    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:DAL:826850417606262806> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Dallas Cowboys")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Dallas Cowboys`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:DAL:826850417606262806> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:DEN:826850412949667841> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Denver Broncos")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Denver Broncos`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:DEN:826850412949667841> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:DET:826850408122548314> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Detroit Lions")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Detroit Lions`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:DET:826850408122548314> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:GB:826850397024026664> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Green Bay Packers")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Green Bay Packers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:GB:826850397024026664> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:HOU:826850392188518400> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Houston Texans")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Houston Texans`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:HOU:826850392188518400> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:IND:826850387071205387> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Indianapolis Colts")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Indianapolis Colts`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:IND:826850387071205387> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:JAX:826850373171806279> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Jacksonville Jaguars")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Jacksonville Jaguars`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:JAX:826850373171806279> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:KC:826850369002930206> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Kansas City Chiefs")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Kansas City Chiefs`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:KC:826850369002930206> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:LAC:826850365030531114> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Los Angeles Chargers")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Los Angeles Chargers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:LAC:826850365030531114> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:LAR:826850353168646154> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Los Angeles Rams")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Los Angeles Rams`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:LAR:826850353168646154> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:LV:826850347758780470> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Las Vegas Raiders")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Las Vegas Raiders`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:LV:826850347758780470> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:MIA:826850343534460969> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Miami Dolphins")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Miami Dolphins`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:MIA:826850343534460969> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:MIN:826850331093762079> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Minnesota Vikings")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Minnesota Vikings`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:MIN:826850331093762079> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:NE:826850326355247165> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New England Patriots")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New England Patriots`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:NE:826850326355247165> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)
  
  if message.content.startswith('<:NO:826850322340249620> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New Orleans Saints")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New Orleans Saints`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:NO:826850322340249620> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:NYG:826850310622281809> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New York Giants")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New York Giants`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:NYG:826850310622281809> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:NYJ:826850305584791552> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="New York Jets")


    if team_role in message.author.roles:
      pass
    
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`New York Jets`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:NYJ:826850305584791552> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:PHI:826850301012607026> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Philadelphia Eagles")


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Philadelphia Eagles`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:PHI:826850301012607026> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:PIT:826850288500998184> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Pittsburgh Steelers")


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Pittsburgh Steelers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:PIT:826850288500998184> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:SEA:826850283590123520> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Seattle Seahawks")


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Seattle Seahawks`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:SEA:826850283590123520> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:SF:826850279500283945> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "Tampa Bay Buccaneers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="San Francisco 49ers")


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`San Francisco 49ers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:SF:826850279500283945> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:TB:826850266564395079> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tennessee Titans",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Tampa Bay Buccaneers")


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Tampa Bay Buccaneers`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:TB:826850266564395079> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:TEN:826850262601826373> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Washington Football Team"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Tennessee Titans")


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Tennessee Titans`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:TEN:826850262601826373> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  if message.content.startswith('<:WAS:826850258256265216> release'):
    names = [
      "Arizona Cardinals",
      "Atlanta Falcons",
      "Baltimore Ravens",
      "Buffalo Bills",
      "Carolina Panthers",
      "Chicago Bears",
      "Cincinnati Bengals",
      "Cleveland Browns",
      "Dallas Cowboys",
      "Denver Broncos",
      "Detroit Lions",
      "Green Bay Packers",
      "Houston Texans",
      "Indianapolis Colts",
      "Jacksonville Jaguars",
      "Kansas City Chiefs",
      "Los Angeles Chargers",
      "Los Angeles Rams",
      "Las Vegas Raiders",
      "Miami Dolphins",
      "Minnesota Vikings",
      "New England Patriots",
      "New Orleans Saints",
      "New York Giants",
      "New York Jets",
      "Philadelphia Eagles",
      "Pittsburgh Steelers",
      "Seattle Seahawks",
      "San Francisco 49ers",
      "Tampa Bay Buccaneers",
      "Tennessee Titans"
    ]
    roles = discord.utils.find(lambda r: r.name == names, message.guild.roles)
    member = message.mentions[0]
    team_role = get(message.guild.roles, name="Washington Football Team")


    if team_role in message.author.roles:
      pass
      
    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{message.author.mention} Does not have \n Required Role:\n**`Washington Football Team`**", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar_url)
      return await message.channel.send(embed=embed)

    if roles not in member.roles:
      await member.remove_roles(team_role)
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing", value=f"{member.mention} Signed to the <:WAS:826850258256265216> \n***Current Roster Count: `{len(team_role.members)}` Players***", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

    else:
      embed=discord.Embed(title="Transactions Information:", color=team_role.color)
      embed.set_author(name=f"{bot.user.name}#{bot.user.discriminator}", icon_url = bot.user.avatar_url)
      embed.add_field(name="Releasing Error:", value=f"{member.mention} Cannot be released from this \n CFL Franchise...", inline=False)
      embed.set_footer(text=f"{message.author.name}#{message.author.discriminator}", icon_url = message.author.avatar_url)
      await message.channel.send(embed=embed)

  

  await bot.process_commands(message)

@bot.command(name='members', aliases=['member'])
async def members(ctx, *args):


        if len(args) < 1:
          return await ctx.send(f'Missing/Unvalid Argument.')

        arg = ' '.join(args)
        
        if args[-1].isdigit():
          arg = arg.rsplit(' ', 1)[0]

        if len(ctx.message.role_mentions) < 1: 
            found_name = process.extractOne(
                arg, [role.name for role in ctx.message.guild.roles]
            )
            found_role = discord.utils.find(
                lambda m: m.name == found_name[0], ctx.message.guild.roles
            )
            if found_role is None:
              return await ctx.send('**I found no role retard.**')
        else:
            found_role = ctx.message.role_mentions[0]

        if args[-1].isdigit():
          page_count = 1 if (len(args) < 2) else int(args[-1])

        else:
          page_count = 1
          
        n = 15
        chunked_members = [
            found_role.members[
                i * n:(i + 1) * n
            ] for i in range(
                (len(found_role.members) + n - 1) // n
            )
        ]
        


        em = discord.Embed(
            title=f"{found_role.name} Member List",
            color=found_role.color,
        )
        em.set_author(name = f'{ctx.author.name}', icon_url = ctx.author.avatar_url)
        em.set_footer(
            text=f"Page {page_count}/{str(len(chunked_members))} "
            
        )

        try:
            for member in chunked_members[page_count - 1]:
                em.add_field(
                    name=f"{member.top_role}",
                    value=f"{member.mention}\n"
                          f"{member.name}#{member.discriminator}"
                )
        except IndexError:
            if page_count > len(chunked_members) and len(chunked_members) != 0:
                return await ctx.send('**Thats Over the page limit autsimo.**')
            elif len(chunked_members) == 0:
                return await ctx.send('**I Couldn\'t find any members.**')

        await ctx.send(embed=em)

try:
  bot.run(token)
except Exception as e:
  print(e)
