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


@dp.message_handler(commands = ['start'])
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветствую, {0.first_name}'.format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler(commands = ['song_text'])
async def song_text(message: types.Message):
    try:
        await message.answer(main.get_song_info_1(message.get_args()) + '\n' + main.get_song_info_2(message.get_args()))
        await message.answer(main.get_song(message.get_args()))
    except AttributeError:
        await message.reply('Такой песни не найдено :(')

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == commands.mainMenu:
        await bot.send_message(message.from_user.id, random.choice(commands.Messages), reply_markup = nav.mainMenu)

    elif message.text == commands.otherMenu:
        await bot.send_message(message.from_user.id, random.choice(commands.Messages), reply_markup = nav.otherMenu)

    elif message.text == commands.song_text:
        await message.answer('Введите команду /song_text [Название песни]')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates='True')