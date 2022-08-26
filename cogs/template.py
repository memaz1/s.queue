import platform
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context
from discord.ui import Button, View, Select
from helpers import checks
from discord.utils import get
import asyncio

# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot):
        self.bot = bot


    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="pick",
        description="Tool for selecting characters in ranked.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(player1="Empty", player2="Empty")
    async def ui_command(self, context: Context, *, player1: str, player2: str) -> None:   
        button1 = Button(label="begin", style=discord.ButtonStyle.green, emoji="<:yipee:1011822258219651154>")
        view = View()
        view.add_item(button1)
        player1 = player1.replace('!', '')
        player2 = player2.replace('!', '')
        select1 = Select(
            placeholder=f"Choose {player1}",
            options=[
                discord.SelectOption(label="Isaac", emoji="<:Isaac:1011819302007087154>"),
                discord.SelectOption(label="Isaac_B", emoji="<:Isaac_B:1011820190759133245>"),
                discord.SelectOption(label="Cain", emoji="<:Cain:1011819423675469834>"),
                discord.SelectOption(label="Cain_B", emoji="<:Cain_B:1011820278143275058>"),
                discord.SelectOption(label="Judas", emoji="<:Judas:1011819479832985630>"),
                discord.SelectOption(label="Judas_B", emoji="<:Judas_B:1011820299672617030>"),
                discord.SelectOption(label="???", emoji="<:__:1011819509549649950>"),
                discord.SelectOption(label="???_B", emoji="<:_B:1011820323341074473>"),
                discord.SelectOption(label="Eve", emoji="<:Eve:1011819534560284754>"),
                discord.SelectOption(label="Eve_B", emoji="<:Eve_B:1011820349391904849>"),
                discord.SelectOption(label="Samson", emoji="<:Samson:1011819569461088388>"),
                discord.SelectOption(label="Samson_B", emoji="<:Samson_B:1011820383621632131>"),
                discord.SelectOption(label="Azazel", emoji="<:Azazel:1011819593175679100>"),
                discord.SelectOption(label="Azazel_B", emoji="<:Azazel_B:1011820411970916394>"),
                discord.SelectOption(label="Lost", emoji="<:Lost:1011819700671492099>"),
                discord.SelectOption(label="Lost_B", emoji="<:Lost_B:1011820490026909856>"),
                discord.SelectOption(label="Lilith", emoji="<:Lilith:1011819744699101184>"),
                discord.SelectOption(label="Lilith_B", emoji="<:Lilith_B:1011820515444396047>>"),
                discord.SelectOption(label="Keeper", emoji="<:Keeper:1011819811912818819>"),
                discord.SelectOption(label="Keeper_B", emoji="<:Keeper_B:1011820542975803422>"),
                discord.SelectOption(label="Apollyon", emoji="<:Apollyon:1011819835606446080>"),
                discord.SelectOption(label="Apollyon_B", emoji="<:Apollyon_B:1011820578119897211>"),
                discord.SelectOption(label="Forgotten", emoji="<:Forgotten:1011819955655803051>"),
                discord.SelectOption(label="Forgotten_B", emoji="<:Forgotten_B:1011820606456606770>"),  
        ],row=1)
        view.add_item(select1)

        select2 = Select(
            placeholder=f"Choose {player2}",
            options=[
                discord.SelectOption(label="Isaac", emoji="<:Isaac:1011819302007087154>"),
                discord.SelectOption(label="Isaac_B", emoji="<:Isaac_B:1011820190759133245>"),
                discord.SelectOption(label="Cain", emoji="<:Cain:1011819423675469834>"),
                discord.SelectOption(label="Cain_B", emoji="<:Cain_B:1011820278143275058>"),
                discord.SelectOption(label="Judas", emoji="<:Judas:1011819479832985630>"),
                discord.SelectOption(label="Judas_B", emoji="<:Judas_B:1011820299672617030>"),
                discord.SelectOption(label="???", emoji="<:__:1011819509549649950>"),
                discord.SelectOption(label="???_B", emoji="<:_B:1011820323341074473>"),
                discord.SelectOption(label="Eve", emoji="<:Eve:1011819534560284754>"),
                discord.SelectOption(label="Eve_B", emoji="<:Eve_B:1011820349391904849>"),
                discord.SelectOption(label="Samson", emoji="<:Samson:1011819569461088388>"),
                discord.SelectOption(label="Samson_B", emoji="<:Samson_B:1011820383621632131>"),
                discord.SelectOption(label="Azazel", emoji="<:Azazel:1011819593175679100>"),
                discord.SelectOption(label="Azazel_B", emoji="<:Azazel_B:1011820411970916394>"),
                discord.SelectOption(label="Lost", emoji="<:Lost:1011819700671492099>"),
                discord.SelectOption(label="Lost_B", emoji="<:Lost_B:1011820490026909856>"),
                discord.SelectOption(label="Lilith", emoji="<:Lilith:1011819744699101184>"),
                discord.SelectOption(label="Lilith_B", emoji="<:Lilith_B:1011820515444396047>>"),
                discord.SelectOption(label="Keeper", emoji="<:Keeper:1011819811912818819>"),
                discord.SelectOption(label="Keeper_B", emoji="<:Keeper_B:1011820542975803422>"),
                discord.SelectOption(label="Apollyon", emoji="<:Apollyon:1011819835606446080>"),
                discord.SelectOption(label="Apollyon_B", emoji="<:Apollyon_B:1011820578119897211>"),
                discord.SelectOption(label="Forgotten", emoji="<:Forgotten:1011819955655803051>"),
                discord.SelectOption(label="Forgotten_B", emoji="<:Forgotten_B:1011820606456606770>"), 
        ],row=2)
        view.add_item(select2)


        async def button1_callback(interaction):
            if select1.values[0] != 0:
                if select2.values[0] != 0:
                    if context.message.author.mention == interaction.user.mention:
                        await interaction.response.edit_message(content=f"**{select1.values[0]}** was selected   |   **{select2.values[0]}** was selected")
        button1.callback = button1_callback


        async def select1_callback(interaction):
            if player1 == interaction.user.mention:
                await interaction.response.edit_message(content="Selecting...")
        select1.callback = select1_callback

        async def select2_callback(interaction):
            if player2 == interaction.user.mention:                
                await interaction.response.edit_message(content="Selecting...")
        select2.callback = select2_callback







        embed = discord.Embed(
        title="**Dodgebomb character picker:**",
        description=f"ーーーーーーーーーーーーーーーー",
        color=0xfeaba3
        )
        embed.set_footer(
        text=f" ーーーーーーーーーーーーーーーーーー "
        )
        if context.message.author.avatar is not None:            
            embed.set_thumbnail(
                url=context.message.author.avatar.url
        )
        embed.add_field(
            name="Player 1",
            value=f"{player1}"
        )
        embed.add_field(
            name="Player 2",
            value=f"{player2}"
        )
        embed.add_field(
            name=f"..........................|",
            value=f".............................|"
        )
        embed.add_field(
            name="Host",
            value=f"{context.message.author.mention}"
        )


        msg = await context.send(".", embed=embed, view=view)

    @commands.hybrid_command(
        name="rolebutton",
        description="Displays role button",
    )
    @checks.not_blacklisted()
    @commands.has_role("Bomb Grimace (Admin)")
    @app_commands.describe(role="empty", desc1="empty", desc2="empty", desc3="empty", desc10="empty", desc20="empty", desc30="empty")
    async def rolebutton_command(self, context: Context, *, role: str, desc1: str, desc2: str, desc3: str, desc10: str, desc20: str, desc30: str) -> None:   
        role1 = discord.utils.get(context.guild.roles, name=role)
        embed = discord.Embed(title=f"**{role1} Role Giver**",description=f"ーーーーーーーーーーーーーーーー",color=0xfeaba3)           
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/avatars/1012550910037217341/6e0988c591287b9c7775c5c5715c5cb6.webp?size=1024"
        )
        if desc1 != 'empty':
            embed.add_field(
                name=f"{desc1}",
                value=f"{desc10}"
        )
        if desc2 != 'empty':
            embed.add_field(
                name=f"{desc2}",
                value=f"{desc20}"
        )
        if desc3 != 'empty':
            embed.add_field(
                name=f"{desc3}",
                value=f"{desc30}"
        )
        view = View()

        button1 = Button(label="yipee", style=discord.ButtonStyle.green, emoji="<:yipee:1011822258219651154>")
        view.add_item(button1)
        async def button1_callback(interaction):
            user = interaction.user
            if role1 not in interaction.user.roles:
                await user.add_roles(role1)
                await interaction.response.send_message(f"Role @{role1} added", ephemeral=True)
            else:
                await user.remove_roles(role1)
                await interaction.response.send_message(f"Role @{role1} removed", ephemeral=True)
        button1.callback = button1_callback
            
        




        msg = await context.send(".", embed=embed, view=view)


















    @commands.hybrid_command(
        name="test",
        description="Test command.",
    )
    @checks.not_blacklisted()
    @commands.has_role("EST")
    @app_commands.describe(empty1="Empty", empty2="Empty")
    async def test_command(self, context: Context, *, empty1: str, empty2: str) -> None:   
        embed = discord.Embed(title="**test:**",description=f"ーーーーーーーーーーーーーーーー",color=0xfeaba3)
        view = View()
        msg = await context.send(".", embed=embed, view=view)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Template(bot))