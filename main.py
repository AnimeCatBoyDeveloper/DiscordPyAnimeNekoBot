from dotenv import load_dotenv
load_dotenv()

import discord, os
from discord.ext import commands

bot = commands.Bot(command_prefix="nya!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Я готова.~ >//<")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="с тябой :3"))

@bot.command(name="info", pass_context=True)
async def _info(ctx):
    await ctx.send("Приветииикиии, меня зовут Няшка, разрабочик мой - AnimeCatBoyDeveloper#5301, я нихуя не умею, но сделаю ваше пребывание в этой помойке веселее!!!!!1!1!! >/////<\nПопробуй nya!help и узнай!!!!\nЛюблю тебя. :3")

@bot.command(name="help", pass_context=True)
async def _help(ctx):
    await ctx.send("А вот что я могу!\nnya!help - показать эту менюффку. >//<\nnya!info - узнать обо мне побольше! :3\nnya!hug - абнимафффффки!!!! :3\nnya!pat - погладить по головочке, м-м-мяу... :pleading_face:\nnya!memes - мемасики, тебе для улыбочки на личике. :3")

@bot.command(name="hug", pass_context=True)
async def _hug(ctx, member: discord.Member = None):
    if member is None:
        return await ctx.reply("А кого?((((((( :pleading_face: :point_right::point_left:")
    else:
        return await ctx.reply(f"{ctx.author} обняль {member} >////////< Надеюсь что у них все будет харафо :pleading_face:\nhttps://gifimage.net/wp-content/uploads/2017/09/anime-comfort-hug-gif-14.gif")

@bot.command(name="pat", pass_context=True)
async def _pat(ctx, member: discord.Member = None):
    if member is None:
        return await ctx.reply("А кого?((((((( :pleading_face: :point_right::point_left:")
    else:
        return await ctx.reply(f"{ctx.author} обняль котичку {member} >////< Н-няя, хозяин, будь н-нежным.... :pleading_face:\nhttps://i.imgur.com/sLwoifL.gif")

@bot.command(name="memes", pass_context=True)
async def _memes(ctx):
    return await ctx.reply("Мемтики для тебя, хазяин. :3\nhttps://cdn.discordapp.com/attachments/818109921480015915/818116613743575080/wgpKX2oPKXI.png\nhttps://cdn.discordapp.com/attachments/818109921480015915/818116684392038460/CeC4Jq_kQik.png")

bot.run(os.environ.get("BOT_TOKEN"))
