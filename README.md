# tgbot

# Telegram Bot User Registration

This Django project demonstrates how to create a Telegram bot for user registration and integrate it with the Django authentication system. Users can register their accounts by providing their email, first name, surname, telephone, and password through the bot.

## Prerequisites

Before running the bot, ensure you have the following prerequisites installed:

- Python (3.7 or higher)
- Django
- `python-telegram-bot` library

You can install the required Python packages using `pip`:

```bash
pip install django python-telegram-bot

Getting Started
Follow these steps to set up and run the Telegram bot for user registration:

1.Clone the repository:
git clone https://github.com/yourusername/telegram-bot-registration.git
cd telegram-bot-registration


Certainly! Here's the README.md text in a more copy-friendly format:

markdown
Copy code
# Telegram Bot User Registration

This Django project demonstrates how to create a Telegram bot for user registration and integrate it with the Django authentication system. Users can register their accounts by providing their email, first name, surname, telephone, and password through the bot.

## Prerequisites

Before running the bot, ensure you have the following prerequisites installed:

- Python (3.7 or higher)
- Django
- `python-telegram-bot` library

You can install the required Python packages using `pip`:

pip install django python-telegram-bot

bash
Copy code

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/telegram-bot-registration.git
   cd telegram-bot-registration

2.Configure your Django project settings in settings.py:

Set your Django secret key.
Add your app to the INSTALLED_APPS list.
Configure your database settings.
3.Create and apply database migrations:
python manage.py makemigrations
python manage.py migrate
4.Create a superuser for accessing the Django admin panel:
python manage.py createsuperuser
5.Create a bot with the BotFather on Telegram and obtain your bot token.
6.Replace "YOUR_BOT_TOKEN" in the bot.py file with your bot token.
7..Start the Django development server:
python manage.py runserver
Access the Django admin panel at http://localhost:8000/admin/ and log in using the superuser credentials created earlier.

Create CustomUser records in the admin panel to simulate user registrations via the Telegram bot.

Start the Telegram bot by running

python bot.py

Certainly! Here's the README.md text in a more copy-friendly format:

markdown
Copy code
# Telegram Bot User Registration

This Django project demonstrates how to create a Telegram bot for user registration and integrate it with the Django authentication system. Users can register their accounts by providing their email, first name, surname, telephone, and password through the bot.

## Prerequisites

Before running the bot, ensure you have the following prerequisites installed:

- Python (3.7 or higher)
- Django
- `python-telegram-bot` library


bash
Copy code

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rayimbek/tgbot.git
   cd telegrambot

pip install django
pip install djangorestframework
pip install djoser

You can install the required Python packages using `pip`:

pip install django python-telegram-bot


python manage.py makemigrations
python manage.py migrate
Create a superuser for accessing the Django admin panel:

python manage.py createsuperuser
Create a bot with the BotFather on Telegram and obtain your bot token.

Replace "YOUR_BOT_TOKEN" in the bot.py file with your bot token.

Start the Django development server:

python manage.py runserver
Access the Django admin panel at http://localhost:8000/admin/ and log in using the superuser credentials created earlier.

Create CustomUser records in the admin panel to simulate user registrations via the Telegram bot.

Start the Telegram bot by running:

python bot.py

##Usage
Start a conversation with your Telegram bot by sending the /start command.

Follow the prompts to provide your email, first name, surname, telephone, and password for registration.

The bot will create a new user account based on the provided information and store it in the database.

You can access the registered users in the Django admin panel.

##Contributing
Contributions are welcome! If you'd like to improve this project or report issues, please open an issue or submit a pull request.
