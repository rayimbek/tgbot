import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'telegrambot.settings'
django.setup()

from telegram import Update
from telegram.ext import *
from telegram.ext import Filters
from django.contrib.auth.models import User

from bott.models import CustomUser

# Telegram bot token from BotFather
BOT_TOKEN = "6609283529:AAFsM1DD_4OjDucLnQpadQsdQFEYGj4fdlI"
print('bot started')

# Conversation states
REGISTER_EMAIL, REGISTER_NAME, REGISTER_SURNAME, REGISTER_PHONE, REGISTER_PASSWORD, REGISTER_CONFIRM_PASSWORD = range(6)


def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Welcome to the registration bot. Please provide your email:")
    return REGISTER_EMAIL


def register_email(update: Update, context: CallbackContext) -> int:
    email = update.message.text

    # Basic email validation
    if "@" not in email:
        update.message.reply_text("Invalid email format. Please provide a valid email address.")
        return REGISTER_EMAIL

    # Check if email is unique in the database
    if CustomUser.objects.filter(email=email).exists():
        update.message.reply_text("This email is already registered. Please provide a different email.")
        return REGISTER_EMAIL

    context.user_data['email'] = email
    update.message.reply_text("Great! Now, please provide your first name:")
    return REGISTER_NAME


def register_name(update: Update, context: CallbackContext) -> int:
    context.user_data['first_name'] = update.message.text

    update.message.reply_text("Now, please provide your surname:")
    return REGISTER_SURNAME


def register_surname(update: Update, context: CallbackContext) -> int:
    context.user_data['surname'] = update.message.text
    update.message.reply_text("Now, please provide your telephone number:")
    return REGISTER_PHONE


def register_phone(update: Update, context: CallbackContext) -> int:
    context.user_data['telephone'] = update.message.text
    update.message.reply_text("Finally, please provide your password:")
    return REGISTER_PASSWORD


def register_password(update: Update, context: CallbackContext) -> int:
    context.user_data['password'] = update.message.text
    update.message.reply_text("Please confirm your password:")
    return REGISTER_CONFIRM_PASSWORD


def register_confirm_password(update: Update, context: CallbackContext) -> int:
    password = context.user_data['password']
    confirmed_password = update.message.text

    if confirmed_password is None:
        context.user_data['confirmed_password'] = password
        update.message.reply_text("Please confirm your password:")
        return REGISTER_CONFIRM_PASSWORD
    elif password == confirmed_password:
        email = context.user_data['email']
        first_name = context.user_data['first_name']
        surname = context.user_data['surname']
        telephone = context.user_data['telephone']
        user = User.objects.create_user(username=first_name, email=email, password=password,
                                        first_name=first_name, last_name=surname)
        # Store user data in the database
        custom_user = CustomUser(user= user,email=email   , first_name=first_name, surname=surname, telephone=telephone, password=password)
        custom_user.save()

        update.message.reply_text("You are now registered!")

        return ConversationHandler.END
    else:
        update.message.reply_text("Passwords do not match. Please try again:")
        return REGISTER_CONFIRM_PASSWORD


if __name__ == '__main__':
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            REGISTER_EMAIL: [MessageHandler(Filters.text, register_email)],
            REGISTER_NAME: [MessageHandler(Filters.text, register_name)],
            REGISTER_SURNAME: [MessageHandler(Filters.text, register_surname)],
            REGISTER_PHONE: [MessageHandler(Filters.text, register_phone)],
            REGISTER_PASSWORD: [MessageHandler(Filters.text, register_password)],
            REGISTER_CONFIRM_PASSWORD: [MessageHandler(Filters.text, register_confirm_password)],
        },
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()
