from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb

# Создаем отдельный роутер для алгебры

algebra_router = Router()


# Единый обработчик для всех предметов
algebra_base = {
    'percentages': ('Проценты', kb.algebra_base),
    'proportions': ('Пропорции', kb.algebra_base),
    'equations': ('Уравнения', kb.algebra_base),
    'coordinates': ('Координаты', kb.algebra_base),
    'exponentiation': ('Возведение в степень', kb.algebra_base),
    'roots': ('Корень из числа', kb.algebra_base),
    'number_sequence': ('Числовая последовательность', kb.algebra_base),
    'number_progression': ('Числовая прогрессия', kb.algebra_base)
}


@algebra_router.callback_query(F.data.in_(algebra_base.keys()))
async def handle_subject(callback: CallbackQuery):
    subject_name, keyboard = algebra_base[callback.data]

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(subject_name)
    await callback.message.answer(
        f'{subject_name}. Чтобы быстрее найти нужную тему, посмотри раздел в учебнике.',
        reply_markup=keyboard
    )


# Словарь для красивого отображения названий тем
# topic_names = {
#     'percentages': 'Проценты',
#     'proportions': 'Пропорции',
#     'equations': 'Уравнения',
#     'coordinates': 'Координаты',
#     'exponentiation': 'Возведение в степень',
#     'roots': 'Корень из числа',
#     'number_sequence': 'Числовая последовательность',
#     'number_progression': 'Числовая прогрессия'
# }

# ФУНКЦИЯ ВЫБОРА ТЕМЫ ПОСЛЕ ПЕРЕХОДА В РАЗДЕЛ
#
# @algebra_router.callback_query(F.data.in_(topic_names.keys()))
# async def handle_algebra_topics(callback: CallbackQuery):
#     topic_key = callback.data
#     topic_name = topic_names[topic_key]
#
#     # Удаляем инлайн кнопки после нажатия
#     await callback.message.edit_reply_markup(reply_markup=None)
#
#     await callback.answer(f"Тема: {topic_name}")
#
#     # Здесь можно добавить специфичные инструкции для каждой темы
#     if topic_key == 'percentages':
#         await callback.message.answer(
#             f"📊 {topic_name}. Введите данные в формате 'количество %, основное число':\n"
#             "• Найти X% от Y\n"
#             "• Сколько процентов составляет X от Y\n"
#             "• Увеличить/уменьшить X на Y%\n\n"
#             "Пример: 'Найти 15% от 200'"
#         )
#     elif topic_key == 'equations':
#         await callback.message.answer(
#             f"📝 {topic_name}. Введите уравнение:\n"
#             "• Линейное: 2x + 5 = 15\n"
#             "• Квадратное: x² - 5x + 6 = 0\n"
#             "• Система уравнений: 2x + y = 7, x - y = 1"
#         )
#     else:
#         await callback.message.answer(
#             f"Вы выбрали тему: {topic_name}. Пожалуйста, введите данные для вычислений..."
#         )


# Здесь будут обработчики для ввода данных и вычислений
@algebra_router.message(F.text)
async def handle_algebra_input(message: Message):
    # Здесь будет логика обработки введенных пользователем данных
    # В зависимости от выбранной темы будем применять разные формулы
    text = message.text.lower()

    # Пример обработки процентов
    if 'процент' in text or '%' in text:
        await message.answer("Обрабатываю запрос по процентам...")
        # Вызов функции вычисления процентов
        # result = calculate_percentages(text)
        # await message.answer(result)
    elif 'уравнение' in text or '=' in text:
        await message.answer("Решаю уравнение...")
        # Вызов функции решения уравнений
    else:
        await message.answer("Пожалуйста, уточните запрос для вычислений")


# Функции вычислений (можно вынести в отдельный файл formulas/algebra_formulas.py)
def calculate_percentages(text: str) -> str:
    """Вычисление процентов"""
    # Логика вычислений
    return "Результат вычисления процентов: ..."


def solve_equation(equation: str) -> str:
    """Решение уравнений"""
    # Логика решения уравнений
    return "Решение уравнения: ..."