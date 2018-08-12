import discord
import os
from discord.ext import commands
import random
import asyncio
import random
bot = commands.Bot(command_prefix='!', description='Acar inanılmaz havalı')
def is_dev():
    async def predicate(ctx):
        return ctx.author.id == 239316316111110155
    return commands.check(predicate)
def avgReturn(times):
    avgReturn.a=0
    times.sort()
    print(times)
    times=times[1:4]
    print(times)
    for x in times:
        avgReturn.a+=x
    return avgReturn.a/3
def gen_scramble2(length=random.randint(6,12)):
    sides = ["F", "U", "R"]
    modifiers = ["", "'", "2"]
    scramble = ""
    last = ''
    for i in range(length):
        current = random.choice(sides)
        while current == last: current = random.choice(sides)
        last = current
        scramble += current
        scramble += random.choice(modifiers)
        scramble += " "
    return scramble[:-1]
def gen_scramble3(length=random.randint(15,25)):
    sides = ["F", "U", "R", "D", "L", "B"]
    modifiers = ["", "'", "2"]
    scramble = ""
    last = ''
    for i in range(length):
        current = random.choice(sides)
        while current == last: current = random.choice(sides)
        last = current
        scramble += current
        scramble += random.choice(modifiers)
        scramble += " "
    return scramble[:-1]
def gen_scramble4(length=random.randint(38,45)):
    sides = ["F", "U", "R", "D", "L", "B"]
    modifiers = ["", "'", "2", "w", "w'", "w2"]
    scramble = ""
    last = ''
    for i in range(length):
        current = random.choice(sides)
        while current == last: current = random.choice(sides)
        last = current
        scramble += current
        scramble += random.choice(modifiers)
        scramble += " "
    return scramble[:-1]
@bot.command()
@is_dev()
async def eval(ctx):
    eval(ctx.messaage)
@bot.command()
@is_dev()
async def delete(ctx,num):
    await ctx.channel.delete_messages([discord.Object(id=num)])
@bot.command()
async def say(ctx, say):
    await ctx.channel.send(say)
    await ctx.message.delete()
@bot.command()
async def scr(ctx, numara, kaçMoruq=1):
    if ctx.author.id==344790059620499456:
        await ctx.channel.send("Acar 2x2 dunya rekoru kiracak o bi efsaneeee")
        if  numara[0]!="2":
            await ctx.channel.send("Yok sana 3x3 falan filan al sana bir 2x2 scramble'ı!")
        numara = "2"
    elif ctx.author.id==239316316111110155:
        await ctx.channel.send("wow değerli saygın developerım da gelmiş")
        numara=numara[0]
    else:
        numara=numara[0]
    for x in range(int(kaçMoruq)):
        await ctx.channel.send(globals()["gen_scramble"+numara]())
@bot.command()
async def comp(ctx, startOrPoint, zaman=None):
    nick = ctx.author.nick if ctx.author.nick!=None else ctx.author.name
    if startOrPoint=="başlat":
        comp.solve=0
        comp.büyüklük=zaman
        comp.zamanlar={}
        comp.inComp=[]
        comp.compStart=True
        comp.allFinished=True
        comp.a=0
        await ctx.channel.send("katılmak isteyenler !comp katıl yazsın!")
        comp.inComp.append(nick)
        comp.zamanlar[nick]=[]
    elif startOrPoint=="katıl" and comp.compStart==True:
        comp.zamanlar[nick]=[]
        await ctx.channel.send("comp a katıldın, "+nick)
        comp.inComp.append(nick)
    elif startOrPoint=="debug" or startOrPoint=="next" and comp.allFinished==True:
        await ctx.channel.send("scramble: "+globals()["gen_scramble"+comp.büyüklük]())
        comp.allFinished=False
    elif startOrPoint=="zaman":
        comp.zamanlar[nick].append(float(zaman))
        comp.a += 1
        if comp.a == len(comp.inComp):
            comp.allFinished=True
            comp.a=0
            comp.solve+=1
            await ctx.channel.send("herkes bitirdi! 2. tura geçmek için !comp next yazın.")
    if comp.solve==5:
        a=0
        y={}
        for x in comp.zamanlar:
            print(comp.zamanlar[x])
            y[str(a)]=avgReturn(comp.zamanlar[x])
            comp.zamanlar[x].append("Avg5("+str(avgReturn(comp.zamanlar[x]))+")")
            print(y)
            a+=1
        await ctx.send(comp.zamanlar)
        comp.solve=0
        comp.zamanlar={}
        comp.inComp=[]
        comp.compStart=False
    print(comp.inComp)
    print(comp.zamanlar)
bot.run(os.environ['BOT_TOKEN'])
