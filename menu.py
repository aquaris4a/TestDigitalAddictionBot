from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_menu_handlers(dp):
    @dp.message_handler(commands=['start', 'menu'])
    async def send_main_menu(message: types.Message):
        kb = InlineKeyboardMarkup(row_width=1)
        kb.add(
            InlineKeyboardButton("📱 Тест на интернет-зависимость", callback_data="test_internet"),
            InlineKeyboardButton("🎨 Струп-тест", callback_data="test_stroop"),
            InlineKeyboardButton("🔍 Тест Бурдона", callback_data="test_bourdon"),
            InlineKeyboardButton("😨 Тест тревожности Бека", callback_data="test_beck")
        )
        await message.answer("👋 Добро пожаловать! Выберите тест:", reply_markup=kb)

    @dp.callback_query_handler(lambda c: c.data.startswith("test_"))
    async def route_test(callback_query: types.CallbackQuery):
        route = {
            "test_internet": "/internet",
            "test_stroop": "/stroop",
            "test_bourdon": "/bourdon",
            "test_beck": "/beck"
        }.get(callback_query.data, None)
        if route:
            await callback_query.message.answer(f"Введите {route} для запуска теста.")
        await callback_query.answer()
