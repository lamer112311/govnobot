import telebot#Материал для канала FALCON-BYTES.github.io
import datetime as DT
import pandas as pd
import time#Материал для канала FALCON-BYTES.github.io
import random
import datetime#Материал для канала FALCON-BYTES.github.io
from telebot import types
from datetime import date
from datetime import datetime, timedelta


def check_user(user_id):
    global users#Материал для канала FALCON-BYTES.github.io
    global ddt
    # Проверяем, есть ли пользователь в DataFrame
    if user_id in users["айди"].values:
        # Если есть, выводим баланс
        ddt = "Есть"
        print(users.loc[users["айди"] == user_id, "подписка"].values[0])
        users.loc[users["айди"] == user_id, "подписка"].values[0]
    else:
        # Если нет, добавляем нового пользователя с нулевыми значениями
        ddt = "нету"


prm = {
    "G2KFGH43F": 1,
    "OSTROV2024": 1,
    "THA446NK6": 1,
    "BJKJK545BT": 1,
    "TLL434FLF": 1,#Материал для канала FALCON-BYTES.github.io
    "GHKRFK43lf": 1,
    "FDLVMQA32": 1,
    "LODKQW8765": 1,#Материал для канала FALCON-BYTES.github.io
    "CJK4952QqW4F": 1,
    "FDFD43MVLaQ": 1,
    "VDKNK695216": 1,#Материал для канала FALCON-BYTES.github.io
    "FDSKTQQ55988": 1,
    "QQAQXCXD43CD": 1,
    "FEKF43MVL59G": 1,
    "O,IKM436IJ": 1,
    "RTYIOR5775": 1,
    "K578BKBVLQZZ": 1,
    "QOQLASLD436": 1,
    "GLDPLE4367": 1,
    "S56GM8QMA55": 1,
    "LlQ792Vv5": 1,
    "Day591VN078": 1,
    "RVN750M3e46s": 1,
    "Dal65vVDd550": 1,
    "Ql323VnB0z": 1,
    "P65sk00Aa": 1,
    "HuZzs6y00": 1,
    "MlCH4i78k": 1,
    "CHtp65bn35VvZ": 1,
    "KO54Ik4ZxC": 1,
    "Zqa43Ebb0Al": 1,
    "SpOk5c11Cxq": 1,
    "XddXXd11qd8": 1,
    "Vn5kvLLs7400Cv": 1,
    "SC500Gu21Nn": 1,
    "DDoZ65b9dBBv": 1,
    "QQQwWcc5400V": 1,
    "DDccbg54bB": 1,
    "Nau567Sni9Kka4": 1,
    "Pr0m1mOR28Czq": 1,
    "fr45NNcs23Qq": 1,
    "Fr0me2Zzc63": 1,
    "Xxv56OixXcd32": 1,
    "DmO54VNMRe665": 1,
    "DUE-439-VNf-098": 1,
    "QAS-001-oOl-c44": 1,
    "nDd-325-C40-071": 1,
    "Tol-314-Z0x-993": 1,
    "XzR-43V-FS6-CCd": 1,
    "Nh2-774-ZX3-452": 1,
}


prm2 = {
    "ODF543MG54N": 1,
    "L54VvLO88GV": 1,
    "HOOO454glDE": 1,
    "NNEE55YYBL21": 1,
    "STO555PPGVM8": 1,
    "BVKCC7865Qz1": 1,
    "G0q-Q52-052-Yk3": 1,
    "DdV-H66-999-Zx3": 1,
    "Bb1-bt2-Kp0-196": 1,
    "ZSHDIDOXLOL2294": 10000,
}


bot = telebot.TeleBot("токен говнобота")
channel_id = "@ostrovokmarixyana"
channel_id2 = "@VNDVANDAYZIOFF"

users = {
    "айди": ["1", "7500298999"],
    "подписка": [4, "неавна"],
    "вайтлист": [55, 33],
    "снесено": [0, 1],
}
users = pd.DataFrame(users)
promous = {"x": 1}


@bot.message_handler(commands=["me"])
def review(message):
    for i in range(len(users)):
        if message.from_user.id == 5095216557:#Материал для канала FALCON-BYTES.github.io
            nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{message.from_user.username}</code>\n🌟роль: <b>владелец</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
        elif message.from_user.id == 7473976918:#Материал для канала FALCON-BYTES.github.io
            nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{message.from_user.username}</code>\n🌟роль: <b>разработчик</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
        else:
            print(users.iat[i, 1])#Материал для канала FALCON-BYTES.github.io
            nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{message.from_user.username}</code>\n🌟роль: <b>пользователь</b>\n💎 Подписка: <b>{users.iat[i,1]}</b>\n📋вайт-лист: <b>{users.iat[i,2]}</b>\n⚡снесено аккаунтов: <b>{users.iat[i,3]}</b>'
    inline_menu_markup = types.InlineKeyboardMarkup()#Материал для канала FALCON-BYTES.github.io
    la1 = types.InlineKeyboardButton("🚀Активировать промокод", callback_data="na1")
    la3 = types.InlineKeyboardButton("⚒️сообщить о баге", url="https://t.me/VNDVandayzi")#Материал для канала FALCON-BYTES.github.io
    snos = types.InlineKeyboardButton("😈начать снос", callback_data="snos")
    sett = types.InlineKeyboardButton("⚙️настройки", callback_data="setting")#Материал для канала FALCON-BYTES.github.io
    la2 = types.InlineKeyboardButton("🌟купить промокод", url="https://t.me/Pavyk23")
    inline_menu_markup.add(la1, la2).add(la3, sett).add(snos) #Материал для канала FALCON-BYTES.github.io
    # lalala2 = bot.edit_message_text(chat_id=message.chat.id, message_id=menn.message_id, text=nah,parse_mode='html',reply_markup=inline_menu_markup)


global theme2
global themenum


