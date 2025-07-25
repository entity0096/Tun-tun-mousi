import discord
import os
import random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

responses = [
    "Tun Tun Mousi 😎",
    "Laddoo chahiye! 🍮",
    "Main hoon legend 😤👑",
    "Kisne yaad kiya mujhe? 😏📞",
    "Aree beta, tumse na ho payega! 😂❌",
    "Mousi sab dekh rahi hai 👀🔍",
    "Padhai karo, gamer ban jao 📚🎮",
    "Tumhara kya hoga kaalia? 😈🔥",
    "khaali peeli mat mention karo 🍭🚫",
    "Mujhe bas chill karna hai 😌🛋️",
    "Laddoo khaate time disturb mat karo 😒🍬",
    "Mousi busy hai, meme bana rahi hai 🖼️🤣",
    "Coding ho ya pyaar, sab me expert hoon 😌💻❤️",
    "Mousi OP, baki sab flop 💅👑",
    "Pehle laddoo, baad me baat 😤🍮🕒",
    "Tameez se mention karo, Mousi hoon main 😌📢",
    "Beta tumse na ho payega, jao so jao 🛌😴",
    "Ping kiya? Shraap lagega 🧙‍♀️✨⚡",
    "Mousi sad ho gayi... kyunki laddoo khatam 😢🍭❌",
    "Ras gulla bhi lao 😋🍡",
    "Kya ha be? 🤨🫵",
    "Namaskaar 🙏😊",
    "Chhuttee kahan h? 🏖️📆",
    "Bheja mat khao 😵🧠",
    "So gaya kya? 😴💤",
    "Abe chup ho jaa 🤫🔇",
    "Toh kya karun main, job chhod du? 😐💼❓",
    "Yeh sab dogalaapan h 😒🎭",
    "Dholakpur me sab theek h? 🥁🏰",
    "Ye bhi Tun Tun Mousi h 😎💥"
]

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')

@client.event
async def on_message(message):
    if client.user in message.mentions and not message.author.bot:
        await message.channel.send(random.choice(responses))

keep_alive()
client.run(os.getenv("TOKEN"))
