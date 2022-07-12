import discord
from discord_token import DiscordToken


class MyClient(discord.Client):

    # Activate
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):

        text_channel = message.channel
        voice_channel = message.author.voice.channel
        players = {}
        color = 0xF7FE2E

        # Check user
        def is_me(message):
            return message.author == self.user

        # Welcome / Hello Command
        if message.content.startswith('!hello'):
            try:
                await text_channel.send(f'Hello {message.author}! How are You?')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')

        # Clear Chat Command
        if message.content.startswith('!clear'):
            try:
                deleted = await text_channel.purge(limit=100, check=is_me)
                await text_channel.send(f'Deleting {len(deleted)} messages...')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')

        # Play Music #

        # Connect bot to a voice channel
        if message.content.startswith('!enter'):
            try:
                await voice_channel.connect()
            except discord.ClientException:
                await text_channel.send(f'Ops! The bot is already connected to a Voice Channel!')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')
        
        # Disconnect bot from a voice channel
        if message.content.startswith('!quit'):
            try:
                await message.guild.voice_client.disconnect()
            except discord.ClientException:
                await text_channel.send(f'Ops! The bot is not in a Voice Channel!')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')

        # Make the bot play some Youtube Musics with URL
        if message.content.startswith('!play'):
            client = discord.VoiceClient(discord.Client(), voice_channel)

            try:
                yt_url = message.content
                
                if client.is_connected():

                    try:
                        # Some Code Here

                        discord.Embed(title="Music to Play: ",
                        color=color)

                    except Exception as e:
                        await text_channel.send(f'Ops! Occured an Exception! {e}')
            
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')


# Run
client = MyClient()
client.run(DiscordToken.token())
