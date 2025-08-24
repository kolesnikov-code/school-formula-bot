from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот для вычислений "ШКОЛЬНЫЕ ФОРМУЛЫ".', reply_markup=kb.main)


# ... остальные обработчики сообщений ...

# Единый обработчик для всех предметов
subjects = {
    'algebra': ('Алгебра', kb.algebra),
    'geometry': ('Геометрия', kb.geometry),
    'physics': ('Физика', kb.physics),
    'chemistry': ('Химия', kb.chemistry),
    'informatics': ('Информатика', kb.informatics)
}


@router.callback_query(F.data.in_(subjects.keys()))
async def handle_subject(callback: CallbackQuery):
    subject_name, keyboard = subjects[callback.data]

    # Удаляем инлайн кнопки после нажатия
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.answer(subject_name)
    await callback.message.answer(
        f'{subject_name}. Чтобы быстрее найти нужную тему, посмотри раздел в учебнике.',
        reply_markup=keyboard
    )


# Обработчики для конкретных тем (пример для алгебры)
@router.callback_query(F.data.in_(['percentages', 'proportions', 'equations', 'coordinates',
                                   'exponentiation', 'roots', 'number_sequence', 'number_progression']))
async def handle_algebra_topics(callback: CallbackQuery):
    topic_name = callback.data
    # Удаляем инлайн кнопки после нажатия
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.answer(f"Тема: {topic_name}")
    await callback.message.answer(
        f"Вы выбрали тему: {topic_name}. Пожалуйста, введите данные для вычислений..."
    )


# Обработчик кнопки "Назад" к выбору предметов
@router.callback_query(F.data == "back_to_subjects")
async def handle_back_to_subjects(callback: CallbackQuery):
    # Удаляем инлайн кнопки после нажатия
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.answer("Выбор предмета")
    await callback.message.answer(
        "Выбери предмет:",
        reply_markup=kb.subjects
    )


# Обработчик кнопки "Назад" в главное меню
@router.callback_query(F.data == "main_menu")
async def handle_back_to_main(callback: CallbackQuery):
    # Удаляем инлайн кнопки после нажатия
    await callback.message.edit_reply_markup(reply_markup=None)

    await callback.answer("Главное меню")
    await callback.message.answer(
        "Главное меню:",
        reply_markup=kb.main
    )


# Обработчик для других проектов
@router.callback_query(F.data.in_(['lol_school_channel', 'test_game_quest', 'channel_chat_bot', 'generous_anonymous']))
async def handle_other_projects(callback: CallbackQuery):
    # Удаляем инлайн кнопки
    await callback.message.edit_reply_markup(reply_markup=None)

    # Ваша логика обработки
    if callback.data == 'lol_school_channel':
        await callback.message.answer("Канал LOL SCHOOL: ...")
    elif callback.data == 'test_game_quest':
        await callback.message.answer("Тесты и игры: ...")
    elif callback.data == 'channel_chat_bot':
        await callback.message.answer("Чат-бот для канала: ...")
    elif callback.data == 'generous_anonymous':
        await callback.message.answer("Щедрый аноним: ...")

    await callback.answer()


