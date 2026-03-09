from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,FSInputFile,CallbackQuery
from aiogram.fsm.state import StatesGroup,State
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

router_income = Router()

class IncomeStates(StatesGroup):
    amount = State()
    description = State()
    confirmed = State()

@router_income.message(F.text == 'Добавить доход')
async def income_command1(message: Message,state: FSMContext):
    await message.answer("Введите сумму дохода:")
    await state.set_state(IncomeStates.amount)

@router_income.message(IncomeStates.amount)
async def income_command2(message: Message,state: FSMContext):
    await state.update_data(amount=message.text)
    await message.answer("Введите описание дохода:")
    await state.set_state(IncomeStates.description)

@router_income.message(IncomeStates.description)
async def income_command3(message: Message,state: FSMContext):
    await state.update_data(description=message.text)

    data = await state.get_data()

    text = f"""
Подтвердите доход
Сумма: {data['amount']}
Описание: {data['description']}
"""

    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="✅ Подтвердить"),
        KeyboardButton(text="❌ Отменить")
    )

    builder.adjust(2, 2, 1)

    main_menu = builder.as_markup(resize_keyboard=True)

    await message.answer(text,reply_markup=main_menu)
    await state.set_state(IncomeStates.confirmed)

@router_income.message(IncomeStates.confirmed)
async def income_command4(message: Message,state: FSMContext):
    if message.text == "❌ Отменить" :
        await message.answer("❌ Отменено")
        await state.clear()
        return
    data = await state.get_data()
    user_id = message.from_user.id
    """ db save"""
    print(data)
    await message.answer("✅ Доход сохранён")
    await state.clear()
