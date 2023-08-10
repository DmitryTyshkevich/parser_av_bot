from aiogram import Bot, types
from aiogram.utils import executor
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Command, Text
import config
import keyboard
import logging
import pars

# Для запуска модуля с парсером
asyncio.set_event_loop(
    asyncio.new_event_loop())  # Устанавливает loop как текущий цикл событий для текущего потока ОС

bot = Bot(token=config.botkey, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(
    filename='log.txt',
    level=logging.INFO,
    format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
           u'[%(asctime)s] %(message)s'
)


# Обработчик команд "/start" и "/restart"
@dp.message_handler(Command(["start", "restart"]), state=None)  # задаем название команды start
async def welcome(message):
    with open("user.txt", "r") as joinedFile:  # создаем файл в который будем записывать id пользователя
        joinedUsers = set()
        for line in joinedFile:  # цикл, в котором проверяем имеется ли такой id в фале user
            joinedUsers.add(line.strip())
    if not str(message.chat.id) in joinedUsers:  # делаем запись в файл user нового id
        with open("user.txt", 'a') as joinedFile:
            joinedFile.write(str(message.chat.id) + "\n")
            joinedUsers.add(message.chat.id)
    await message.answer(
        f'Здравствуйте, {message.from_user.first_name}, Bot запущен',
        reply_markup=keyboard.start
    )
    # после проверки и записи выводим сообщение с именем пользователя и отображаем кнопки


# Обработчик инлайн-кнопоки'Получить информацию'
@dp.callback_query_handler(text=['inlineinfo'])
async def inline_reference_list_button_handler(call: types.CallbackQuery):
    match call.data:
        case 'inlineinfo':
            await call.message.answer('Бот создан для изучения фреймворка aiogram')
    await call.answer()


# Обработчик команд с клавиатуры
@dp.message_handler(Text(
    [
        'Info', 'AUDI 80', 'AUDI 90', 'AUDI 100', 'AUDI 200',
        "AUDI Class A", 'AUDI Class A', 'AUDI Class Q', 'AUDI R8/RS',
        'AUDI S/SQ', 'AUDI TT/TTS'
    ]
), state=None)
async def get_message(message: types.Message):
    match message.text:
        case 'Info':
            await message.answer('Информация о боте:', reply_markup=keyboard.in_info)
        case "AUDI 80":
            if message.text in pars.links_per_model:
                for link in pars.links_per_model[message.text]:
                    await message.answer(link)
        case "AUDI 90":
            if message.text in pars.links_per_model:
                for link in pars.links_per_model[message.text]:
                    await message.answer(link)
        case "AUDI 100":
            if message.text in pars.links_per_model:
                for link in pars.links_per_model[message.text]:
                    await message.answer(link)
        case "AUDI 200":
            if message.text in pars.links_per_model:
                for link in pars.links_per_model[message.text]:
                    await message.answer(link)
        case "AUDI Class A":
            await bot.send_message(message.chat.id, text='Выберите модель:',
                                   reply_markup=keyboard.buttons_models_audi_class_a)
        case "AUDI Class Q":
            await bot.send_message(message.chat.id, text='Выберите модель:',
                                   reply_markup=keyboard.buttons_models_audi_class_q)
        case "AUDI R8/RS":
            await bot.send_message(message.chat.id, text='Выберите модель:',
                                   reply_markup=keyboard.buttons_models_audi_r8_rs)
        case "AUDI S/SQ":
            await bot.send_message(message.chat.id, text='Выберите модель:',
                                   reply_markup=keyboard.buttons_models_audi_s_sq)
        case "AUDI TT/TTS":
            await bot.send_message(message.chat.id, text='Выберите модель:',
                                   reply_markup=keyboard.buttons_models_audi_tt_tts)


# Обработчик инлайн-кнопок: buttons_models_audi
@dp.callback_query_handler(Text(startswith='AUDI'))
async def func(call: types.CallbackQuery):
    if call.data in pars.links_per_model:
        for link in pars.links_per_model[call.data]:
            await call.message.answer(link)
        await call.answer()


if __name__ == '__main__':
    print('Бот запущен!')
    executor.start_polling(dp, skip_updates=True)