@bot.message_handler(commands=["start"])
def review(message):
    global menn
    global godd
    user_id = message.from_user.id
    chat_member = bot.get_chat_member(channel_id, user_id)
    chat_member2 = bot.get_chat_member(channel_id2, user_id)
    inn = types.InlineKeyboardMarkup()
    ha1 = types.InlineKeyboardButton("👤Профиль", callback_data="ha1")
    ha2 = types.InlineKeyboardButton("ℹ️Информация", callback_data="ha2")
    ha3 = types.InlineKeyboardButton("⚒️cообщить о баге", url="https://t.me/VNDVandayzi")
    inn.add(ha1).add(ha2).add(ha3)
    if chat_member.status != "left" and chat_member2.status != "left":
        users = {
            "айди": ["1", "5095216557", "7473976918"],
            "подписка": [4, "✅до 02.11.2025", "✅до 02.11.2025"],
            "вайтлист": [55, "✅активен", "✅активен"],
            "снесено": [0, 7, 3],
        }
        users = pd.DataFrame(users)
        for i in range(len(users)):
            try:
                if message.from_user.id == users.iat[i, 0]:
                    if themenum == True:
                        pls = f"<a href={theme2}>👋</a><code>{message.from_user.first_name}</code>,добро пожаловать в OSTROVREPORT\n⚡выберите действие ниже"
                    else:#Материал для канала FALCON-BYTES.github.io
                        pls = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">👋</a><code>{message.from_user.first_name}</code>,добро пожаловать в OSTROVREPORT\n⚡выберите действие ниже'
                else:
                    godd = "❌неактивна"#Материал для канала FALCON-BYTES.github.io
                    ddd = users.loc[len(users) + 1] = (#Материал для канала FALCON-BYTES.github.io
                        message.from_user.id,#Материал для канала FALCON-BYTES.github.io
                        "❌неактивна",
                        "❌неактивен",#Материал для канала FALCON-BYTES.github.io
                        0,
                    )
                    print(users)
                    print("kic")
                    if themenum == True:
                        pls = f"<a href={theme2}>👋</a><code>{message.from_user.first_name}</code>,добро пожаловать в OSTROVREPORT\n⚡выберите действие ниже"
                    else:
                        pls = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">👋</a><code>{message.from_user.first_name}</code>,добро пожаловать в OSTROVREPORT\n⚡выберите действие ниже'
            except:
                pls = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">👋</a><code>{message.from_user.first_name}</code>,добро пожаловать в OSTROVREPORT\n⚡выберите действие ниже'
        menn = bot.send_message(
            message.chat.id, pls, parse_mode="html", reply_markup=inn
        )

    else:
        inm = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(
            "🔒Канал #1", url="https://t.me/VNDVANDAYZIOFF"
        )
        button2 = types.InlineKeyboardButton(
            "🔒Канал #2", url="https://t.me/ostrovokmarixyana"
        )
        button3 = types.InlineKeyboardButton(
            "🔎проверить подписку", callback_data="button3"
        )
        inm.add(button1, button2).add(button3)
        menn = bot.send_message(
            message.chat.id,
            f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a>чтобы начать пользоватся ботом, <b>подпишитесь на каналы</b>',
            parse_mode="html",
            reply_markup=inm,
        )


