import discord

client = discord.Client()
with open("token.txt", "r") as f:
    token = f.read()

@client.event
async def on_ready():
    print(client.user.id)

@client.event
async def on_message(message):
    print(message.content)
    if "gif" in message.content:
        print("gif")
        embed = discord.Embed(color=0x363535)
        embed.set_image(url=f"https://i.imgur.com/mHl2kpv.gif")
        await message.channel.send(embed=embed)
    else:
        print("png")
client.run(token)