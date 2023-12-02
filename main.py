

from aiogram import Bot, Dispatcher, types, executor

# Устанавливаем уровень логов на DEBUG, чтобы видеть сообщения от Aiogram


# Создаем объекты бота и диспетчера
bot = Bot(token='6616755063:AAG0EMxgDT-UBeRimjQo2xSMfIF2Ftn7NoI')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Здравствуйте! Меня зовут Александра, я менеджер турагентства Pegas Touristik.\n- - - - - - -\n"
                        "Для подбора тура менеджеру необходимо задать вам несколько вопросов "
                        "и обсудить все нюансы.\n\n"
                        "Предоставьте контакты по кнопке внизу, чтобы я могла передать заявку в работу.",
                        reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True).add(
                            types.KeyboardButton("Предоставить контакты", request_contact=True)))


@dp.message_handler(content_types=['contact'])
async def handle_contact(message: types.Message):
    contact = message.contact
    user_data = f"Пользователь: {contact.first_name} {contact.last_name}\n" \
                f"Номер телефона: {contact.phone_number}\n" \
                f"Имя пользователя: @{message.from_user.username}"

    # Отправляем сообщение с контактами в указанный чат
    chat_id = -1002140769008  # ID чата, куда отправлять контакты
    await bot.send_message(chat_id, user_data)

    await message.reply("Спасибо! Ваша заявка принята. Мы свяжемся с вами в ближайшее время.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)