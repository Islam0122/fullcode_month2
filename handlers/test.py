from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from .questions import questions

router_test = Router()


class Test(StatesGroup):
    answering = State()


@router_test.message(Command("test"))
async def start_test(message: Message, state: FSMContext):

    await state.update_data(q_index=0, score=0)

    data = await state.get_data()
    q = questions[data["q_index"]]

    kb = ReplyKeyboardBuilder()

    for option in q["options"]:
        kb.add(KeyboardButton(text=option))
    kb.add(KeyboardButton(text="❌ Отменить Test"))
    kb.adjust(2)

    await message.answer(
        "🧠 Добро пожаловать в тест!\n\n"
        "Я задам тебе несколько вопросов.\n"
        "Выбирай правильный вариант ответа.\n\n"
        "Начнем! 🚀",
    )

    await message.answer(
        f"❓ Вопрос 1\n\n{q['question']}",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )

    await state.set_state(Test.answering)


@router_test.message(Test.answering)
async def answering(message: Message, state: FSMContext):
    data = await state.get_data()
    q_index = data["q_index"]
    score = data["score"]

    if message.text == "❌ Отменить Test":
        await message.answer(
            f"❌ Тест остановлен.\n\n"
            f"Твой текущий результат: {score} из {len(questions)}",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.clear()
        return

    q = questions[q_index]

    if message.text not in q["options"]:
        await message.answer("⚠ Пожалуйста, выбери вариант ответа с кнопок.")
        return

    if message.text.startswith(q['correct']):
        score += 1

    q_index += 1

    if q_index >= len(questions):
        await message.answer(
            f"🏁 Тест завершён!\n\n"
            f"Твой результат: {score} из {len(questions)}\n\n"
            "Спасибо за участие 🎉",
            reply_markup=ReplyKeyboardRemove()
        )
        await state.clear()
        return

    await state.update_data(q_index=q_index, score=score)

    next_q = questions[q_index]

    kb = ReplyKeyboardBuilder()

    for option in next_q["options"]:
        kb.add(KeyboardButton(text=option))

    kb.add(KeyboardButton(text="❌ Отменить Test"))
    kb.adjust(2, 1)

    await message.answer(
        f"❓ Вопрос {q_index + 1}\n\n{next_q['question']}",
        reply_markup=kb.as_markup(resize_keyboard=True)
    )