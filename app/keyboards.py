from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Функция для добавления кнопки "Назад" к любой клавиатуре
def add_back_button(keyboard: InlineKeyboardMarkup, back_data: str = "main_menu") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    # Добавляем существующие кнопки
    for row in keyboard.inline_keyboard:
        builder.row(*row)

    # Добавляем кнопку "Назад"
    builder.row(InlineKeyboardButton(text="◀️ Назад", callback_data=back_data))

    return builder.as_markup()


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Что умеет этот бот?')],
    [KeyboardButton(text='Попробовать бесплатно')],
    [KeyboardButton(text='Как снять ограничения?')],
    [KeyboardButton(text='Купить безлимитную версию')],
    [KeyboardButton(text='Другие каналы и боты для тебя')]],
    resize_keyboard=True, input_field_placeholder='Выбери пункт меню...')

# Основное меню предметов
subjects = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Алгебра', callback_data='algebra')],
    [InlineKeyboardButton(text='Геометрия', callback_data='geometry')],
    [InlineKeyboardButton(text='Физика', callback_data='physics')],
    [InlineKeyboardButton(text='Химия', callback_data='chemistry')],
    [InlineKeyboardButton(text='Информатика', callback_data='informatics')],
    [InlineKeyboardButton(text="◀️ Назад", callback_data="main_menu")]],
    row_width=1)

# Клавиатуры для предметов (без кнопки "Назад" в базовой версии)
algebra_base = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Проценты', callback_data='percentages')],
    [InlineKeyboardButton(text='Пропорции', callback_data='proportions')],
    [InlineKeyboardButton(text='Уравнения', callback_data='equations')],
    [InlineKeyboardButton(text='Координаты', callback_data='coordinates')],
    [InlineKeyboardButton(text='Возведение в степень', callback_data='exponentiation')],
    [InlineKeyboardButton(text='Корень из числа', callback_data='roots')],
    [InlineKeyboardButton(text='Числовая последовательность', callback_data='number_sequence')],
    [InlineKeyboardButton(text='Числовая прогрессия', callback_data='number_progression')]],
    row_width=1)

geometry_base = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Квадрат, прямоугольник', callback_data='square_cube')],
    [InlineKeyboardButton(text='Треугольник, круг', callback_data='rectangle_circle')],
    [InlineKeyboardButton(text='Ромб, трапеция', callback_data='rhombus_trapezoid')],
    [InlineKeyboardButton(text='Куб, пирамида', callback_data='triangle_pyramid')],
    [InlineKeyboardButton(text='Сфера (шар)', callback_data='_sphere')],
    [InlineKeyboardButton(text='Многогранники', callback_data='polyhedra')],
    [InlineKeyboardButton(text='Теоремы (Пифагора и т.д.)', callback_data='theorems')],
    [InlineKeyboardButton(text='Площадь фигуры', callback_data='area')],
    [InlineKeyboardButton(text='Объём фигуры', callback_data='volume')]],
    row_width=1)

physics_base = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оптика', callback_data='optics')],
    [InlineKeyboardButton(text='Акустика', callback_data='acoustics')],
    [InlineKeyboardButton(text='Механика', callback_data='mechanics')],
    [InlineKeyboardButton(text='Термодинамика', callback_data='thermodynamics')],
    [InlineKeyboardButton(text='Молекулярная физика', callback_data='molecular_physics')],
    [InlineKeyboardButton(text='Электричество и магнетизм', callback_data='electromagnetism')]],
    row_width=1)

chemistry_base = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кислоты', callback_data='acids')],
    [InlineKeyboardButton(text='Щелочи', callback_data='alkalis')],
    [InlineKeyboardButton(text='Соли', callback_data='salts')],
    [InlineKeyboardButton(text='Газы', callback_data='gases')],
    [InlineKeyboardButton(text='Металлы', callback_data='metals')],
    [InlineKeyboardButton(text='Неметаллы', callback_data='nonmetals')],
    [InlineKeyboardButton(text='Органическая химия', callback_data='organic_chemistry')],
    [InlineKeyboardButton(text='Неорганическая химия', callback_data='inorganic_chemistry')]],
    row_width=1)

informatics_base = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Информация', callback_data='information')],
    [InlineKeyboardButton(text='Алгоритмы', callback_data='algorithms')],
    [InlineKeyboardButton(text='Кодирование', callback_data='coding')],
    [InlineKeyboardButton(text='Базы данных, хранение информации', callback_data='databases')],
    [InlineKeyboardButton(text='Сеть, интернет', callback_data='networking')]],
    row_width=1)

# Финальные клавиатуры с кнопкой "Назад"
algebra = add_back_button(algebra_base, "back_to_subjects")
geometry = add_back_button(geometry_base, "back_to_subjects")
physics = add_back_button(physics_base, "back_to_subjects")
chemistry = add_back_button(chemistry_base, "back_to_subjects")
informatics = add_back_button(informatics_base, "back_to_subjects")

other_projects = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Канал "LOL SCHOOL"', callback_data='lol_school_channel')],
    [InlineKeyboardButton(text='Тесты | Игры | Квесты', callback_data='test_game_quest')],
    [InlineKeyboardButton(text='Чат-бот для твоего канала', callback_data='channel_chat_bot')],
    [InlineKeyboardButton(text='Щедрый аноним', callback_data='generous_anonymous')],
    [InlineKeyboardButton(text="◀️ Назад", callback_data="main_menu")]],
    row_width=1)