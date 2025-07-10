import discord
from discord.ext import commands
import string
import random
import aiohttp
import requests
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = 1372820645754306681
last_found_user = {}
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    bot.loop.create_task(random_dm_task())

def create_embed(title, description, user):
    embed = discord.Embed(title=title, description=description, color=discord.Color.orange())
    if user.avatar:
        embed.set_thumbnail(url=user.avatar.url)
    else:
        embed.set_thumbnail(url=user.default_avatar.url)
    return embed

import asyncio

async def random_dm_task():
    await bot.wait_until_ready()
    guild = bot.get_guild(1368038012042346516)

    if not guild:
        print("❌ Server not found.")
        return

    jokes = ["Yo bro i just send u a dm to tell you that i love you dude and keep going man fucking dickhead always supports u we can always get hoes together babes",
    "lets fuck anisa tg","u want yozuial or nah between us bro ik u want her","YO BRO i can set u up with kisha u interested?",
    "ngl bro i think antilq might be gay asf","i love you","dude yk how hot zyrsiaa is bro? like between me and u wanna esex her?",
    "bro i wont tell anyone do u fw gay porn?","lmk if u want gaia she has big knockers bro ive seen them","bro does bry have big boobs dude i kinda want some",
    "yo g i heard that dana has a big ass is that true bro? like i needa know"
    ]

    while not bot.is_closed():
        members = [m for m in guild.members if not m.bot and m.status != discord.Status.offline]
        if members:
            member = random.choice(members)
            try:
                await member.send(random.choice(jokes))
                print("SENT DM!")
            except discord.Forbidden:
                print("Retard")

        wait_time = random.randint(18000, 36000)  # This is seconds → 5 to 10 HOURS
        print(f"⏳ Waiting {wait_time // 3600}h {(wait_time % 3600) // 60}m until next DM...")
        await asyncio.sleep(wait_time)

@bot.event
async def on_presence_update(before, after):
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("❌ Channel not found")
        return

    if before.status != after.status:
        embed = create_embed(
            title="Status Changed!",
            description=f"⚡ {after.name} changed status from **{before.status}** to **{after.status}**! HE TRHINKS WE CANT SEE HIM LOL! DUMB KID IM WATCHING",
            user=after
        )
        await channel.send(embed=embed)

    before_custom = None
    after_custom = None

    # Extract custom status from before.presence activities (if any)
    for activity in before.activities:
        if isinstance(activity, discord.CustomActivity):
            before_custom = activity.state  # The text message in custom status

    # Extract custom status from after.presence activities (if any)
    for activity in after.activities:
        if isinstance(activity, discord.CustomActivity):
            after_custom = activity.state

    if before_custom != after_custom:
        embed = discord.Embed(
            title=f"{after.name} changed their custom status!",
            color=discord.Color.orange()
        )
        embed.add_field(name="Old Custom Status", value=before_custom or "None", inline=False)
        embed.add_field(name="New Custom Status", value=after_custom or "None", inline=False)
        embed.set_thumbnail(url=after.avatar.url if after.avatar else after.default_avatar.url)
        await channel.send(embed=embed)

@bot.command(name="namegen")
async def generate_name(ctx):
    styles = ['syllabic', 'random']
    names = []

    for i in range(10): 
            syllables = ['ae', 'lor', 'ven', 'dra', 'mir', 'thal', 'zor', 'ul', 'ix', 'en', 'xor', 'vul', 'ath', 'ves', 'ism', 'dem','des','tri','pho','ex',"sif","tre"]
            name_parts = random.choices(syllables, k=random.randint(2, 3))
            name = ''.join(name_parts).capitalize()
            names.append(name)

    formatted_names = "\n".join([f"{i+1}. {name}" for i, name in enumerate(names)])
    await ctx.send(f"**🎲 Here are some spicy generated names:**\n{formatted_names}")

