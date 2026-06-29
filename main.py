import discord
from discord.ext import commands, tasks
from discord import app_commands

# إعدادات البوت
intents = discord.Intents.default()
intents.message_content = True  # ضروري لقراءة الرسائل
intents.members = True          # ضروري للتعامل مع أعضاء السيرفر

bot = commands.Bot(command_prefix="!", intents=intents)


# الذكر الذي سيتم إرساله كل 5 دقائق
@tasks.loop(minutes=5)
async def send_dhikr():
    # استبدل الرقم برقم الروم الخاص بك
    channel = bot.get_channel(1512425200778739732) 
    if channel:
        await channel.send("سبحان الله وبحمده، سبحان الله العظيم.")

@bot.event
async def on_ready():
    await bot.tree.sync() # مزامنة السلاش كوماندز
    send_dhikr.start()
    print(f"تم تسجيل الدخول كـ {bot.user}")

# مثال على سلاش كوماند
@bot.tree.command(name="ramadan", description="كم باقي على رمضان؟")
async def ramadan(interaction: discord.Interaction):
    await interaction.response.send_message("اللهم بلغنا رمضان!")

import os
# البوت سيقرأ التوكن من إعدادات الموقع وليس من الكود مباشرة
bot.run(os.environ['TOKEN'])