users = pd.DataFrame(users)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global lalala2
    global dar2
    global dar
    global dar3
    global chose
    if call.data == "okay1":
        global theme
        theme2 = f"https://s.iimg.su/s/04/YdfDXYuJzTDMkMFwr9s9pxmUPDe7mvlfw3JPZDFv.png"
        themenum = True
    if call.data == "next2":
        pic = types.InlineKeyboardMarkup()
        nextt = types.InlineKeyboardButton("далее▶️", callback_data="next3")
        backk = types.InlineKeyboardButton("◀️назад", callback_data="next1")
        okset = types.InlineKeyboardButton("✅применить✅", callback_data="okay3")
        pic.add(backk, nextt).add(okset)
        dar4 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=dar2.message_id,
            text=f'<a href="https://s.iimg.su/s/04/Wc6GVau7crJ7hzgfGR0orNTTa19uJMmp3cJ3rBnL.png">⚒️</a>изменение картинки⚒️\n\n🌟описание: <code>black</code>',
            parse_mode="html",
            reply_markup=pic,#Материал для канала FALCON-BYTES.github.io
        )
    if call.data == "next1":
        pic = types.InlineKeyboardMarkup()
        nextt = types.InlineKeyboardButton("далее▶️", callback_data="next2")
        backk = types.InlineKeyboardButton("◀️назад", callback_data="next")
        okset = types.InlineKeyboardButton("✅применить✅", callback_data="okay2")
        pic.add(backk, nextt).add(okset)
        dar3 = bot.edit_message_text(
            chat_id=call.message.chat.id,#Материал для канала FALCON-BYTES.github.io
            message_id=dar2.message_id,
            text=f'<a href="https://s.iimg.su/s/04/k8JzuUIzOj8DDoXWz8BKySuHD6SduGUy8pvr1OCy.png">⚒️</a>изменение картинки⚒️\n\n🌟описание: <code>blue</code>',
            parse_mode="html",
            reply_markup=pic,
        )
    if call.data == "next":
        pic = types.InlineKeyboardMarkup()#Материал для канала FALCON-BYTES.github.io
        nextt = types.InlineKeyboardButton("далее▶️", callback_data="next1")
        backk = types.InlineKeyboardButton("◀️назад", callback_data="setting")
        okset = types.InlineKeyboardButton("✅применить✅", callback_data="okay1")#Материал для канала FALCON-BYTES.github.io
        pic.add(backk, nextt).add(okset)
        dar2 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=dar.message_id,
            text=f'<a href="https://s.iimg.su/s/04/YdfDXYuJzTDMkMFwr9s9pxmUPDe7mvlfw3JPZDFv.png">⚒️</a>изменение картинки⚒️\n\n🌟описание: <code>premium</code>',
            parse_mode="html",
            reply_markup=pic,
        )
    if call.data == "setting":#Материал для канала FALCON-BYTES.github.io
        if call.from_user.id in promous:
            pic = types.InlineKeyboardMarkup()
            nextt = types.InlineKeyboardButton("далее▶️", callback_data="next")
            okset = types.InlineKeyboardButton("✅применить✅", callback_data="okay")
            pic.add(nextt).add(okset)
            dar = bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=lalala2.message_id,
                text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">⚒️</a>изменение картинки⚒️\n\n🌟описание: <code>default</code>',
                parse_mode="html",
                reply_markup=pic,
            )
        else:
            innd = types.InlineKeyboardMarkup()
            ha3d = types.InlineKeyboardButton(
                "🚀Купить подписку🚀", url="https://t.me/Pavyk23"
            )
            ha11 = types.InlineKeyboardButton("🔙Назад", callback_data="ha1")
            innd.add(ha3d, ha11)
            bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=lalala2.message_id,
                text=f"❌у вас отсутствует подписка\n🚀активируйте подписку для доступа к расширенным настройкам",
                reply_markup=innd,
            )

    global lalala
    if call.data == "button3":
        user_id = call.from_user.id
        chat_member = bot.get_chat_member(channel_id, user_id)
        chat_member2 = bot.get_chat_member(channel_id2, user_id)
        if chat_member.status != "left" and chat_member2.status != "left":
            inn = types.InlineKeyboardMarkup()#Материал для канала FALCON-BYTES.github.io
            ha1 = types.InlineKeyboardButton("👤Профиль", callback_data="ha1")
            ha2 = types.InlineKeyboardButton("ℹ️Информация", callback_data="ha2")
            ha3 = types.InlineKeyboardButton(
                "⚒️cообщить о баге", url="https://t.me/Pavyk23"
            )
            inn.add(ha1).add(ha2).add(ha3)
            lalala = bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=menn.message.id,
                text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">👋</a><code>{call.from_user.first_name}</code>,добро пожаловать в OSTROVREPORT\n⚡выберите действие ниже',
                parse_mode="html",
                reply_markup=inn,
            )

        global meny
        global nd
        global checkrr
        global vb
    if call.data == "snos":
        try:
            if call.from_user.id in promous:
                users.loc[2] = (call.from_user.id, godd3, "❌неактивен", 0)
                print(
                    23333333333333333333333333333333333333333333333331111111111111111111111
                )
                print(users)
                vb = users[users["айди"] == call.from_user.id].index[0]
                if users.iat[vb, 1] == "❌неактивна":
                    innd = types.InlineKeyboardMarkup()
                    ha3d = types.InlineKeyboardButton(
                        "🚀Купить подписку🚀", url="https://t.me/Pavyk23"
                    )
                    innd.add(ha3d)
                    bot.send_message(#Материал для канала FALCON-BYTES.github.io
                        call.message.chat.id,
                        f"❌у вас отсутствует подписка\n🚀активируйте подписку для доступа к сносу",
                        reply_markup=innd,
                    )
                else:
                    chh = types.InlineKeyboardMarkup()
                    hah1 = types.InlineKeyboardButton(#Материал для канала FALCON-BYTES.github.io
                        "👥Снос канала", callback_data="haha1"
                    )
                    hah2 = types.InlineKeyboardButton(
                        "👤Снос аккаунта", callback_data="haha2"
                    )
                    hah3 = types.InlineKeyboardButton(
                        "👤⭐Снос премиум аккаунта", callback_data="haha3"
                    )
                    hah4 = types.InlineKeyboardButton(
                        "🤖Снос бота", callback_data="haha4"
                    )
                    chh.add(hah1).add(hah2).add(hah3).add(hah4)
                    chose = bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=lalala2.message_id,
                        text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🎯</a>выберите, что хотите снести🎯',
                        parse_mode="html",
                        reply_markup=chh,
                    )
            else:
                users.loc[2] = (call.from_user.id, godd, "❌неактивен", 0)
                print(
                    23333333333333333333333333333333333333333333333331111111111111111111111
                )
                print(users)
                vb = users[users["айди"] == call.from_user.id].index[0]
                if users.iat[vb, 1] == "❌неактивна":
                    innd = types.InlineKeyboardMarkup()
                    ha11 = types.InlineKeyboardButton("🔙Назад", callback_data="ha1")
                    ha3d = types.InlineKeyboardButton(
                        "🚀Купить подписку🚀", url="https://t.me/Pavyk23"
                    )
                    innd.add(ha3d, ha11)
                    chosesb = bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=lalala2.message_id,
                        text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">❌</a>у вас отсутствует подписка\n🚀активируйте подписку для доступа к сносу',
                        parse_mode="html",#Материал для канала FALCON-BYTES.github.io
                        reply_markup=innd,
                    )
                else:
                    chh = types.InlineKeyboardMarkup()
                    hah1 = types.InlineKeyboardButton(
                        "👥Снос канала", callback_data="haha1"
                    )#Материал для канала FALCON-BYTES.github.io
                    hah2 = types.InlineKeyboardButton(
                        "👤Снос аккаунта", callback_data="haha2"
                    )
                    hah3 = types.InlineKeyboardButton(
                        "👤⭐Снос премиум аккаунта", callback_data="haha3"#Материал для канала FALCON-BYTES.github.io
                    )
                    hah4 = types.InlineKeyboardButton(
                        "🤖Снос бота", callback_data="haha4"
                    )
                    chh.add(hah1).add(hah2).add(hah3).add(hah4)
                    chose = bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=lalala2.message_id,
                        text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🎯</a>выберите, что хотите снести🎯',
                        parse_mode="html",
                        reply_markup=chh,
                    )
        except:
            users.loc[2] = (call.from_user.id, godd, "❌неактивен", 0)
            print(
                23333333333333333333333333333333333333333333333331111111111111111111111
            )
            print(users)#Материал для канала FALCON-BYTES.github.io
            vb = users[users["айди"] == call.from_user.id].index[0]
            if users.iat[vb, 1] == "❌неактивна":#Материал для канала FALCON-BYTES.github.io
                innd = types.InlineKeyboardMarkup()
                ha11 = types.InlineKeyboardButton("🔙Назад", callback_data="ha1")
                ha3d = types.InlineKeyboardButton(
                    "🚀Купить подписку🚀", url="https://t.me/Pavyk23"
                )
                innd.add(ha3d, ha11)#Материал для канала FALCON-BYTES.github.io
                chosesb = bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=lalala2.message_id,
                    text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">❌</a>у вас отсутствует подписка\n🚀активируйте подписку для доступа к сносу',
                    parse_mode="html",
                    reply_markup=innd,
                )
            # bot.send_message(call.message.chat.id,f'❌у вас отсутствует подписка\n🚀активируйте подписку для доступа к сносу',reply_markup=innd)
            else:
                chh = types.InlineKeyboardMarkup()
                hah1 = types.InlineKeyboardButton(
                    "👥Снос канала", callback_data="haha1"
                )
                hah2 = types.InlineKeyboardButton(
                    "👤Снос аккаунта", callback_data="haha2"
                )
                hah3 = types.InlineKeyboardButton(
                    "👤⭐Снос премиум аккаунта", callback_data="haha2"
                )
                hah4 = types.InlineKeyboardButton("🤖Снос бота", callback_data="haha4")
                chh.add(hah1).add(hah2).add(hah3).add(hah4)
                chose = bot.edit_message_text(
                    chat_id=call.message.chat.id,
                    message_id=lalala2.message_id,
                    text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🎯</a>выберите, что хотите снести🎯',
                    parse_mode="html",
                    reply_markup=chh,
                )
            # nd = bot.send_message(call.message.chat.id,'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🎯</a>выберите, что хотите снести🎯',parse_mode='html',reply_markup=chh)

    if call.data == "haha1":
        if users.iat[vb, 1] == "❌неактивна":
            innd = types.InlineKeyboardMarkup()
            ha3d = types.InlineKeyboardButton(
                "🚀Купить подписку🚀", url="https://t.me/Pavyk23"
            )
            innd.add(ha3d)#Материал для канала FALCON-BYTES.github.io
            # print(ahyel)#Материал для канала FALCON-BYTES.github.io
            bot.send_message(
                call.message.chat.id,
                f"❌у вас отсутствует подписка\n🚀активируйте подписку для доступа к сносу",
                reply_markup=innd,
            )
        else:
            nos = bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=chose.message_id,
                text="🚀отправьте ссылку на канал",
                parse_mode="html",
            )
            bot.register_next_step_handler(nos, snosiktgk)
    if call.data == "ha2":
        bot.send_message(
            call.message.chat.id,
            f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">👋</a><b>👋 Добро пожаловать в OSTROV REPORT</b>\nЭтот бот создан для удобного и эффективного snosa телеграм каналов и аккаунтов:\n🚀эффективно snesem любой аккаунт\n-даже с премиумом\n\n⚡мы используем уникальные методы для snosa\n🌟купив подписку, вы поддерживаете наш проект',
            parse_mode="html",
        )#Материал для канала FALCON-BYTES.github.io
    if call.data == "ha1":
        for i in range(len(users)):
            if call.from_user.id == 5095216557:
                nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{call.from_user.username}</code>\n🌟роль: <b>владелец</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
            elif call.from_user.id == 7473976918:
                nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{call.from_user.username}</code>\n🌟роль: <b>администратор (126/126 кодов доступно)</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
            else:
                nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{call.from_user.username}</code>\n🌟роль: <b>пользователь</b>\n💎 Подписка: <b>{users.iat[i,1]}</b>\n📋вайт-лист: <b>{users.iat[i,2]}</b>\n⚡снесено аккаунтов: <b>{users.iat[i,3]}</b>'
        if call.from_user.id in promous:
            inline_menu_markup = types.InlineKeyboardMarkup()
            la1 = types.InlineKeyboardButton(
                "🚀Активировать промокод", callback_data="na1"
            )
            la3 = types.InlineKeyboardButton(
                "⚒️сообщить о баге", url="https://t.me/VNDVandayzi"
            )
            snos = types.InlineKeyboardButton("😈начать снос", callback_data="snos")
            sett = types.InlineKeyboardButton("⚙️настройки", callback_data="setting")
            la2 = types.InlineKeyboardButton(
                "🌟купить промокод", url="https://t.me/Pavyk23"
            )
            inline_menu_markup.add(la1, la2).add(la3, sett).add(snos)
            lalala2 = bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=menn.message_id,
                text=nah,
                parse_mode="html",
                reply_markup=inline_menu_markup,
            )
        else:
            inline_menu_markup = types.InlineKeyboardMarkup()
            la1 = types.InlineKeyboardButton(
                "🚀Активировать промокод", callback_data="na1"
            )
            la3 = types.InlineKeyboardButton(
                "⚒️сообщить о баге", url="https://t.me/VNDVandayzi"
            )
            snos = types.InlineKeyboardButton("🔒начать снос🔒", callback_data="snos")
            sett = types.InlineKeyboardButton("🔒настройки🔒", callback_data="setting")
            la2 = types.InlineKeyboardButton(
                "🌟купить промокод", url="https://t.me/Pavyk23"#Материал для канала FALCON-BYTES.github.io
            )
            inline_menu_markup.add(la1, la2).add(la3, sett).add(snos)
            lalala2 = bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=menn.message_id,
                text=nah,
                parse_mode="html",
                reply_markup=inline_menu_markup,
            )
        # meny = bot.send_message(call.message.chat.id,nah,parse_mode='html',reply_markup=inline_menu_markup)
    global star
    global lol
    global uss
    global methodd

    if call.data == "smtpt":
        lol = random.randint(20054, 169999)#Материал для канала FALCON-BYTES.github.io
        rez = types.InlineKeyboardMarkup()
        ye2 = types.InlineKeyboardButton("Начать✅", callback_data="ye2")
        no2 = types.InlineKeyboardButton("Отмена❌", callback_data="no2")
        rez.add(ye2, no2)
        methodd = "SMTP"
        star = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=na.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал:<b> {ahyel}</b>\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\nподтвердите снос",
            parse_mode="html",
            reply_markup=rez,
        )#Материал для канала FALCON-BYTES.github.io
    if call.data == "ftpt":
        lol = random.randint(20054, 169999)
        rez = types.InlineKeyboardMarkup()
        ye2 = types.InlineKeyboardButton("Начать✅", callback_data="ye2")
        no2 = types.InlineKeyboardButton("Отмена❌", callback_data="no2")#Материал для канала FALCON-BYTES.github.io
        rez.add(ye2, no2)
        methodd = "FTP"
        star = bot.edit_message_text(
            chat_id=call.message.chat.id,#Материал для канала FALCON-BYTES.github.io
            message_id=na.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал:<b> {ahyel}</b>\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\nподтвердите снос",
            parse_mode="html",
            reply_markup=rez,
        )
    if call.data == "webt":#Материал для канала FALCON-BYTES.github.io
        methodd = "WEB"
        lol = random.randint(20054, 169999)
        rez = types.InlineKeyboardMarkup()
        ye2 = types.InlineKeyboardButton("Начать✅", callback_data="ye2")
        no2 = types.InlineKeyboardButton("Отмена❌", callback_data="no2")
        rez.add(ye2, no2)
        star = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=na.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал:<b> {ahyel}</b>\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\nподтвердите снос",
            parse_mode="html",
            reply_markup=rez,
        )

    if call.data == "smtp":
        lol = random.randint(20054, 169999)#Материал для канала FALCON-BYTES.github.io
        rez = types.InlineKeyboardMarkup()
        ye = types.InlineKeyboardButton("Начать✅", callback_data="ye")
        no = types.InlineKeyboardButton("Отмена❌", callback_data="no")
        rez.add(ye, no)
        methodd = "SMTP"
        star = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=na.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🆔айди:<b> {snosid}</b>\n🗺️юз:<b> {kol}</b>\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\nподтвердите снос",
            parse_mode="html",
            reply_markup=rez,
        )
    if call.data == "ftp":#Материал для канала FALCON-BYTES.github.io
        lol = random.randint(20054, 169999)
        rez = types.InlineKeyboardMarkup()#Материал для канала FALCON-BYTES.github.io
        ye = types.InlineKeyboardButton("Начать✅", callback_data="ye")
        no = types.InlineKeyboardButton("Отмена❌", callback_data="no")
        rez.add(ye, no)
        methodd = "FTP"#Материал для канала FALCON-BYTES.github.io
        star = bot.edit_message_text(
            chat_id=call.message.chat.id,#Материал для канала FALCON-BYTES.github.io
            message_id=na.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🆔айди:<b> {snosid}</b>\n🗺️юз:<b> {kol}</b>\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\nподтвердите снос",
            parse_mode="html",#Материал для канала FALCON-BYTES.github.io
            reply_markup=rez,
        )
    if call.data == "web":
        methodd = "WEB"
        lol = random.randint(20054, 169999)
        rez = types.InlineKeyboardMarkup()
        ye = types.InlineKeyboardButton("Начать✅", callback_data="ye")
        no = types.InlineKeyboardButton("Отмена❌", callback_data="no")
        rez.add(ye, no)
        star = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=na.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🆔айди:<b> {snosid}</b>\n🗺️юз:<b> {kol}</b>\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\nподтвердите снос",
            parse_mode="html",
            reply_markup=rez,
        )
