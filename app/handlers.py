from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command


import app.keyboards as kb
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот для вычислений "ШКОЛЬНЫЕ ФОРМУЛЫ".', reply_markup=kb.main)

@router.message(F.text == 'Что умеет этот бот?')
async def cmd_who_is_bot(message: Message):
    await message.answer('Я умею проводить вычисления по основным школьным предметам - алгебра, геометрия, физика, химия, информатика.'
                         '\n\nЯ могу найти объём сферы, площадь круга, силу тока, ускорение объекта, определить результат химической реакции, вычислить квадратный корень и ещё много других, сложных задач.'
                         '\n\nКак это работает?'
                         '\nШаг 1. Выбираешь нужный предмет.'
                         '\nШаг 2. Выбираешь тему, на которую надо что-то посчитать.'
                         '\nШаг 3. Отправляешь мне данные для вычислений.'
                         '\nШаг 4. Я присылаю тебе готовое решение!'
                         '\n\nИ всё это менее чем за 30 секунд!'
                         '\n\nИдеальные оценки, уважение учителя, довольные родители и куча свободного времени обеспечены!', reply_markup=kb.main)


@router.message(F.text == 'Попробовать бесплатно')
async def cmd_try_for_free(message: Message):
    await message.answer('Сейчас тебе доступно одно вычисление в день.'
                         '\n\nЛимит обновляется раз в день. В платной версии нет никаких ограничений.'
                         '\n\nТы можешь попробовать прямо сейчас. Выбери нужный предмет, тему и отправь мне данные для решения задачи.', reply_markup=kb.subjects)


@router.message(F.text == 'Как снять ограничения?')
async def cmd_remove_restrictions(message: Message):
    await message.answer('Ты можешь приобрести платную версию бота с функционалом на максималках...'
                         '\n\nСтоимость подписки  - 99 рублей в месяц либо 799 на год.'
                         '\n\nС 01 октября 2025г. стоимость бота подорожает до 150 рублей в месяц и 999 рублей в год.'
                         '\n\nУспевай приобрести прямо сейчас по самой низкой цене!'
                         '\n\nЧат-бот будет развиваться и обучаться, будут добавлены новые, даже сложные формулы по всем предметам.'
                         '\n\nНе упускай возможность завести себе умного помощника, который может посчитать для тебя всё!'
                         '\n\nЧтобы приобрести платную версию, нажми на кнопку "Купить безлимитную версию"')


@router.message(F.text == 'Купить безлимитную версию')
async def cmd_buy_unlimited_version(message: Message):
    await message.answer('Чтобы приобрести полную версию, выбери подписку для оплаты:')


@router.message(F.text == 'Другие каналы и боты для тебя')
async def other_projects(message: Message):
    await message.answer('Выбери интересующий проект:', reply_markup=kb.other_projects)


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

    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer(subject_name)
    await callback.message.answer(
        f'{subject_name}. Чтобы быстрее найти нужную тему, посмотри раздел в учебнике.',
        reply_markup=keyboard
    )


# Обработчики кнопок "Назад" (остаются здесь)
@router.callback_query(F.data == "back_to_subjects")
async def handle_back_to_subjects(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer("Выбор предмета")
    await callback.message.answer("Выбери предмет:", reply_markup=kb.subjects)


@router.callback_query(F.data == "main_menu")
async def handle_back_to_main(callback: CallbackQuery):
    await callback.message.edit_reply_markup(reply_markup=None)
    await callback.answer("Главное меню")
    await callback.message.answer("Главное меню:", reply_markup=kb.main)

# Обработчик для других проектов
@router.callback_query(F.data.in_(['lol_school_channel', 'test_game_quest', 'channel_chat_bot', 'generous_anonymous']))
async def handle_other_projects(callback: CallbackQuery):
    # Удаляем инлайн кнопки
    await callback.message.edit_reply_markup(reply_markup=None)

    # Ваша логика обработки
    if callback.data == 'lol_school_channel':
        await callback.message.answer("Канал LOL SCHOOL: ...")
    elif callback.data == 'test_game_quest':
        await callback.message.answer("Тесты, игры, квесты: ...")
    elif callback.data == 'channel_chat_bot':
        await callback.message.answer("Чат-бот для твоего канала: ...")
    elif callback.data == 'generous_anonymous':
        await callback.message.answer("Щедрый аноним: ...")

    await callback.answer()


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