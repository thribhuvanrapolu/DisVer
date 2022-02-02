import os
import aiohttp
import dotenv
import hikari
import lightbulb



dotenv.load_dotenv()

bot = lightbulb.BotApp(
    token="OTM1MDQ3NDQ0MzE0NjE1ODM4.Ye48yw.JTghxc9CKH9Bw11Qmd_kaRkDtkY",
    prefix="+",
    banner=None,
    intents=hikari.Intents.ALL,
)


@bot.command
@lightbulb.command("ping", description="Whether the bot is working")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond(f"Pong! Latency: {bot.heartbeat_latency*1000:.2f}ms")


bot.load_extensions_from("./extensions/", must_exist=True)

@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()

@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    await bot.d.aio_session.close()



if __name__ == "__main__":
    if os.name != "nt":
        import uvloop

        uvloop.install()

    bot.run()