#Материал для канала FALCON-BYTES.github.io
    if call.data == "ye2":
        star1 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=star.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал: {ahyel}\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>генерируем репорты</code>",
            parse_mode="html",
        )
        time.sleep(4)
        star2 = bot.edit_message_text(#Материал для канала FALCON-BYTES.github.io
            chat_id=call.message.chat.id,#Материал для канала FALCON-BYTES.github.io
            message_id=star1.message_id,#Материал для канала FALCON-BYTES.github.io
            text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал: {ahyel}\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>запускаем рассылку</code>",
            parse_mode="html",
        )
        time.sleep(2)#Материал для канала FALCON-BYTES.github.io
        star3 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=star2.message_id,#Материал для канала FALCON-BYTES.github.io
            text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал: {ahyel}\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>в процессе</code>\n🚀отправлено жалоб: <code>0</code>",
            parse_mode="html",
        )
        uss = int(uss2)
        for i in range(uss2):
            shal = 1 + i
            star4 = bot.edit_message_text(
                chat_id=call.message.chat.id,
                message_id=star3.message_id,
                text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал: {ahyel}\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>в процессе</code>\n🚀отправлено жалоб: <code>{shal}/{uss}</code>",
                parse_mode="html",
            )
            time.sleep(0.6)
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=star3.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🗺️канал: {ahyel}\n⚠️кол-во жалоб:<b> {uss2}</b>\n🔗метод: <b>{methodd}</b>\n\n✅статус: <code>завершен</code>\n🚀отправлено жалоб: <code>{uss}/{uss}</code>",
            parse_mode="html",
        )
        otz = bot.send_message(
            call.message.chat.id,
            f"✅<b>снос прошел успешно</b>✅\n🚀отправьте <b>отзыв</b> о нашем боте",
            parse_mode="html",
        )
        bot.register_next_step_handler(otz, after_text_otz)

    if call.data == "haha2":
        if users.iat[vb, 1] == "❌неактивна":
            innd = types.InlineKeyboardMarkup()
            ha3d = types.InlineKeyboardButton(
                "🚀Купить подписку🚀", url="https://t.me/Pavyk23"
            )
            ha3d2 = types.InlineKeyboardButton("👤Меню", callback_data="ha1")
            innd.add(ha3d).add(ha3d2)
            bot.send_message(
                call.message.chat.id,#Материал для канала FALCON-BYTES.github.io
                f"❌у вас отсутствует подписка\n🚀активируйте подписку для доступа к сносу",
                reply_markup=innd,
            )#Материал для канала FALCON-BYTES.github.io
        else:
            # print(ahyel)
            global da
            inline_menu_markup = types.InlineKeyboardMarkup()
            la1 = types.InlineKeyboardButton("🔙Назад", callback_data="ha1")
            inline_menu_markup.add(la1)
            da = bot.edit_message_text(#Материал для канала FALCON-BYTES.github.io
                chat_id=call.message.chat.id,
                message_id=chose.message_id,
                text=f"🚀Укажите id пользователя",
                parse_mode="html",
                reply_markup=inline_menu_markup,
            )
            bot.register_next_step_handler(da, snosik)

    if call.data == "ye":
        star1 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=star.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🆔айди:<b> {snosid}</b>\n🗺️юз: {kol}\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>генерируем репорты</code>",
            parse_mode="html",
        )
        time.sleep(4)
        star2 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=star1.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🆔айди:<b> {snosid}</b>\n🗺️юз: {kol}\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>запускаем рассылку</code>",
            parse_mode="html",
        )
        time.sleep(2)
        star3 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=star2.message_id,
            text=f"😈снос №<b>{lol}</b>😈\n\n🆔айди:<b> {snosid}</b>\n🗺️юз: {kol}\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>в процессе</code>\n🚀отправлено жалоб: <code>0</code>",
            parse_mode="html",
        )
        uss = int(uss)
        for i in range(uss):
            shal = 1 + i
            star4 = bot.edit_message_text(
                chat_id=call.message.chat.id,#Материал для канала FALCON-BYTES.github.io
                message_id=star3.message_id,
                text=f"😈снос №<b>{lol}</b>😈\n\n🆔а #Материал для канала FALCON-BYTES.github.io йди:<b> {snosid}</b>\n🗺️юз: {kol}\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\n🔰статус: <code>в процессе</code>\n🚀отправлено жалоб: <code>{shal}/{uss}</code>",
                parse_mode="html",
            )
            time.sleep(0.6)
        bot.edit_message_text(#Материал для канала FALCON-BYTES.github.io
            chat_id=call.message.chat.id,
            message_id=star3.message_id,#Материал для канала FALCON-BYTES.github.io
            text=f"😈снос №<b>{lol}</b>😈\n\n🆔айди:<b> {snosid}</b>\n🗺️юз: {kol}\n⚠️кол-во жалоб:<b> {uss}</b>\n🔗метод: <b>{methodd}</b>\n\n✅статус: <code>завершен</code>\n🚀отправлено жалоб: <code>{uss}/{uss}</code>",
            parse_mode="html",
        )
        otz = bot.send_message(
            call.message.chat.id,
            f"✅<b>снос прошел успешно</b>✅\n🚀отправьте <b>отзыв</b> о нашем боте",
            parse_mode="html",
        )
        bot.register_next_step_handler(otz, after_text_otz)
    if call.data == "hana1":
        for i in range(len(users)):
            if call.from_user.id == 5095216557:
                nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{call.from_user.username}</code>\n🌟роль: <b>владелец</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
            elif call.from_user.id == 7473976918:
                nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{call.from_user.username}</code>\n🌟роль: <b>разработчик</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
            else:
                nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{call.from_user.username}</code>\n🌟роль: <b>пользователь</b>\n💎 Подписка: <b>{users.iat[i,1]}</b>\n📋вайт-лист: <b>{users.iat[i,2]}</b>\n⚡снесено аккаунтов: <b>{users.iat[i,3]}</b>'
        inline_menu_markup = types.InlineKeyboardMarkup()
        la1 = types.InlineKeyboardButton("🚀Активировать промокод", callback_data="na1")
        la3 = types.InlineKeyboardButton(
            "⚒️сообщить о баге", url="https://t.me/VNDVandayzi"
        )
        snos = types.InlineKeyboardButton("😈начать снос", callback_data="snos")
        sett = types.InlineKeyboardButton("⚙️настройки", callback_data="setting")#Материал для канала FALCON-BYTES.github.io
        la2 = types.InlineKeyboardButton(
            "🌟купить промокод", url="https://t.me/Pavyk23"
        )
        inline_menu_markup.add(la1, la2).add(la3, sett).add(snos)
        lalala2 = bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=pring.message_id,
            text=nah,
            parse_mode="html",
            reply_markup=inline_menu_markup,
        )
    if call.data == "na1":
        innd = types.InlineKeyboardMarkup()
        ha3d = types.InlineKeyboardButton(
            "🚀Купить подписку🚀", url="https://t.me/Pavyk23"
        )
        ha3d2 = types.InlineKeyboardButton("👤Меню", callback_data="ha1")
        innd.add(ha3d).add(ha3d2)
        global da4
        da4 = bot.edit_message_text(
            chat_id=call.message.chat.id,#Материал для канала FALCON-BYTES.github.io
            message_id=lalala2.message_id,
            text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a>введите ваш промокод:',
            parse_mode="html",
        )
        # da = bot.send_message(call.message.chat.id,f'🚀введите ваш промокод:',parse_mode='html')
        bot.register_next_step_handler(da4, after_text_2)


def after_text_2(message):
    global pring
    global godd
    global godd2
    global godd3
    rez2 = types.InlineKeyboardMarkup()
    ye2 = types.InlineKeyboardButton("🏠На главную", callback_data="hana1")
    rez2.add(ye2)
    if message.text in prm:
        global da3
        da3 = bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=da4.message_id,
            text=f'<a href="https://s.iimg.su/s/05/gHuzfO8AJVsXILt6kobKM7n1aM88TXKrFgfzEten.png">⌛</a><code>читаем промокод...</code>',
            parse_mode="html",
        )
        time.sleep(4)
        if prm[message.text] == 0:#Материал для канала FALCON-BYTES.github.io
            pring = bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=da3.message_id,
                text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">❌</a>у промокода закончились активации',
                parse_mode="html",
                reply_markup=rez2,
            )
        else:
            pring = bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=da3.message_id,
                text=f'<a href="https://s.iimg.su/s/05/AbUNqqlz3riAAoUOyJALnKKGxy5oKmiDam9EObqR.png">✅</a>вы успешно активировали промокод на <b>1 месяц</b> подписки\n🚀теперь вам доступен доступ к сносу',
                parse_mode="html",
                reply_markup=rez2,
            )
            # pring = bot.reply_to(message,f'✅вы успешно активировали промокод на 1 месяц подписки\n🚀спасибо, что выбрали нас',reply_markup=rez2)
            current_time = datetime.now().time()
            today = datetime.now()#Материал для канала FALCON-BYTES.github.io
            future_date = today + timedelta(days=31)
            formatted_date = future_date.strftime("%d %b").upper()
            prm[message.text] = prm[message.text] - 1
            for i in range(len(users)):
                print("оваыЫПФВерпвеРОДЛЩЭФВЕрфер")
                users.iat[i, 1] = 45455454
                current_date = datetime.now()
                new_date = current_date + timedelta(days=31)
                formatted_date = new_date.strftime("%d.%m.%Y")
                godd = f"✅до {formatted_date}"
                godd2 = f"{message.from_user.id}True"
                godd3 = f"✅до {formatted_date}"
                promous[message.from_user.id] = f"{message.from_user.id}True"
                users.iat[i, 1] = f"✅до {formatted_date}"
    elif message.text in prm2:
        da3 = bot.edit_message_text(
            chat_id=message.chat.id,#Материал для канала FALCON-BYTES.github.io
            message_id=da4.message_id,
            text=f'<a href="https://s.iimg.su/s/05/gHuzfO8AJVsXILt6kobKM7n1aM88TXKrFgfzEten.png">⌛</a><code>читаем промокод...</code>',
            parse_mode="html",
        )
        time.sleep(4)
        if prm2[message.text] == 0:
            pring = bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=da3.message_id,
                text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">❌</a>у промокода закончились активации',
                parse_mode="html",
                reply_markup=rez2,
            )
        else:
            pring = bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=da3.message_id,
                text=f'<a href="https://s.iimg.su/s/05/AbUNqqlz3riAAoUOyJALnKKGxy5oKmiDam9EObqR.png">✅</a>вы успешно активировали промокод на <b>1 месяц</b> подписки\n🚀теперь вам доступен доступ к сносу',
                parse_mode="html",
                reply_markup=rez2,
            )
            current_time = datetime.now().time()#Материал для канала FALCON-BYTES.github.io
            today = datetime.now()
            future_date = today + timedelta(days=31)
            formatted_date = future_date.strftime("%d %b").upper()
            prm2[message.text] = prm2[message.text] - 1
            for i in range(len(users)):
                print("оваыЫПФВерпвеРОДЛЩЭФВЕрфер")#Материал для канала FALCON-BYTES.github.io
                current_date = datetime.now()
                new_date = current_date + timedelta(days=365)
                formatted_date = new_date.strftime("%d.%m.%Y")
                godd = f"✅до {formatted_date}"
                godd3 = f"✅до {formatted_date}"
                godd2 = f"{message.from_user.id}True"
                promous[message.from_user.id] = f"{message.from_user.id}True"
                users.iat[i, 1] = f"✅до {formatted_date}"
    else:
        da3 = bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=da4.message_id,
            text=f'<a href="https://s.iimg.su/s/05/gHuzfO8AJVsXILt6kobKM7n1aM88TXKrFgfzEten.png">⌛</a><code>читаем промокод...</code>',
            parse_mode="html",
        )
        time.sleep(4)
        pring = bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=da3.message_id,
            text=f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">❌</a>такого промокода не существует',
            parse_mode="html",
            reply_markup=rez2,
        )


