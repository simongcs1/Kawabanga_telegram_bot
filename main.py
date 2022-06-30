import telebot
import requests
import datetime
from telebot import types
from bs4 import BeautifulSoup as bs
from random import choice


###ФУНКЦИЯ ВЫДАЕТ СЛУЧАЙНЫЙ АНЕКДОТ###
def joke_parcer():
    r = requests.get('https://www.anekdot.ru/random/anekdot/')
    soup = bs(r.text, 'html.parser')
    jokes = soup.find_all('div', class_='text')
    list_of_jokes = [i.text for i in jokes]
    return choice(list_of_jokes)

bot = telebot.TeleBot('5538413542:AAFBTI5ibHPSPuKQw-yssbdC_Jp8w8EagHg') #API token from BotFather

'''*******************************КОНСТАНТЫ************************************************'''
call_to_admin = types.InlineKeyboardButton("📞 Связь с администратором! 📞", url='https://t.me/kawabangaschool')
text_via_tg = types.InlineKeyboardButton("Написать в Telegram", url='https://t.me/kawabangaschool')
call_order = types.InlineKeyboardButton("Заказать звонок", url='https://t.me/simon_lbu')
kwb_chat = types.InlineKeyboardButton("🤙 Kawabanga chat 🤙", url='https://t.me/kawabanga_school')
kwb_site = types.InlineKeyboardButton("🤙 Kawabanga School 🤙", url='https://kawabanga.pro')
time_table = types.InlineKeyboardButton("Расписание групповых занятий",
                                        callback_data='Расписание групповых занятий')
spots = types.InlineKeyboardButton("Наши места для катания!",
                                        callback_data='Места для катания')
private_training = types.InlineKeyboardButton("Записаться на индивидуальное занятие",
                                              callback_data='Индивидуальные занятия')
weather = f"☝️Место проведения занятий сильно зависит от погоды!\n🌦🌦🌦" \
          f"\nСледите за новостями занятий через наш Telegram канал!"
price_list = f'<b>Стоимость индивидуального занятия: <u>1300 р/час.</u></b>\n\n' \
             f'Комплект снаряжения на индивидуальное занятие выдается бесплатно!\n\n' \
             f'<b>В комплект входят: 🛹🛹🛹</b>\nлонгборд/скейт, шлем, наколенники, налокотники, перчатки\n\n' \
             f'<b>Групповые занятия:</b>\n\n' \
             f'<b>Разовое занятие</b>: <u>650 рублей</u>\n\n<b>Абонементы:</b>' \
             f'\n<b>5 занятий:</b> <u> 3000 р.</u>  (600 рублей одно занятие)\n' \
             f'<b>10 занятий</b>: <u>5500 р.</u> (550 рублей одно занятие)\n' \
             f'<b>20 занятий</b>: <u>10000 р.</u> (500 рублей занятие) \n\n' \
             f'<b>Проката снаряжения в группе:</b> <u>300 рублей</u>\n\n' \
             f'Все занятия проходят <b><u>ПО ПРЕДВАРИТЕЛЬНОЙ ЗАПИСИ!</u></b>\n\n' \
             f'Вы можете записаться у администратора через Telegram или позвонит по телефону:\n+7-927-233-92-85'
time = f'<b>Понедельник, Среда, Пятница:\n\n🕟<u>19:00 "Уфа Арена"</u>\n(со стороны фонтанов)' \
       f'\n\nВторник, Четверг:\n\n🕟<u>20.00 Роллердром</u>\n(ТЦ "Ультра, левый вход, 2й этаж)"' \
       f'\n\nСуббота:\n\n<u>🕙11.00 "Уфа Арена" или "Роллердром"</u>' \
       f'\n\nВоскресенье:\n\n<u>🕙11.00 Памп трек</u>\n(TРЦ Мега)</b>\n\n' \
       f'Все занятия проходят <b><u>ПО ПРЕДВАРИТЕЛЬНОЙ ЗАПИСИ!</u></b>\n\n' \
       f'Вы можете записаться у администратора через Telegram или позвонит по телефону:\n+7-927-233-92-85'
booking = types.KeyboardButton('Запись на занятие ')
prices = types.InlineKeyboardButton("Цены на обучение", callback_data='Цены на обучение')

inst = types.InlineKeyboardButton("Наш Instagram", url='https://instagram.com/kawabanga_ufa')
vk = types.InlineKeyboardButton("Наш VK", url='https://vk.com/kawabangaschool')
###start###
inline_keyboard_start = types.InlineKeyboardMarkup(row_width=1)
inline_keyboard_start.add(time_table, private_training, prices)
###Групповые
time_markup = types.InlineKeyboardMarkup()
admin_markup = types.InlineKeyboardMarkup()
time_markup.add(prices, kwb_chat)
admin_markup.add(call_to_admin)
###ЦЕНЫ
inline_keyboard_prices = types.InlineKeyboardMarkup(row_width=1)
inline_keyboard_prices.add(call_to_admin, time_table, private_training)
###Места катаний
# inline_keyboard_spots = types.InlineKeyboardMarkup(row_width=1)
# inline_keyboard_spots.add(arena, biathlon, rollerdrome)

'''*******************************КЛИЕНТСКИЙ БЛОК************************************************'''
@bot.message_handler(commands=['start'])
def start(message):
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # keyboard.add(booking, call_to_admin)

    greatings = f'Привет <b>{message.from_user.first_name}</b>!👋\n\nМы экстрим школа для взрослых и детей <b>Kawabanga!</b>🤙' \
                f'\n\n<b>Зимой</b> обучаем катанию на сноуборде и горных лыжах!\n🏂⛷\n<b>Летом</b> на лонгборде/скейте и роликах!\n🛹🛼' \
                f'\n\nВыбери какой вопрос тебя интересует или напишите в сообщении?👇'

    bot.send_message(message.chat.id, greatings, parse_mode='html', reply_markup=inline_keyboard_start)

###РАСПИСАНИЕ ГРУППОВЫХ ЗАНЯТИЙ###
@bot.callback_query_handler(func=lambda call: call.data =='Расписание групповых занятий')
def group_training(call: types.CallbackQuery):

    bot.send_message(call.message.chat.id, time, reply_markup=admin_markup, parse_mode='html')
    bot.send_message(call.message.chat.id, weather, parse_mode='html', reply_markup=time_markup)
    bot.answer_callback_query(call.id)

###ИНДИВИДУАЛЬНЕ ЗАНЯТИЯ(еще не готов)###
@bot.callback_query_handler(func=lambda call: call.data =='Индивидуальные занятия')


#def private_training(call: types.CallbackQuery):
    # markup = types.InlineKeyboardMarkup()
    # client_age = f'Укажите пожалуйста возраст ученика!'
    #
    # markup.add(kwb_chat)
    # bot.send_message(call.message.chat.id, client_age, parse_mode='html')
    # bot.answer_callback_query(call.id)

###МЕСТА КАТАНИЙ
@bot.message_handler(commands=['spot'])
def spots_info_menu(a):
    spots_mainmenu = types.InlineKeyboardMarkup()
    arena_button = types.InlineKeyboardButton(text='"Уфа Арена"', callback_data='arena_button')
    biathlon_button = types.InlineKeyboardButton(text='Биатлон', callback_data='biathlon_button')
    rollerdrom_button = types.InlineKeyboardButton(text='Роллердром', callback_data='rollerdrom_button')
    spots_mainmenu.add(arena_button, biathlon_button, rollerdrom_button)
    bot.send_message(a.chat.id, f'👇 Наши места катания!👇', reply_markup=spots_mainmenu)

@bot.callback_query_handler(func=lambda call: True)
def spots_info(call):
    # if call.data == "spots_mainmenu":
    #     spots_mainmenu = types.InlineKeyboardMarkup()
    #     arena_button = types.InlineKeyboardButton(text='"Уфа Арена"', callback_data='arena_button')
    #     biathlon_button = types.InlineKeyboardButton(text='Биатлон', callback_data='biathlon_button')
    #     rollerdrom_button = types.InlineKeyboardButton(text='Роллердром', callback_data='rollerdrom_button')
    #     spots_mainmenu.add(arena_button, biathlon_button, rollerdrom_button)
    #     bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=spots_mainmenu)
    if call.data == "arena_button":
        next_menu = types.InlineKeyboardMarkup()
        biathlon_button = types.InlineKeyboardButton(text='Биатлон', callback_data='biathlon_button')
        rollerdrom_button = types.InlineKeyboardButton(text='Роллердром', callback_data='rollerdrom_button')
        next_menu.add(biathlon_button, rollerdrom_button)
        arena_adress = "<a href='https://yandex.ru/maps/172/ufa/?indoorLevel=1&ll=" \
                       "55.956763%2C54.738658&mode=routes&rtext=~54.738983%2C55.955658&rtt=auto&ruri=~&z=17.4'><u>Ленина 114</u></a>"

        arena_photo = "<a href='https://sun9-66.userapi.com/impf/bw5Q9Y475rmwqSnpW51TDBbN9J9WO30Unu2BgQ/" \
                      "6MHLkwtpTxc.jpg?size=1280x847&quality=95&sign=8dc4d2e5cc5a326c886c8b57a27a5661&type=album'> </a>"

        bot.edit_message_text(f'<b>"Уфа Арена"</b> {arena_photo}\n\nРовный асфальт и умеренный уклон!'
                               f'\n\nПрекрасное место для новичков и любителей денсинга!\n\n{arena_adress} 👈 Смотреть на карте!\nТочка сбора за лабораторией <b>"Лорак"</b> ✌️',
                               call.message.chat.id, call.message.message_id,
                               reply_markup=next_menu, parse_mode='HTML')
    elif call.data == "biathlon_button":
        next_menu2 = types.InlineKeyboardMarkup()
        arena_button = types.InlineKeyboardButton(text='"Уфа Арена"', callback_data='arena_button')
        rollerdrom_button = types.InlineKeyboardButton(text='Роллердром', callback_data='rollerdrom_button')
        next_menu2.add(arena_button, rollerdrom_button)
        biathlon_photo = "<a href='https://sun9-29.userapi.com/impf/o8gTO1dvo1kGcSxh6QJC6tMP9Hq3mfovl-cSKw/" \
                         "-cP5znS1aBI.jpg?size=1280x853&quality=95&sign=965acd57ece5865dadc96a54baf1c03b&type=album'> </a>"
        biathlon_adress = "<a href='https://yandex.ru/maps/172/ufa/?ll=56.039473%2C54.803905&mode=routes&rtext=~54.805432%2C56.036132&rtt=auto&ruri=~&z=15.53'><u>Комарова 1</u></a>"

        bot.edit_message_text(f'<b>"Биатлон"</b>{biathlon_photo}\n\nМы любим "Биатлон" за его универсальность!\n\n'
                              f'Идеальный асфальт и уклон <b>"на любой вкус"</b>\nОтлично подходит для <b>скоростного спуска(Downhill)</b>\n\n{biathlon_adress} 👈 '
                              f'Смотреть на карте!\nТочка сбора парковке перед комплексом <b>"Биатлон"</b> ✌', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2, parse_mode='HTML')

    elif call.data == "rollerdrom_button":
        next_menu3 = types.InlineKeyboardMarkup()
        arena_button = types.InlineKeyboardButton(text='"Уфа Арена"', callback_data='arena_button')
        biathlon_button = types.InlineKeyboardButton(text='Биатлон', callback_data='biathlon_button')
        rollerdrom_adress = "<a href='https://yandex.ru/maps/172/ufa/?indoorLevel=1&ll=55.984471%2C54.717286&" \
                            "mode=routes&rtext=~54.717276%2C55.984338&rtt=auto&ruri=~ymapsbm1%3A%2F%2Forg%3Foid%3D1903275297&z=17.38'>Бакалинская 27</a>"
        rollerdrom_photo = "<a href='https://sun9-9.userapi.com/impf/Vtn2dpLEW1yzOIqT1zcq0meDbQ36UEXInEe_Gw/tWMwxRjbosQ.jpg?size=1280x719&quality=95&sign=d39e7e8dbf49ef632207187656e39f60&type=album'> </a>"
        next_menu3.add(arena_button, biathlon_button)
        bot.edit_message_text(f'<b>"Роллердром"</b>{rollerdrom_photo}\n\nНа "Роллердроме" всегда отличная погода!\n\n'
                              f'Бетонное покрытие, тепло зимой и свежо летом!\nОтлично подходит для новичков, лучшее место для старта!\n\n{rollerdrom_adress} 👈 '
                              f'Смотреть на карте!\nТЦ Ультра, 2 этаж, левое крыло ✌', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu3, parse_mode='HTML')
