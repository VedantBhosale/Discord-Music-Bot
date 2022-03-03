import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='&')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run("NTY3NTk4MzE2ODU5MjkzNjk3.XLV3IA.kgtntPKexqDm5vL_MNzTtJilN74")


#start the bot with our token
# TOKEN = "NTY3NTk4MzE2ODU5MjkzNjk3.XLV3IA.kgtntPKexqDm5vL_MNzTtJilN74"
