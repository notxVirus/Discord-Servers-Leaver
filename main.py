import discord
from discord.ext import commands
import time
import os
import colorama
from colorama import Fore, init
colorama.init()

access = [1,2,3,4,5] # who can use bot commands
members_required = 10 # if the server member count is less than the specified number, the bot will leave the server. However, if the server member count is equal to or greater than the specified number, the bot will remain in the server.

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@client.event
async def on_conect():
	print(f"{Fore.YELLOW}LOADING{Fore.RESET} | Connecting to the API")

@client.event
async def on_ready():
	print(f"{Fore.GREEN}SUCCESS{Fore.RESET} | Logged in as {Fore.CYAN}{client.user}{Fore.RESET}")
	print(f"{Fore.YELLOW}INFO{Fore.RESET} | Bot Invite Link: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=0&scope=bot%20applications.commands")


@client.command(aliases = ['leave', 'leave_guilds', 'guilds_leave'])
async def start(ctx):
	if ctx.author.id in access:
		guilds = len(client.guilds)
		a = 0
		msg = await ctx.send(f"[`START`](https://github.com/notxVirus) | Starting leave guilds with less than {members_required} members.")
		for guild in client.guilds:
			try:
				os.system(f"title Successfully left {a} server(s). {guilds - a} server(s) left.")
				if guild.member_count < members_required:
					if guild.id == ctx.guild.id:
						print(f"{Fore.RED}DIDN'T LEAVE{Fore.RESET} | Guild {guild} ({guild.id}) because command was used on that server.")
					else:						
						await guild.leave()
						a += 1
						print(f"{Fore.GREEN}SUCCESS{Fore.RESET} | Left {guild} ({guild.id}) with {guild.member_count} members.")
				else:
					print(f"{Fore.RED}DIDN'T LEAVE{Fore.RESET} | Guild {guild} ({guild.id}) has {guild.member_count}, so i didn't leave that guild.")
			except Exception as e:
				print(f"{Fore.RED}ERROR{Fore.RESET} | {e}")
		print(f"{Fore.GREEN}DONE{Fore.RESET} | The bot has completed its shutdown sequence and has now left all the server(s) that had less than {members_required} members. ({a}/{guilds})")
		await msg.reply(f"[`DONE`](https://github.com/notxVirus) | The bot has completed its shutdown sequence and has now left all the server(s) that had less than {members_required} members. ({a}/{guilds})")
		await ctx.send("Thanks for using our script!\nDeveloped by [xVirus](https://github.com/notxVirus)")
	else:
		await ctx.send("stfu, nigga. u can't use this command.", delete_after = 10)

@client.command(aliases = ['leave_all', 'all_leave', 'leave_all_guilds'])
async def all(ctx):
	if ctx.author.id in access:
		guilds = len(client.guilds)
		a = 0
		msg = await ctx.send(f"[`START`](https://github.com/notxVirus) | Starting leave **__ALL__** (**{guilds}**) guilds.\nStart in 15s.")
		time.sleep(15)
		await msg.reply("Started.")
		for guild in client.guilds:
			try:
				if guild.id == ctx.guild.id:
					print(f"{Fore.RED}DIDN'T LEAVE{Fore.RESET} | Guild {guild} ({guild.id}) because command was used on that server.")
				else:
					os.system(f"title Successfully left {a} server(s). {guilds - a} server(s) left.")
					await guild.leave()
					a += 1
					print(f"{Fore.GREEN}SUCCESS{Fore.RESET} | Left {guild} ({guild.id}) with {guild.member_count} members.")
			except Exception as e:
				print(f"{Fore.RED}ERROR{Fore.RESET} | {e}")
		print(f"{Fore.GREEN}DONE{Fore.RESET} | The bot has completed its shutdown sequence and has now left all the server(s) it was in. ({a}/{guilds})")
		await msg.reply(f"[`DONE`](https://github.com/notxVirus) | The bot has completed its shutdown sequence and has now left all the server(s) it was in. ({a}/{guilds})")
		await ctx.send("Thanks for using our script!\nDeveloped by [xVirus](https://github.com/notxVirus)")
	else:
		await ctx.send("stfu, nigga. u can't use this command.", delete_after = 10)

client.run("YOUR DISCORD BOT TOKEN")