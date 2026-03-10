from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from keyboards.reply_keyboards import cancel_kb,confirm_kb
from aiogram.types import  ReplyKeyboardRemove
router_income = Router()


class IncomeStates(StatesGroup):
    amount = State()
    description = State()
    confirmed = State()

@router_income.message(Command("cancel"))
@router_income.message(F.text == "❌ Отменить")
async def cancel(message: Message, state: FSMContext):
    await message.answer("❌ Действие отменено.")
    await state.clear()

@router_income.message(F.text == "Добавить доход")
async def income_start(message: Message, state: FSMContext):
    await message.answer(
        "💰 Введите сумму дохода:",
        reply_markup=cancel_kb()
    )
    await state.set_state(IncomeStates.amount)


@router_income.callback_query(F.data == "add")
async def income_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "💰 Введите сумму дохода:",
        reply_markup=cancel_kb()
    )
    await state.set_state(IncomeStates.amount)
    await callback.answer()


@router_income.message(IncomeStates.amount)
async def income_amount(message: Message, state: FSMContext):

    if message.text == "❌ Отменить":
        await cancel(message, state)
        return

    if not message.text.isdigit():
        await message.answer("⚠️ Пожалуйста, введите **только число**.\nНапример: 5000")
        return

    await state.update_data(amount=message.text)

    await message.answer(
        "📝 Введите описание дохода:",
        reply_markup=cancel_kb()
    )

    await state.set_state(IncomeStates.description)


@router_income.message(IncomeStates.description)
async def income_description(message: Message, state: FSMContext):

    if message.text == "❌ Отменить":
        await cancel(message, state)
        return

    await state.update_data(description=message.text)

    data = await state.get_data()

    text = (
        "📊 Подтвердите добавление дохода:\n\n"
        f"💰 Сумма: {data['amount']}\n"
        f"📝 Описание: {data['description']}\n\n"
        "Подтвердить?"
    )

    await message.answer(text, reply_markup=confirm_kb())

    await state.set_state(IncomeStates.confirmed)


@router_income.message(IncomeStates.confirmed)
async def income_confirm(message: Message, state: FSMContext):

    if message.text == "❌ Отменить":
        await cancel(message, state)
        return

    if message.text != "✅ Подтвердить":
        await message.answer("Пожалуйста, выберите кнопку ниже.")
        return

    data = await state.get_data()
    user_id = message.from_user.id
    print(user_id, data)

    await message.answer("✅ Доход успешно сохранён.", reply_markup=ReplyKeyboardRemove())

    await state.clear()