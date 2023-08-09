from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, \
    KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start = ReplyKeyboardMarkup(resize_keyboard=True)

info = types.KeyboardButton('Info')

audi_80 = KeyboardButton('AUDI 80')
audi_90 = KeyboardButton('AUDI 90')
audi_100 = KeyboardButton('AUDI 100')
audi_200 = KeyboardButton('AUDI 200')
audi_class_a = KeyboardButton("AUDI Class A")
audi_class_q = KeyboardButton("AUDI Class Q")
audi_class_r8_rs = KeyboardButton("AUDI R8/RS")
audi_class_s_sq = KeyboardButton("AUDI S/SQ")
audi_class_tt_tts = KeyboardButton("AUDI TT/TTS")

restart = KeyboardButton('/restart')
start.add(audi_80, audi_90, audi_100)
start.add(audi_200, audi_class_a, audi_class_q)
start.add(audi_class_r8_rs, audi_class_s_sq, audi_class_tt_tts)
start.add(info, restart)

in_info = InlineKeyboardMarkup()
inline_info = InlineKeyboardButton(
    text='Получить информацию', callback_data='inlineinfo')
in_info.add(inline_info)

# Инлайн-кнопки ауди класса А
buttons_models_audi_class_a = InlineKeyboardMarkup(row_width=2)
audi_a1 = InlineKeyboardButton(text='AUDI A1', callback_data='AUDI A1')
audi_a2 = InlineKeyboardButton(text='AUDI A2', callback_data='AUDI A2')
audi_a3 = InlineKeyboardButton(text='AUDI A3', callback_data='AUDI A3')
audi_a4 = InlineKeyboardButton(text='AUDI A4', callback_data='AUDI A4')
audi_a4_allroad = InlineKeyboardButton(
    text='AUDI A4-ALLROAD', callback_data='AUDI A4-ALLROAD')
audi_a5 = InlineKeyboardButton(text='AUDI A5', callback_data='AUDI A5')
audi_a6 = InlineKeyboardButton(text='AUDI A6', callback_data='AUDI A6')
audi_a6_allroad = InlineKeyboardButton(
    text='AUDI A6-ALLROAD', callback_data='AUDI A6-ALLROAD')
audi_a7 = InlineKeyboardButton(text='AUDI A7', callback_data='AUDI A7')
audi_a8 = InlineKeyboardButton(text='AUDI A8', callback_data='AUDI A8')
buttons_models_audi_class_a.add(audi_a1, audi_a2)
buttons_models_audi_class_a.add(audi_a3, audi_a4)
buttons_models_audi_class_a.add(audi_a4_allroad, audi_a5)
buttons_models_audi_class_a.add(audi_a6, audi_a6_allroad)
buttons_models_audi_class_a.add(audi_a7, audi_a8)

# Инлайн-кнопки ауди класса Q
buttons_models_audi_class_q = InlineKeyboardMarkup(row_width=2)
audi_q2 = InlineKeyboardButton(text='AUDI Q2', callback_data='AUDI Q2')
audi_q3 = InlineKeyboardButton(text='AUDI Q3', callback_data='AUDI Q3')
audi_q3_sportback = InlineKeyboardButton(
    text='AUDI Q3-SPORTBACK', callback_data='AUDI Q-SPORTBACK')
audi_q4_e_tron = InlineKeyboardButton(
    text='AUDI Q4-E-TRON', callback_data='AUDI Q4-E-TRON')
audi_q5 = InlineKeyboardButton(text='AUDI Q5', callback_data='AUDI Q5')
audi_q5_sportback = InlineKeyboardButton(
    text='AUDI Q5-SPORTBACK', callback_data='AUDI Q5-SPORTBACK')
audi_q7 = InlineKeyboardButton(text='AUDI Q7', callback_data='AUDI Q7')
audi_q8 = InlineKeyboardButton(text='AUDI Q8', callback_data='AUDI Q8')
buttons_models_audi_class_q.add(audi_q2, audi_q3)
buttons_models_audi_class_q.add(audi_q3_sportback, audi_q4_e_tron)
buttons_models_audi_class_q.add(audi_q5, audi_q5_sportback)
buttons_models_audi_class_q.add(audi_q7, audi_q8)

# Инлайн-кнопки ауди R8/RS
buttons_models_audi_r8_rs = InlineKeyboardMarkup(row_width=2)
audi_r8 = InlineKeyboardButton(text='AUDI R8', callback_data='AUDI R8')
audi_rs_q3 = InlineKeyboardButton(
    text='AUDI RS-Q3', callback_data='AUDI RS-Q3')
audi_rs_q8 = InlineKeyboardButton(
    text='AUDI RS-Q8', callback_data='AUDI RS-Q8')
audi_rs3 = InlineKeyboardButton(text='AUDI RS3', callback_data='AUDI RS3')
audi_rs5 = InlineKeyboardButton(text='AUDI RS5', callback_data='AUDI RS5')
audi_rs6 = InlineKeyboardButton(text='AUDI RS6', callback_data='AUDI RS6')
audi_rs7 = InlineKeyboardButton(text='AUDI RS7', callback_data='AUDI RS7')
buttons_models_audi_r8_rs.add(audi_r8, audi_rs_q3)
buttons_models_audi_r8_rs.add(audi_rs_q8, audi_rs3)
buttons_models_audi_r8_rs.add(audi_rs5, audi_rs6)
buttons_models_audi_r8_rs.add(audi_rs7)

# Инлайн-кнопки ауди S/SQ
buttons_models_audi_s_sq = InlineKeyboardMarkup(row_width=2)
audi_s3 = InlineKeyboardButton(text='AUDI S3', callback_data='AUDI S3')
audi_s4 = InlineKeyboardButton(text='AUDI S4', callback_data='AUDI S4')
audi_s5 = InlineKeyboardButton(text='AUDI S5', callback_data='AUDI S5')
audi_s6 = InlineKeyboardButton(text='AUDI S6', callback_data='AUDI S6')
audi_s7 = InlineKeyboardButton(text='AUDI S7', callback_data='AUDI S7')
audi_sq5 = InlineKeyboardButton(text='AUDI SQ5', callback_data='AUDI SQ5')
audi_sq7 = InlineKeyboardButton(text='AUDI SQ7', callback_data='AUDI SQ7')
audi_sq8 = InlineKeyboardButton(text='AUDI SQ8', callback_data='AUDI SQ8')
buttons_models_audi_s_sq.add(audi_s3, audi_s4)
buttons_models_audi_s_sq.add(audi_s5, audi_s6)
buttons_models_audi_s_sq.add(audi_s7, audi_sq5)
buttons_models_audi_s_sq.add(audi_sq7, audi_sq8)

# Инлайн-кнопки ауди TT/TTS
buttons_models_audi_tt_tts = InlineKeyboardMarkup(row_width=2)
audi_tt = InlineKeyboardButton(text='AUDI TT', callback_data='AUDI TT')
audi_tts = InlineKeyboardButton(text='AUDI TTS', callback_data='AUDI TTS')

buttons_models_audi_tt_tts.add(audi_tt, audi_tts)
