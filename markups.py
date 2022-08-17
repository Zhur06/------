from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import commands

btnMain = KeyboardButton(commands.mainMenu)

# Main Menu
btnPlay_song = KeyboardButton(commands.play_song)
btnSong_text = KeyboardButton(commands.song_text)
btnOther = KeyboardButton(commands.otherMenu)
btnStop = KeyboardButton(commands.stop_messaging)
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPlay_song, btnStop, btnSong_text, btnOther)

# Other Menu
btnInfo = KeyboardButton(commands.info)
btnConfigs = KeyboardButton(commands.configs)
btnCommandsInfo = KeyboardButton(commands.commandsInfoMenu)
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnConfigs, btnCommandsInfo, btnMain)

# Config Menu
btnEasyMode = KeyboardButton(commands.easyMode)
btnChangeDelay = KeyboardButton(commands.change_delay)
configMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnEasyMode, btnChangeDelay, btnMain)

# Commands Info Menu 
btnSong_textInfo = KeyboardButton(commands.song_text + '?')
btnEasyModeInfo = KeyboardButton(commands.easyMode + '?')
commandsInfoMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnSong_textInfo, btnEasyModeInfo, btnMain)