# @bot.callback_query_handler(func=lambda call: call.data == 'Места катания')
# def spots(call: types.CallbackQuery):
#
#
#     bot.send_message(call.message.chat.id, price_list, reply_markup=inline_keyboard_spots, parse_mode='html')
#     bot.answer_callback_query(call.id)

###ЦЕНЫ НА ОБУЧЕНИЕ###
@bot.callback_query_handler(func=lambda call: call.data =='Цены на обучение')
def prices(call: types.CallbackQuery):

    bot.send_message(call.message.chat.id, price_list, reply_markup=inline_keyboard_prices, parse_mode='html')
    bot.answer_callback_query(call.id)

###КОМАНДА С ССЫЛКАМИ НА СОЦ.СЕТИ###
@bot.message_handler(commands=['social'])
def social(message):
    inline_social = types.InlineKeyboardMarkup(row_width=2)
    inline_social.add(inst, vk, kwb_chat)
    bot.send_message(message.chat.id, f'<b>Наши социальные сети</b> 👇\n\nПодписывайтесь и рассказывайте друзьям!🤙'
                     , parse_mode='html', reply_markup=inline_social)



###ФУНКЦИЯ НИЖЕ ОБРАБАТЫВАЕТ ЛЮБЫЕ ТЕКСТОВЫЕ СООБЩЕНИЯ###
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    markup = types.InlineKeyboardMarkup()
    answer_flag = False
    clean_words=''.join([c if c.isalpha() else ' ' for c in message.text.lower()])
    for j in clean_words.split():

        if j in ['привет', 'hi', 'hello', 'хай', 'здарова', 'здравствуйте', "приветствую", "алоха"]:
            bot.send_sticker(message.chat.id,
                             sticker='CAACAgIAAxkBAAEFB4lip3bfDkujNcA1mRCQ6ivA6S9VKgAC_wIAAm2wQgMEoDmrNAI2NyQE')
            bot.send_message(message.chat.id, "И тебе привет!")
            answer_flag = True

        if j in ["цены", "стоимость", "стоит", "цена", "прайс", "price", "cost", "лист", "прайслист"]:

            bot.send_message(message.chat.id, price_list, reply_markup=inline_keyboard_prices, parse_mode='html')
            answer_flag = True
            break
        elif j in ['лет', "возраст", "возраста", "возрасте"]:
            markup.add(call_to_admin)
            bot.send_message(message.chat.id, 'Обычно с <b>4 лет</b> до "бесконечности"😁\n\nСамому старшему ученику в нашей школе <b>66 лет</b>!!!'
                                              '\n\nВсе зависит от индивидуальных особенностей ученика!\n\n'
                                              'Всю подобную информацию Вы можете узнать у администратора через<u>👇️ Telegram 👇</u>\n'
                                              'Или позвонив по телефону +7-927-233-92-85 ️', reply_markup=markup, parse_mode='html')
            answer_flag = True
            break
        elif j in ['website', 'веб', 'сайт', 'site', 'web', 'вебсайт', "интернет", "страница"]:
            markup.add(kwb_site)
            bot.send_message(message.chat.id, '⬇️ Интернет страничка школы! ⬇', reply_markup=markup)
            answer_flag = True
            break

        elif j in ['канал', 'channel', 'chanel', 'telegram', 'чат', 'chat']:
            markup.add(kwb_chat)
            bot.send_message(message.chat.id,
                         f'Присоединяйтесь к Telegram каналу школы, что бы не пропустить групповые занятия! 👇️',
                         reply_markup=markup)
            answer_flag = True
            break

        elif j in ['запись', 'занятие', 'записаться', 'записатся', 'booking', 'book', "записаться", "запишите"]:

            markup.add(call_to_admin)
            bot.send_message(message.chat.id, '⬇ Запись на занятие! ⬇', reply_markup=markup)
            answer_flag = True
            break

        elif j in ['связь', 'звонок', 'контакт', 'контакты', "позвоните", "позвонить"]:

            markup.add(text_via_tg, call_order)
            bot.send_message(message.chat.id, '📞 Вы можете выбрать удобный для Вас способ связи! 📞'
                                          '\n\nПозвонить по телефону +7-927-233-92-85!\nили 👇', reply_markup=markup)
            answer_flag = True
            break

        elif j in ['kawabanga', 'kowabunga', 'kavabanga', 'kowabanga', 'кавабанга', "ковабанга"]:
            bot.send_sticker(message.chat.id,
                              sticker='CAACAgIAAxkBAAEFCl9iqLY5HLy2wj1RbU409laJiphfjgACmQADwu9cBZJvaP6daeplJAQ')
            bot.send_message(message.chat.id, 'А вы знали, что "Kowabunga" означать возглас восхищения у серферов?!')
            answer_flag = True
            break


        elif j in ['анекдот', 'joke', 'шутка', 'шутку']:
            bot.send_message(message.chat.id, "Лови!")
            bot.send_message(message.chat.id, joke_parcer())
            answer_flag = True
            break

        elif j in ['блять', 'сука', 'бля', 'блядь', 'гондон', 'ебать', 'выебу', 'ебланы', "еблан", 'пиздец', "шлюха", "пизда"]:
            bot.send_sticker(message.chat.id,
                         sticker='CAACAgQAAxkBAAEFB1pip2GCimih4eNlJPlS8PzsNqicSgACRgEAAqqvuQFIh89RP1b99CQE')
            bot.send_message(message.chat.id, "Ай, ай, ай... Нехорошо материться!")
            answer_flag = True
            break

    if not answer_flag:
         bot.send_sticker(message.chat.id, sticker='CAACAgIAAxkBAAEFB1Rip2BUbaDd6NK6lZEEY0WlNJbnzwACugADwPsIAAGSbw-9i6NJSyQE')
         bot.send_message(message.chat.id, "Я тебя не понимаю")


