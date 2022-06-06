from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import commands

btnMain = KeyboardButton(commands.mainMenu)

# Main Menu
btnSong_text = KeyboardButton(commands.song_text)
btnOther = KeyboardButton(commands.otherMenu)
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSong_text, btnOther)

# Other Menu
btnInfo = KeyboardButton(commands.info)
btnConfigs = KeyboardButton(commands.configs)
btnCommandsInfo = KeyboardButton(commands.commandsInfoMenu)
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnConfigs, btnCommandsInfo, btnMain)

# Config Menu
btnEasyMode = KeyboardButton(commands.easyMode)
configMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnEasyMode, btnMain)

# Commands Info Menu 
btnSong_textInfo = KeyboardButton(commands.song_text + '?')
btnEasyModeInfo = KeyboardButton(commands.easyMode + '?')
commandsInfoMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSong_textInfo, btnEasyModeInfo, btnMain)