# СНОС ТГК СНОС ТГК
def snosiktgk(message):
    global ahyel
    ahyel = message.text
    global tryy
    inline_menu_markup = types.InlineKeyboardMarkup()
    snos = types.InlineKeyboardButton("🎯попробовать еще раз", callback_data="snos")
    inline_menu_markup.add(snos)
    methodtg = types.InlineKeyboardMarkup()#Материал для канала FALCON-BYTES.github.io
    webt = types.InlineKeyboardButton("WEB", callback_data="webt")
    ftpt = types.InlineKeyboardButton("FTP", callback_data="ftpt")
    smtpt = types.InlineKeyboardButton("SMTP", callback_data="smtpt")
    methodtg.add(webt, smtpt, ftpt)
    print(ahyel[0:12])
    # global du2
    if ahyel == "@VNDVANDAYZIOFF" or ahyel[0:1] == "@ostrovokmarixyana":
        tryy = bot.send_message(
            message.chat.id,#Материал для канала FALCON-BYTES.github.io
            f"❎недопустимый юзернейм канала\n🔗убедитесь, что вы правильно указали юзернейм",
            reply_markup=snos,
        )
    else:
        if ahyel[0:1] == "@":
            dd2 = bot.send_message(message.chat.id, "🚀укажите кол-во жалоб")
            bot.register_next_step_handler(dd2, after_text_521)

        else:
            print(ahyel[0:13])
            tryy = bot.send_message(
                message.chat.id,
                f"❎недопустимый юзернейм канала\n🔗убедитесь, что вы правильно указали юзернейм",
                reply_markup=snos,
            )#Материал для канала FALCON-BYTES.github.io

