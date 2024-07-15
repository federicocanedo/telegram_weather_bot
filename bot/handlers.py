from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from weather.api import get_weather
from bot.counter import increment_counter, get_counter


async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Obtener Clima", callback_data='weather')],
        [InlineKeyboardButton("Mostrar Contador de Uso", callback_data='counter')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Hola! Use los botones a continuación.', reply_markup=reply_markup)


async def menu_button(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'weather':
        await query.edit_message_text(text="Por favor, enviar el nombre de la ciudad.")
        context.user_data['awaiting_city'] = True
    elif query.data == 'counter':
        count = get_counter()
        await query.edit_message_text(text=f"El comando de clima ha sido utilizado {count} veces.")


async def handle_message(update, context):
    if ('awaiting_city' in context.user_data) and (context.user_data['awaiting_city']):
        city = update.message.text
        weather_info = get_weather(city)
        await update.message.reply_text(weather_info)
        context.user_data['awaiting_city'] = False
        increment_counter()
    else:
        await update.message
