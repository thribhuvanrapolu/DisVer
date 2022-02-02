import hikari
import lightbulb

info_plugin = lightbulb.Plugin("Info")


@info_plugin.command
@lightbulb.command("info",description="gives you information")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def info(ctx: lightbulb.Context) -> None:
    embed = (
        hikari.Embed(
            title=f"DisVer-The Security Bot for your Server",
            colour=0x3B9DFF,
        )
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.avatar_url or ctx.member.default_avatar_url,
        )
        .add_field(
            f"EVERYONE :\nType '/verifyid' and enter your id to get verified",
            value="_______________________________",    
            inline=True,
        )
        .add_field(
            f"\nADMIN :\nType '/setup' and follow the steps in setting up \nType '/admincmd' for commands that are needed for setting up and can only be accessed by administrator ",
            value="_______________________________",
            inline=False, 
        )
    )

    await ctx.respond(embed)


@info_plugin.command
@lightbulb.command("admincmd",description="shows list of admin commands")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def info(ctx: lightbulb.Context) -> None:
    embed = (
        hikari.Embed(
            title=f"DisVer-The Security Bot For Your Server",
            colour=0x3B9DFF,
        )
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.avatar_url or ctx.member.default_avatar_url,
        )
        .add_field(
            f"ADMIN COMMANDS \n'/verifyrole': select the role to which verified user must get assigned \n'/idadd': to add the id \n'/printid': displays all the id's stored in idadd",    
            value="_______________________________",
            inline=True,
        )
    )
    await ctx.respond(embed)







@info_plugin.command
@lightbulb.command("setup",description="how to start")
@lightbulb.implements(lightbulb.PrefixCommand,lightbulb.SlashCommand)
async def info(ctx: lightbulb.Context) -> None:
    embed = (
        hikari.Embed(
            title=f"DisVer-The Security Head of Server",
            colour=0x3B9DFF,
        )
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.avatar_url or ctx.member.default_avatar_url,
        )
        .add_field(
            f"SETUP :\nWeb link:",    
            value="https://disver-bot.w3spaces.com/",
            inline=True,
        )
        .add_field(
            f"SETUP :\nYouTube link:",    
            value="https://www.youtube.com/watch?v=7EV2y9OQWZ4",
            inline=True,
        )
    )
    await ctx.respond(embed)




def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(info_plugin)