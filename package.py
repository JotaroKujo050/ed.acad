import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('>hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('>notanass'):
        await message.channel.send('Hello! I have been summoned to tell you that this conversation is too triggering or against the rules. If you do not move on, we will give out warnings, mutes and bans. Some things you can talk about are Shakespeare, gluten free foods and asking about eachother's wellbeing. 😁')
            if message.content.startswith('>server-invite'):
        await message.channel.send('You want the server invite? Ask Joe, he'll be happy tp give you it 😀')
client.run('your token here')
