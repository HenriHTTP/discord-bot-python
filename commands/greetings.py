from discord.ext import commands
from utils.message import Message
from views.greetings_view import GreetingView


class Greetings(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
        messages_send_on_server = f'message from  {ctx.author} content: {ctx.content}'
        print(messages_send_on_server)

    @commands.Cog.listener()
    async def on_member_join(self, ctx: commands.Context):
        on_member_join_message = f"Welcome to the server, {ctx.author.mention} We're glad to have you here"
        message = Message(ctx, on_member_join_message, self.__bot)
        await message.send_message_user()

    @commands.command(name='hello')
    async def greet_user(self, ctx: commands.Context):
        greet_user_message = f'hello, {ctx.author} how are you my friend, be welcome to {ctx.guild}'
        message = Message(ctx, greet_user_message, self.__bot)
        await message.send_message_user()


async def setup(bot: commands.bot):
    await bot.add_cog(Greetings(bot))
