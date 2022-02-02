import json
import hikari
import lightbulb
import numpy as np
import ast



verify_plugin = lightbulb.Plugin("Verify")
admin_plugin = lightbulb.Plugin("Admin")

admin_plugin.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
global fx
p=[]



@admin_plugin.command
@lightbulb.option("roleverify", "stores the role that verified access", hikari.Role)
@lightbulb.command("verifyrole", "select the role to which verified users must get assigned")
@lightbulb.implements(lightbulb.SlashCommand)
async def adminrole(ctx: lightbulb.Context) -> None:
    fvr=ctx.options.roleverify
    finalverifyrole[ctx.guild_id]=int(fvr)
    await ctx.respond("\nDone!!")




@admin_plugin.command
@lightbulb.option('idall', 'stores id of all members', type=str)
@lightbulb.command("idadd", "id of members")
@lightbulb.implements(lightbulb.SlashCommand)
async def idadd(ctx: lightbulb.Context) -> None:
        global final
        final=ctx.options.idall.split()
        try:
           p=finalid[ctx.guild_id]
        except KeyError:
            finalid[ctx.guild_id]=[]
        p=finalid[ctx.guild_id]
        p.extend(final)
        finalid[ctx.guild_id]=p
        await ctx.respond("Added!! \ntype'/printid' to see all the id's stored in bot")

    

@admin_plugin.command
@lightbulb.command("printid", "prints id's of all members")
@lightbulb.implements(lightbulb.SlashCommand)
async def printid(ctx: lightbulb.Context) -> None:
    await ctx.respond(finalid[ctx.guild_id])


@verify_plugin.command
@lightbulb.option("yourid","stores your id")
@lightbulb.command("verifyid", "Enter your id")
@lightbulb.implements(lightbulb.SlashCommand)
async def verifyid(ctx :lightbulb.Context) -> None:
    global sysid
    sysid=ctx.options.yourid
    x=False
    for i in finalid[ctx.guild_id]:
        if sysid==i:
            x=True
            
    if x==True:
        finalid[ctx.guild_id].remove(i)
        await ctx.user.app.rest.add_role_to_member(ctx.guild_id, ctx.user.id, finalverifyrole[ctx.guild_id], reason="VERIFIED!")
        await ctx.respond("id:"+sysid+"\nVERIFIED!! Welcome to the server")
    if x==False:
        await ctx.respond("id:"+sysid+"not verified. Please contact the server head")

    

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(admin_plugin)
    bot.add_plugin(verify_plugin)
    @bot.listen()
    async def on_starting(event: hikari.StartingEvent) -> None:
         global finalid
         finalid=dict()
         global finalverifyrole
         finalverifyrole=dict()
         finalid = np.load('finalid.npy',allow_pickle='TRUE').item()
         finalverifyrole = np.load('finalverifyrole.npy',allow_pickle='TRUE').item()

    @bot.listen()
    async def on_stopping(event: hikari.StoppingEvent) -> None:
         np.save('finalid.npy', finalid) 
         np.save('finalverifyrole.npy', finalverifyrole)




