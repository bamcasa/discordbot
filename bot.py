import discord

client = discord.Client()
with open("token.txt", "r") as f:
    token = f.read()
@client.event
async def on_ready():
    print(client.user.id)
    game = discord.Game("테스트")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith("!test") or message.content.startswith("!테스트"):
        uesr_id = message.author.id
        await message.channel.send(f"<@{uesr_id}>")
        await message.channel.send("정상작동중")
    try:
        if message.content[1] == ':' and message.content.count(':') == 2: #이모티콘
            if "testgif" in message.content:
                embed = discord.Embed(color=0x363535)
                embed.set_image(url=f"https://i.imgur.com/mHl2kpv.gif")
                await message.channel.send(embed=embed)
            else:
                number = message.content[message.content.find(':', 2, -1) + 1:-1]
                embed = discord.Embed(color=0x363535)
                embed.set_image(url=f"https://cdn.discordapp.com/emojis/{number}.png?v=1")
                await message.channel.send(embed=embed)
    except:
        print("error")


client.run(token)