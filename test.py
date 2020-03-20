import discord

client = discord.Client()

with open("token.txt", "r") as f:
    token = f.read()

@client.event
async def on_ready():
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith("퀴즈"):
        f = open("quiz.txt","r",encoding = "utf-8")
        quiz = f.readlines()
        f.close()

        f = open("test.txt", "w", encoding="utf-8")
        f.write("quiz.txt")
        f.close()
        await message.channel.send(quiz[0])



@client.event
async def on_reaction_add(reaction, uesr):
    f = open("test.txt", "r", encoding="utf-8")
    quiz1 = f.readlines()
    f.close()
    f = open("quiz.txt", "r", encoding="utf-8")
    quiz = f.readlines()
    f.close()
    if str(reaction.emoji) == "⭕":
        if quiz[1] == "O":
            await reaction.message.channel.send("나이스")
        elif quiz[1] == "X":
            await reaction.message.channel.send("아니야")
    elif str(reaction.emoji) == "❌":
        print("X")



client.run("token")