from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, KeyboardButton
from aiogram.fsm.state import StatesGroup, State
from keyboards.reply_keyboards import cancel_kb,confirm_kb
from aiogram.types import  ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router_expense = Router()

class ExpenseStates(StatesGroup):
    amount = State()
    category = State()
    description = State()
    confirmed = State()

@router_expense.message(F.text == "Добавить расход")
async def expense_start(message: Message, state: FSMContext):
    await message.answer("💸 Введите сумму расхода:",reply_markup=cancel_kb())
    await state.set_state(ExpenseStates.amount)

@router_expense.callback_query(F.data == "minus")
async def income_callback(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "💰 Введите сумму расхода:",
        reply_markup=cancel_kb()
    )
    await state.set_state(ExpenseStates.amount)
    await callback.answer()

@router_expense.message(ExpenseStates.amount)
async def expense_amount(message: Message, state: FSMContext):

    if message.text == "❌ Отменить":
        await message.answer("❌ Отменено")
        await state.clear()
        return

    if not message.text.isdigit():
        await message.answer("Введите число. Например: 500")
        return

    await state.update_data(amount=message.text)

    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="🍔 Еда"),
        KeyboardButton(text="🚕 Транспорт"),
        KeyboardButton(text="🎮 Развлечения"),
        KeyboardButton(text="🛒 Покупки"),
        KeyboardButton(text="❌ Отменить")
    )
    builder.adjust(2)

    await message.answer(
        "Выберите категорию:",
        reply_markup=builder.as_markup(resize_keyboard=True)
    )

    await state.set_state(ExpenseStates.category)

@router_expense.message(ExpenseStates.category)
async def expense_category(message: Message, state: FSMContext):
    if message.text == "❌ Отменить":
        await message.answer("❌ Отменено")
        await state.clear()
        return
    await state.update_data(category=message.text)
    await message.answer("Введите описание расхода:", reply_markup=cancel_kb())
    await state.set_state(ExpenseStates.description)


@router_expense.message(ExpenseStates.description)
async def expense_description(message: Message, state: FSMContext):
    if message.text == "❌ Отменить":
        await message.answer("❌ Отменено")
        await state.clear()
        return
    await state.update_data(description=message.text)
    data = await state.get_data()

    text = f"""
    📊 Подтвердите расход

    💸 Сумма: {data['amount']}
    📂 Категория: {data['category']}
    📝 Описание: {data['description']}
    """

    await message.answer(
        text,
        reply_markup=confirm_kb(),
    )

    await state.set_state(ExpenseStates.confirmed)

@router_expense.message(ExpenseStates.confirmed)
async def expense_confirm(message: Message, state: FSMContext):
    if message.text == "❌ Отменить":
        await message.answer("❌ Отменено")
        await state.clear()
        return

    data = await state.get_data()
    print(data)

    await message.answer("✅ Расход сохранён",reply_markup=ReplyKeyboardRemove())

    await state.clear()