from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message
from aiogram.utils import executor

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

################# на  старт в  консоль
#async def on_startup( ):
#    print('Бот  в  онлайн')

#**********************клиент********************
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):    
    try:
        await bot.send_message(message.from_user.id, 'поехали!')
        await message.delete()
    except:
        await message.reply('общение с ботом через ЛС')

@dp.message_handler(commands=['Режим_работы'])
async def command_start(message : types.Message):    
    await bot.send_message(message.from_user.id, 'С 8:30  до 17:30')

@dp.message_handler(commands=['Расположение'])
async def command_start(message : types.Message):    
    await bot.send_message(message.from_user.id, 'Сыктывкар')

#*********************админ*********************
#***********************************************
@dp.message_handler()
async def echo_send(message : types.Message):
    if message.text == 'Привет':
        await message.answer(f"И тебе привет")
    #await message.reply(message.text)
    #await bot.send_message(message.from_user.id, message.text)

#executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
executor.start_polling(dp, skip_updates=True)