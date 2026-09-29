from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_kb():
    """Главное меню."""
    kb = InlineKeyboardMarkup()
    kb.row(InlineKeyboardButton("Отметить чтение", callback_data="report"))
    kb.row(InlineKeyboardButton("Моя библиотека", callback_data="library"))
    kb.row(InlineKeyboardButton("Рейтинг", callback_data="rating"))
    kb.row(InlineKeyboardButton("Профиль", callback_data="profile"))
    return kb