from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#main menu
#buttons
button_get = KeyboardButton(text='Получить номер предписания')
button_inf = KeyboardButton(text='Справка')

menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [button_get],  # Создаем список, содержащий одну кнопку
    [button_inf]   # Создаем список, содержащий вторую кнопку
])

#admin menu
button_delete = KeyboardButton(text='Удалить номер предписания')
button_log = KeyboardButton(text='Журнал логов')
button_back = KeyboardButton(text='Вернуться в главное меню')
button_db = KeyboardButton(text='Скачать БД')
button_del = KeyboardButton(text='Удалить пользователя')
button_null = KeyboardButton(text='Сбросить номер предписания')
button_reg = KeyboardButton(text='Логи регистрации')
button_generate = KeyboardButton(text='Сгенерировать код')
button_check = KeyboardButton(text='Посмотреть код')

#inline_buttons
ikb_delete = InlineKeyboardButton(text='Подтвердить',callback_data='Подтвердить')
ikb_cancel = InlineKeyboardButton(text='Отмена',callback_data='Отмена')

ikb_remove = InlineKeyboardButton(text='Удалить пользователя',callback_data='Удалить пользователя')

#menus setup
admin_menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [button_delete, button_del],
    [button_db, button_log],
    [button_check, button_reg],
    [button_generate],
    [button_back]
])

#ikb_menu = InlineKeyboardMarkup(row_width= 2).add(ikb_cancel,ikb_delete)
ikb_menu = InlineKeyboardMarkup(row_width= 2, inline_keyboard=[
    [ikb_cancel, ikb_delete]  # Создаем список, содержащий две кнопки
])
#ikb_remove_user = InlineKeyboardMarkup(row_width= 2).add(ikb_cancel,ikb_remove)
ikb_remove_user = InlineKeyboardMarkup(row_width= 2, inline_keyboard=[
    [ikb_cancel, ikb_remove]  # Создаем список, содержащий две кнопки
])