#
#     elif message.text == 'id':
#         m=types.InlineKeyboardMarkup()
#         m.add(types.InlineKeyboardButton('Цены',url="http://n.sss"))
# #        m.add(telebot.types.InlineKeyboardButton('Запись', url="#tst"))
# #        m.add(telebot.types.InlineKeyboardButton('Chih pih'))
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user}", reply_markup=m)
#     else:
#         bot.send_message(message.chat.id, 'Я тебя не понимаю...', parse_mode='html')



# @bot.message_handler(commands=['menu']) # Вызов меню бота
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#     website = types.KeyboardButton('Веб сайт')
#     kwb_chat = types.KeyboardButton('Telegram канал')
#     booking = types.KeyboardButton('Запись на занятие')
#     markup.add(website, kwb_chat, booking)
#     bot.send_message(message.chat.id, 'Выберете категорию', reply_markup=markup)
#
# def get_calendar(message):
#     now = datetime.datetime.now()  # Текущая дата
#     chat_id = message.chat.id
#     date = (now.year, now.month)
#     current_shown_dates[chat_id] = date  # Сохраним текущую дату в словарь
#     markup = create_calendar(now.year, now.month)
#     bot.send_message(message.chat.id, "Выберите дату для занятий!", reply_markup=markup)

bot.polling(none_stop=True)
