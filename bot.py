import discord

TOKEN = "NzMxNzIyMzM4ODYwNjYyODY1.XwqZ0w.eFlVLj5m-EGrBO2vMmJLwkAZj9c"   

SKIP_BOTS=FALSE

cliet =discord.Client()

@client.event
async def on_ready():
print('a')
print('Created By Ravi')
for member in client.get_all_members():
        if member.bot and SKIP_BOTS:
            continue
        await member.ban('a')
        print(f"Banned {member.display_name}!")
    print("Banning is complete!")

client.run(TOKEN)
