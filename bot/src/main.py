import discord


class MyClient(discord.Client):

    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):

        text_channel = message.channel
        voice_channel = message.author.voice.channel

        def is_me(message):
            return message.author == self.user

        # Welcome / Hello
        
        if message.content.startswith('!hello'):
            try:
                await text_channel.send(f'Hello {message.author}! How are You?')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')

        # Clear Chat

        if message.content.startswith('!clearchat'):
            try:
                deleted = await text_channel.purge(limit=100, check=is_me)
                await text_channel.send(f'Deleting {len(deleted)} messages...')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')

        # Play Music

        if message.content.startswith('!play'):
            try:
                await voice_channel.connect()
            except discord.ClientException:
                await text_channel.send(f'Ops! The bot is already connected to a Voice Channel!')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')
            
        if message.content.startswith('!quit'):
            try:
                await message.voice_client.disconnect()
            except discord.ClientException:
                await text_channel.send(f'Ops! The bot is not in a Voice Channel!')
            except Exception as e:
                await text_channel.send(f'Ops! Occured an Exception! {e}')
                

client = MyClient()
client.run('OTkzMTQ3OTA3NjQzNTM5NTQ2.Gb2CPi.elxCzw8WARUtIvaElwyx3b71hIyNBJ0BZgtGTY')

