import discord
import random
import asyncio
import os

# -----------------------------
# SETTINGS
# -----------------------------
TOKEN = os.getenv("DISCORD_TOKEN")   # Gets token from environment variable
CHANNEL_ID = 1310860330095611923     # Replace with your channel ID
OWNER_ID = 730303104192610324        # Your Discord user ID
# -----------------------------

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# List of random messages
messages = [
    "Cater CAÇADA 200 Wings",
    "CAÇADA on top!",
    "Daily School Snap",
    "Sneezy Boyyy",
    "NebraskaCookie",
    "Prime Cookie might be 2025",
    "CAÇADA Live Event Incident",
    "Here Aura Take This!",
    "Ziiiiiinxx",
    "Sneezy for Owner?",
    "I Love You",
    "Jesus Loves You!",
    "You know I can’t control my love for you",
    "It might be time for Sneezy to lock in",
    "Alright brooo like I cant! like yesterday I kinda could but today I really cant!",
    "Come eat with me!",
    "Can I join someone’s 5 stack for Siege ranked? :)",
    "Jenks High School",
    "1v1 me Dad Bot.",
    "I’ll see y’all, on the flip sideeeeeeeee",
    "GG's, Kushly.",
    "Prime Chico",
    "Jordan Barret",
    "Riymoo",
    "Set your heart ablaze.",
    "Vanguard Incident",
    "Bug Blaster"
]

# -----------------------------
# RANDOM MESSAGE TASK
# -----------------------------
async def random_messages():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while True:
        await asyncio.sleep(random.randint(900, 1560))  # 15–26 minutes
        await channel.send(random.choice(messages))

# -----------------------------
# EVENTS
# -----------------------------
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    # Start random message loop
    client.loop.create_task(random_messages())

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # Only allow OWNER to use commands
    if message.author.id == OWNER_ID:
        # SAY COMMAND
        if message.content.startswith("!say "):
            say_message = message.content[5:]
            await message.channel.send(say_message)
            await message.delete()

        # IMGURL COMMAND
        elif message.content.startswith("!imgurl "):
            image_url = message.content[8:]
            await message.channel.send(image_url)
            await message.delete()

        # IMG COMMAND
        elif message.content.startswith("!img "):
            image_file = message.content[5:]
            try:
                await message.channel.send(file=discord.File(image_file))
            except Exception as e:
                await message.channel.send(f"Could not send image: {e}")
            await message.delete()

        # POLL COMMAND
        elif message.content.startswith("c!poll "):
            poll_question = message.content[7:]
            poll_msg = await message.channel.send(
                f"📊 **Poll:** {poll_question}\n\n✅ = Yes\n❌ = No"
            )
            await poll_msg.add_reaction("✅")
            await poll_msg.add_reaction("❌")
            await message.delete()

# -----------------------------
# RUN BOT
# -----------------------------
client.run(TOKEN)
