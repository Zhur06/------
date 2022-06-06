from pyparsing import Each
import config
import logging
import main
import markups as nav
import commands
import random

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# Тестирование бота
# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

selected_song = ''
easyMode = True

@dp.message_handler(commands = ['start'])
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветствую, {0.first_name}'.format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler(commands = ['song_text'])
async def song_text(message: types.Message):
    try:
        if message.get_args() != '':
            await message.answer(main.get_song_info_1(message.get_args()) + '\n' + main.get_song_info_2(message.get_args()))
            await message.answer(main.get_song(message.get_args()))
        else:
            await message.answer(main.get_song_info_1(selected_song) + '\n' + main.get_song_info_2(selected_song))
            await message.answer(main.get_song(selected_song))
    except AttributeError:
        await message.reply('Такой песни не найдено :(')

@dp.message_handler()
async def echo(message: types.Message):
    global easyMode
    global selected_song
    # Навигация в меню
    if message.text == commands.mainMenu:
        await bot.send_message(message.from_user.id, random.choice(commands.Messages), reply_markup = nav.mainMenu)

    elif message.text == commands.otherMenu:
        await bot.send_message(message.from_user.id, random.choice(commands.Messages), reply_markup = nav.otherMenu)
    
    elif message.text == commands.configs:
        await bot.send_message(message.from_user.id, 'Ваши настройки: ', reply_markup = nav.configMenu)
        replyText = 'Простой режим: '
        if easyMode:
            replyText += 'Включён'
        else:
            replyText += 'Выключен'
        await message.answer(replyText)

    elif message.text == commands.commandsInfoMenu:
        await bot.send_message(message.from_user.id, 'Для получения справки по коммандам выберите соответствующую на клавиатуре', reply_markup = nav.commandsInfoMenu)

    # Комманды бота
    elif message.text == commands.song_text:
        if easyMode:
            await message.answer('Напишите название песни а затем /song_text')
        else:
            try:
                await message.answer(main.get_song_info_1(selected_song) + '\n' + main.get_song_info_2(selected_song))
                await message.answer(main.get_song(selected_song))
            except AttributeError:
                await message.reply('Такой песни не найдено :(')

    elif message.text == commands.easyMode:
        await message.answer(random.choice(commands.Messages))
        easyMode = not easyMode

    # Комманды справки
    elif message.text == commands.song_text + '?':
        await message.answer('Отправляет сводку по песне (полное название, автора) и её текст с аккордами для гитары')

    elif message.text == commands.easyMode + '?':
        await message.answer('Простой режим, отвечает за реакции бота: поясняет ли бот что нужно сделать при использовании комманд (Простой режим включён) или просто выполняет их со стандартными настройками (Простой режим выключен)')

    # Обработчик всех сообщений
    else:
        selected_song = message.text

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates='True')