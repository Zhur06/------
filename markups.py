from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import commands

btnMain = KeyboardButton(commands.mainMenu)

# MainMenu
btnSong_text = KeyboardButton(commands.song_text)
btnOther = KeyboardButton(commands.otherMenu)
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSong_text, btnOther)

# Other Meny
btnInfo = KeyboardButton(commands.info)
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnMain)