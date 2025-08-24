from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Что умеет этот бот?')],
    [KeyboardButton(text='Попробовать бесплатно')],
    [KeyboardButton(text='Как снять ограничения?')],
    [KeyboardButton(text='Купить безлимитную версию')],
    [KeyboardButton(text='Другие каналы и боты для тебя')]],
    resize_keyboard=True, input_field_placeholder='Выбери пункт меню...')


subjects = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Алгебра', callback_data='algebra')],
    [InlineKeyboardButton(text='Геометрия', callback_data='geometry')],
    [InlineKeyboardButton(text='Физика', callback_data='physics')],
    [InlineKeyboardButton(text='Химия', callback_data='chemistry')],
    [InlineKeyboardButton(text='Информатика', callback_data='informatics')]],
    row_width=1)


algebra = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Дроби', callback_data='fractions')],
    [InlineKeyboardButton(text='Проценты', callback_data='percentages')],
    [InlineKeyboardButton(text='Пропорции', callback_data='proportions')],
    [InlineKeyboardButton(text='Уравнения', callback_data='equations')],
    [InlineKeyboardButton(text='Координаты', callback_data='coordinates')],
    [InlineKeyboardButton(text='Многочлены', callback_data='polynomials')],
    [InlineKeyboardButton(text='Возведение в степень', callback_data='exponentiation')],
    [InlineKeyboardButton(text='Корень из числа', callback_data='roots')],
    [InlineKeyboardButton(text='Числовая плоскость', callback_data='number_plane')],
    [InlineKeyboardButton(text='Числовые промежутки', callback_data='number_intervals')],
    [InlineKeyboardButton(text='Рациональные уравнения', callback_data='rational_equations')],
    [InlineKeyboardButton(text='Иррациональные уравнения', callback_data='irrational_equations')],
    [InlineKeyboardButton(text='Неравенства', callback_data='inequalities')],
    [InlineKeyboardButton(text='Функции и графики', callback_data='functions_graphs')],
    [InlineKeyboardButton(text='Числовая последовательность', callback_data='number_sequence')],
    [InlineKeyboardButton(text='Числовая прогрессия', callback_data='number_progression')],
    [InlineKeyboardButton(text='Линейные уравнения', callback_data='linear_equations')],
    [InlineKeyboardButton(text='Квадратные уравнения', callback_data='quadratic_equations')],
    [InlineKeyboardButton(text='Частота и вероятность', callback_data='frequency_probability')]],
    row_width=1)


geometry = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Точка', callback_data='point')],
    [InlineKeyboardButton(text='Прямая, вектор', callback_data='line_vector')],
    [InlineKeyboardButton(text='Параллель, перпендикуляр', callback_data='parallel_perpendicular')],
    [InlineKeyboardButton(text='Плоскость', callback_data='plane')],
    [InlineKeyboardButton(text='Треугольник, пирамида', callback_data='triangle_pyramid')],
    [InlineKeyboardButton(text='Квадрат, куб', callback_data='square_cube')],
    [InlineKeyboardButton(text='Прямоугольник, цилиндр', callback_data='rectangle_cylinder')],
    [InlineKeyboardButton(text='Круг, сфера (шар)', callback_data='circle_sphere')],
    [InlineKeyboardButton(text='Ромб, трапеция, призма', callback_data='rhombus_trapezoid_prism')],
    [InlineKeyboardButton(text='Многогранники', callback_data='polyhedra')],
    [InlineKeyboardButton(text='Теоремы (Пифагора и т.д.)', callback_data='theorems')],
    [InlineKeyboardButton(text='Площадь фигуры', callback_data='area')],
    [InlineKeyboardButton(text='Объём фигуры', callback_data='volume')]],
    row_width=1)


physics = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оптика', callback_data='optics')],
    [InlineKeyboardButton(text='Акустика', callback_data='acoustics')],
    [InlineKeyboardButton(text='Механика', callback_data='mechanics')],
    [InlineKeyboardButton(text='Термодинамика', callback_data='thermodynamics')],
    [InlineKeyboardButton(text='Молекулярная физика', callback_data='molecular_physics')],
    [InlineKeyboardButton(text='Электричество и магнетизм', callback_data='electromagnetism')],
    [InlineKeyboardButton(text='Атомная физика', callback_data='atomic_physics')],
    [InlineKeyboardButton(text='Квантовая физика', callback_data='quantum_physics')],
    [InlineKeyboardButton(text='Ядерная физика', callback_data='nuclear_physics')]],
    row_width=1)


chemistry = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Кислоты', callback_data='acids')],
    [InlineKeyboardButton(text='Щелочи', callback_data='alkalis')],
    [InlineKeyboardButton(text='Соли', callback_data='salts')],
    [InlineKeyboardButton(text='Газы', callback_data='gases')],
    [InlineKeyboardButton(text='Металлы', callback_data='metals')],
    [InlineKeyboardButton(text='Неметаллы', callback_data='nonmetals')],
    [InlineKeyboardButton(text='Органическая химия', callback_data='organic_chemistry')],
    [InlineKeyboardButton(text='Неорганическая химия', callback_data='inorganic_chemistry')],
    [InlineKeyboardButton(text='Физическая химия', callback_data='physical_chemistry')],
    [InlineKeyboardButton(text='Аналитическая химия', callback_data='analytical_chemistry')],
    [InlineKeyboardButton(text='Биохимия', callback_data='biochemistry')]],
    row_width=1)


informatics = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Информация', callback_data='information')],
    [InlineKeyboardButton(text='Алгоритмы', callback_data='algorithms')],
    [InlineKeyboardButton(text='Кодирование', callback_data='coding')],
    [InlineKeyboardButton(text='Формальные языки', callback_data='formal_languages')],
    [InlineKeyboardButton(text='Архитектура ЭВМ', callback_data='computer_architecture')],
    [InlineKeyboardButton(text='Операционные системы (ОС)', callback_data='operating_systems')],
    [InlineKeyboardButton(text='Языки программирования (ЯП)', callback_data='programming_languages')],
    [InlineKeyboardButton(text='Программное обеспечение (ПО)', callback_data='software')],
    [InlineKeyboardButton(text='Базы данных, хранение информации', callback_data='databases')],
    [InlineKeyboardButton(text='Сеть, интернет', callback_data='networking')],
    [InlineKeyboardButton(text='Искусственный интеллект', callback_data='artificial_intelligence')]],
    row_width=1)


other_projects = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Канал "LOL SCHOOL"', callback_data='lol_school_channel')],
    [InlineKeyboardButton(text='Тесты | Игры | Квесты', callback_data='test_game_quest')],
    [InlineKeyboardButton(text='Чат-бот для твоего канала', callback_data='channel_chat_bot')],
    [InlineKeyboardButton(text='Щедрый аноним', callback_data='generous_anonymous')]],
    row_width=1)