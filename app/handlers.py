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
                         '\n\nЯ могу найти объём сферы, площадь круга, силу тока, ускорение объекта, определить результат химической реакции, вычислить квадратный корень из сложного уравнения и ещё много других, сложных задач.'
                         '\n\nКак это работает?'
                         '\nШаг 1. Выбираешь нужный предмет.'
                         '\nШаг 2. Выбираешь тему, на которую надо что-то посчитать.'
                         '\nШаг 3. Отправляешь мне данные для вычислений.'
                         '\nШаг 4. Я присылаю тебе готовое решение!'
                         '\n\nИ всё это менее чем за 30 секунд!'
                         '\n\nИдеальные оценки, уважение учителя, довольные родители и куча свободного времени обеспечены!', reply_markup=kb.main)


@router.message(F.text == 'Попробовать бесплатно')
async def cmd_try_for_free(message: Message):
    await message.answer('Сейчас тебе доступно одно вычисление в неделю.'
                         '\n\nЛимит обновляется раз в 7 дней, начиная с момента первого использования.'
                         '\n\nТы можешь попробовать прямо сейчас. Выбери нужный предмет, тему и отправь мне данные для решения задачи.', reply_markup=kb.subjects)


@router.message(F.text == 'Как снять ограничения?')
async def cmd_remove_restrictions(message: Message):
    await message.answer('Ты можешь приобрести платную версию бота с функционалом на максималках...'
                         '\n\nСтоимость подписки навсегда - 300 рублей при оплате до 31 августа 2025г. Оплата нужна один раз за всё время, бот будет работать всегда.'
                         '\n\nС 01 сентября 2025г. стоимость бота поднимется до 500 рублей!'
                         '\nС 01 октября 2025г. стоимость бота подорожает до 1000 рублей!'
                         '\n\nУспевай приобрести прямо сейчас по самой низкой цене!'
                         '\n\nЧат-бот будет развиваться и обучаться, будут добавлены все существующие формулы по всем предметам.'
                         '\n\nНе упускай возможность завести себе умного помощника, который может посчитать для тебя всё!'
                         '\n\nЧтобы приобрести платную версию, нажми на кнопку "Купить безлимитную версию"')


@router.message(F.text == 'Купить безлимитную версию')
async def cmd_buy_unlimited_version(message: Message):
    await message.answer('Чтобы приобрести полную версию, перейди по кнопке ниже для оплаты:')


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
    await callback.answer(subject_name)
    await callback.message.answer(
   f'{subject_name}. Чтобы быстрее найти нужную тему, посмотри раздел в учебнике.',
        reply_markup=keyboard
    )