import discord
import subprocess
import subprocess
from discord.ext import commands

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True  # Allow bot to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Define bot's personality
BOT_PERSONALITY = "You are a brutally honest, sarcastic AI with a rugged personality. You roast people but in a humorous way. Be sharp, witty, and unpredictable."

@bot.event
async def on_ready():
    print(f"🔥 Bot is online as {bot.user}")

# Function to get a response from LLaMA via Ollama
def get_llama_response(user_message):
    try:
        process = subprocess.run(
            ["ollama", "run", "llama2", user_message],  # Removed unnecessary formatting
            capture_output=True,
            text=True,
            timeout=30  # Prevents bot from hanging
        )
        
        if process.returncode != 0:
            return "Error: Ollama didn't respond properly."

        return process.stdout.strip()
    
    except subprocess.TimeoutExpired:
        return "something went wrong"

    except Exception as e:
        return f"Error: {str(e)}"

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and not message.author.bot:
        user_input = message.content.replace(f"<@{bot.user.id}>", "").strip()
        reply = get_llama_response(user_input)
        await message.channel.send(reply)

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

# Run the bot with your Discord token
bot.run("YOUR_DISCORD_BOT_TOKEN")
