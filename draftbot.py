import os
import discord
from discord.ext import commands
from Levenshtein import distance

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # Add this line to enable the message content intent
intents.presences = True  # Add this line to enable the presence intent
intents.members = True  # Add this line to enable the server members intent

bot = commands.Bot(command_prefix='/', intents=intents)

# Directory containing the map images
MAP_DIRECTORY = './map_images'

# Read the token from the file
with open("../discord_token", "r") as token_file:
    token = token_file.readline().strip()

@bot.command(name='draft')
async def draft(ctx, *, map_name):
    # Get a list of all image files in the directory
    image_files = [f for f in os.listdir(MAP_DIRECTORY) if f.endswith('.png') or f.endswith('.jpg')]
    
    # Find the image with the closest match using Levenshtein distance
    closest_match = min(image_files, key=lambda x: distance(map_name.lower(), os.path.splitext(x)[0].lower()))
    
    # Send the closest matching image
    await ctx.send(file=discord.File(os.path.join(MAP_DIRECTORY, closest_match)))

bot.run(token)