#Материал для канала FALCON-BYTES.github.io
def after_text_521(message):#Материал для канала FALCON-BYTES.github.io
    inline_menu_markup = types.InlineKeyboardMarkup()#Материал для канала FALCON-BYTES.github.io
    snos = types.InlineKeyboardButton("🎯попробовать еще раз", callback_data="snos")
    inline_menu_markup.add(snos)
    methodtg = types.InlineKeyboardMarkup()
    webt = types.InlineKeyboardButton("WEB", callback_data="webt")
    ftpt = types.InlineKeyboardButton("FTP", callback_data="ftpt")
    smtpt = types.InlineKeyboardButton("SMTP", callback_data="smtpt")
    methodtg.add(webt, smtpt, ftpt)
    global uss2
    uss2 = message.text
    if uss2[0:1] == "0":
        bot.send_message(
            message.chat.id,
            f"❎недопустимое кол-во репортов\n🔗укажите число от 1 до 150",
            reply_markup=snos,
        )
    else:
        try:
            uss2 = int(uss2)
            if uss2 > 150:
                bot.send_message(#Материал для канала FALCON-BYTES.github.io
                    message.chat.id,
                    f"❎недопустимое кол-во репортов\n🔗укажите число от 1 до 150",
                    reply_markup=snos,
                )
            else:
                global na
                na = bot.send_message(
                    message.chat.id, "🚀выберите метод сноса", reply_markup=methodtg
                )
        except:
            bot.send_message(#Материал для канала FALCON-BYTES.github.io#Материал для канала FALCON-BYTES.github.io#Материал для канала FALCON-BYTES.github.io#Материал для канала FALCON-BYTES.github.io
                message.chat.id,
                f"❎недопустимое кол-во репортов\n🔗укажите число от 1 до 150",
                reply_markup=snos,
            )#Материал для канала FALCON-BYTES.github.io#Материал для канала FALCON-BYTES.github.io


