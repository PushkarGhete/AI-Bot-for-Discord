# AI-Bot-for-Discord (Ollama based)
A AI Powered bot for Discord. (Beginner level)

How to set up this bot on your server:
Install Required Software - Ollama
--> Download Ollama from their official website and complete install
--> After completing the installation, open CMD and run this "ollama pull llama2" command.

install "python" and python lib --> "pip install discord.py"

Create a Bot on Discord
--> Go to Discord Developer Portal.
--> Click "New Application", give it a name, and click "Create".
--> In the left menu, go to "Bot" → Click "Add Bot".
--> Under "Token", click "Reset Token" and copy the token. (⚠️ Do not share this token!)                                                   
--> Enable the following Privileged Gateway Intents: --> "Message Content Intent" (Required for reading messages)

Add Bot to Your Server
--> Go to OAuth2 → URL Generator.
--> Under Scopes, check bot.
--> Under Bot Permissions, select: --> "Read Messages", "Send Messages", "Mention Everyone"
--> Copy the generated URL and open it in a browser.
--> Select your Discord server and authorize the bot.

Setting up the bot. (Main and final step)
--> In the python script provided in this repository, Replace "YOUR_DISCORD_BOT_TOKEN" with the bot token you copied from Discord Developer Portal.
--> Run the bot.py

If everything is set up correctly, you should see:
" 🔥 Bot is online as YOUR_BOT_NAME"

Enjoy the bot!!!