@bot.command(name="roast")
async def roast_game(ctx,member:discord.Member):
    roasts = {
    633756140848545803 : ["Bitchass nigga abuses steroids everyday whens yo next pin bitch",
    "Hairy ass nigga","U like them emo u worship devils now?","wheres sevdoll awww 🥺","wanna gang bang and fuck stupjdgirl?",
    "ill fuck sssnatcher do some about it","no more dating chubby chicks buddy","nigga said i love u to a trasngender gg"
    ],
    812871484283420703 : ["Rapist ass nigga","Bro wants that norwegian pussy chase after it like i chased ur mom the night of the wedding",
    "niggas a faggot hs gonna sexually assault me everytime im not the norwegian my friend Xd","Siffeh? u mean suckmycockffeh",
    "bitchass nigga u died to tyler aka sarlexzes cock Xd"
    ],
    704707034846593086 : ["We really gonna roast this guy? The girl traumatizer i know him.","wheres rose at 15 21 nigga i know about u",
    "nigga e fucked every female on this roblox game hows ur mamacita rosey i want her too",
    "Oh sorry im parking my car outside- sentry","All the females come and go by 24 hours and the guys stay forever Xd",
    "i want that i want her! what else you want my cock? Xd"],

    903643157122666518 : ["Oh no Antilq, Safi is going to come and I’ll end up bombing both these nggas",
    "burgersandcats the 372031th one that guy gets me angry","so a 9 yr old can be with a 75 year old? Antilq answer:ye",
    "dont talk antilq OCTAVIAN OCTAVIA MOTHERFUCKING PUSSY SAY SOMETHING TO ME","I wanna fuck zyrsiaas brains out Xd",
    "i wanna know how fat are zyrsiaas flaps gaiass kid","lol xd wheres toxic i want her cum on my screen",
    "watch when i fuck the shit out of gaia nigga","duck ass nigga"],

    312653098566811650 : ["VARRATER ILL FUCKIGN RAPE YOU MOTHERFUCKER","ATOMIC BOMB NIGGA","what u gonna do to me man? describe every detail like a good boy",
    "u know i fucked the shit out of wrathverrater right?","u still got juanitas tit pics saved? help a brother out cmon nig",
    "bro ur so sexy but ur such a faggot i hate it u turn me on"],

    520597207343169595 : ["Unre FEET TITTIES xd","Bros a transformer turn into a girl for me nigga xd","Bro efucks men everyday niggas gay",
    "u want nour back bro? or u want me to fuck her instead nigga","lol yea i know unre i fucked his feet and tits"],

    781941498811908126 : ["Haui bro should we fuck anisa together?","wats geht nigguh","lol bro lowkey just take dollers ex and let me fck anisa",
    "wanna have gay strong interracial sex?","im sexually mad for ur penis nigga"]
    }
    userr = member.id
    if userr in roasts:
        roast_line = random.choice(roasts[userr])
    await ctx.send(f"{member.mention} {roast_line}")

found_headless_users = {}
HEADLESS_ID = 15093053680  # Asset ID for Headless Head
@bot.command(name="headless")
async def retrieve_headless(ctx, group_id):
    group_id = str(group_id)  # Store keys as strings
    loading_msg = await ctx.send("🔍 Searching for a Headless user in the group...")

    if group_id not in found_headless_users:
        found_headless_users[group_id] = set()

    async with aiohttp.ClientSession() as session:
        cursor = None
        while True:
            group_url = f"https://groups.roblox.com/v1/groups/{group_id}/users?limit=100&sortOrder=Asc"
            if cursor:
                group_url += f"&cursor={cursor}"

            async with session.get(group_url) as r:
                data = await r.json()

            if "errors" in data:
                await loading_msg.edit(content="❌ Invalid group ID or API issue.")
                return

            users = data.get("data", [])
            cursor = data.get("nextPageCursor")

            for user in users:
                user_data = user.get("user", {})
                user_id = user_data.get("userId")
                username = user_data.get("username")

                if not user_id or not username:
                    continue

                if user_id in found_headless_users[group_id]:
                    continue  # Skip already found users

                # Use full avatar data instead of currently-wearing
                avatar_url = f"https://avatar.roblox.com/v1/users/{user_id}/avatar"
                async with session.get(avatar_url) as r:
                    avatar_data = await r.json()

                assets = avatar_data.get("assets", [])
                if any(asset.get("id") == HEADLESS_ID for asset in assets):
                    found_headless_users[group_id].add(user_id)

                    profile_url = f"https://www.roblox.com/users/{user_id}/profile"
                    thumb_api = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=150x150&format=Png&isCircular=false"
                    async with session.get(thumb_api) as r:
                        thumb_data = await r.json()
                    thumb_url = thumb_data["data"][0]["imageUrl"]

                    embed = discord.Embed(
                        title="🎃 Headless egirl/eboy found!",
                        description=(
                            f"**Username:** [{username}]({profile_url})\n"
                            f"**User ID:** {user_id}\n"
                            f"[View Profile]({profile_url})"
                        ),
                        color=discord.Color.purple()
                    )
                    embed.set_thumbnail(url=thumb_url)

                    await ctx.send(embed=embed)
                    await loading_msg.delete()
                    return

            if not cursor:
                break

    await loading_msg.edit(content="❌ NO IDIOTS WITH HEADLESS FOUND IN THIS GROUP.")

# 🔁 Reset Command
@bot.command(name="headlessreset")
async def reset_headless(ctx, group_id):
    group_id = str(group_id)
    if group_id in found_headless_users:
        found_headless_users[group_id].clear()
        await ctx.send(f"🔄 Headless search for group {group_id} has been reset.")
    else:
        await ctx.send(f"ℹ️ No previous headless search found for group {group_id}.")


@bot.command(name="headlessresetall")
async def reset_all_headless(ctx):
    found_headless_users.clear()
    await ctx.send("🧹 All cached Headless users across all groups have been cleared.")

def get_user_id_from_username(username):
    url = f"https://users.roblox.com/v1/usernames/users"
    res = requests.post(url, json={"usernames": [username]})
    if res.status_code == 200:
        data = res.json()
        if data["data"]:
            return data["data"][0]["id"]

    return None

    
bot.run(BOT_TOKEN)