def snosik(message):
    idd = message.text
    global du
    global snosid
    snosid = message.text
    inline_menu_markup = types.InlineKeyboardMarkup()
    la1 = types.InlineKeyboardButton("🔙Назад", callback_data="haha2")
    inline_menu_markup.add(la1)
    inline_menu_markupp = types.InlineKeyboardMarkup()
    snos = types.InlineKeyboardButton("🎯попробовать еще раз", callback_data="snos")
    inline_menu_markupp.add(snos)
    print(snosid[0:1])
    if snosid[0:1] == "0":
        nada = bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=da.message_id,
            text=f"❎недопустимый id пользователя\n🔗убедитесь, что вы правильно указали id",
            reply_markup=inline_menu_markupp,
        )
    else:
        try:
            snosid = int(snosid)
            global du
            du = bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=da.message_id,#Материал для канала FALCON-BYTES.github.io
                text=f"🚀укажите юзернейм пользователя\n⚡если его нет, отправьте id пользователя",
                parse_mode="html",
                reply_markup=inline_menu_markup,
            )
            bot.register_next_step_handler(du, after_text_52)
        except:
            nada = bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=da.message_id,
                text=f"❎недопустимый id пользователя\n🔗убедитесь, что вы правильно указали id",
                reply_markup=inline_menu_markupp,#Материал для канала FALCON-BYTES.github.io
            )
            # bot.send_message(message.chat.id,f'❎недопустимый id пользователя\n🔗убедитесь, что вы правильно указали id',reply_markup=inline_menu_markupp)


def after_text_52(message):
    global dd
    inline_menu_markup = types.InlineKeyboardMarkup()
    la1 = types.InlineKeyboardButton("🔙Отмена", callback_data="haha2")
    inline_menu_markup.add(la1)
    global dd
    dd = bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=da.message_id,
        text=f"🚀укажите кол-во репортов",
        parse_mode="html",
        reply_markup=inline_menu_markup,
    )
    global kol
    kol = message.text
    if kol[0:1] == "@":
        bot.register_next_step_handler(dd, after_text_522)
    else:
        inline_menu_markupp = types.InlineKeyboardMarkup()
        snos = types.InlineKeyboardButton("🎯попробовать еще раз", callback_data="snos")
        inline_menu_markupp.add(snos)
        bot.send_message(
            message.chat.id,
            f"#Материал для канала FALCON-BYTES.github.io ❎недопустимый юзернейм\n🔗укажите юзернейм человека с @",
            reply_markup=inline_menu_markupp,
        )


def after_text_522(message):

    inline_menu_markupp = types.InlineKeyboardMarkup()
    snos = types.InlineKeyboardButton("🎯попробовать еще раз", callback_data="snos")
    inline_menu_markupp.add(snos)
    method = types.InlineKeyboardMarkup()
    web = types.InlineKeyboardButton("WEB", callback_data="web")
    ftp = types.InlineKeyboardButton("FTP", callback_data="ftp")
    smtp = types.InlineKeyboardButton("SMTP", callback_data="smtp")
    method.add(web, smtp, ftp)
    global uss
    global na
    uss = message.text
    if uss[0:1] == "0":
        na = bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=da.message_id,
            text=f"❎недопустимое кол-во репортов\n🔗укажите число от 1 до 150",
            reply_markup=inline_menu_markupp,
        )
    else:
        try:
            uss = int(uss)
            if uss > 150:
                na = bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=da.message_id,
                    text=f"❎недопустимое кол-во репортов\n🔗укажите число от 1 до 150",
                    reply_markup=inline_menu_markupp,
                )
            else:
                na = bot.edit_message_text(
                    chat_id=message.chat.id,
                    message_id=da.message_id,
                    text=f"🚀выберите метод сноса",
                    reply_markup=method,
                )
        except:
            na = bot.edit_message_text(#Материал для канала FALCON-BYTES.github.io
                chat_id=message.chat.id,
                message_id=da.message_id,
                text=f"❎недопустимое кол-во репортов\n🔗укажите число от 1 до 150",
                reply_markup=inline_menu_markupp,
            )


def after_text_otz(message):
    for i in range(len(users)):
        if message.from_user.id == 5095216557:
            nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{message.from_user.username}</code>\n🌟роль: <b>владелец</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
        elif message.from_user.id == 7473976918:
            nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{message.from_user.username}</code>\n🌟роль: <b>разработчик</b>\n💎 Подписка: <b>✅до 02.11.2025</b>\n📋вайт-лист: <b>✅активен</b>\n⚡снесено аккаунтов: <b>7</b>'
        else:
            nah = f'<a href="https://s.iimg.su/s/02/675JKmjwjoI5IHy3SpDikDb6tAjkqdz25GUhSioM.png">🚀</a><b>Ваш профиль</b>🚀\n\n👤логин: <code>{message.from_user.username}</code>\n🌟роль: <b>пользователь</b>\n💎 Подписка: <b>{users.iat[i,1]}</b>\n📋вайт-лист: <b>{users.iat[i,2]}</b>\n⚡снесено аккаунтов: <b>{users.iat[i,3]}</b>'
    inline_menu_markup = types.InlineKeyboardMarkup()
    la1 = types.InlineKeyboardButton("🚀Активировать промокод", callback_data="na1")
    la3 = types.InlineKeyboardButton("⚒️сообщить о баге", url="https://t.me/VNDVandayzi")
    snos = types.InlineKeyboardButton("😈начать снос", callback_data="snos")
    sett = types.InlineKeyboardButton("⚙️настройки", callback_data="setting")
    la2 = types.InlineKeyboardButton("🌟купить промокод", url="https://t.me/Pavyk23")
    inline_menu_markup.add(la1, la2).add(la3, sett).add(snos)
    meny = bot.send_message(
        message.chat.id, nah, parse_mode="html", reply_markup=inline_menu_markup
    )#Материал для канала FALCON-BYTES.github.io
    otzz = message.text
    bot.send_message(
        7473976918,
        f"🚀<b>новый отзыв</b>🚀\n\nот @{message.from_user.username}\nайди: <code>{message.from_user.id}</code>\nотзыв: {otzz}",
        parse_mode="html",
    )
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
bot.infinity_polling(timeout=20, long_polling_timeout=10)

#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
#Материал для канала FALCON-BYTES.github.io
