# tgbot

# Telegram Bot User Registration

This Django project demonstrates how to create a Telegram bot for user registration and integrate it with the Django authentication system. Users can register their accounts by providing their email, first name, surname, telephone, and password through the bot.

## Prerequisites

Before running the bot, ensure you have the following prerequisites installed:

- Python (3.7 or higher)
- Django
- `python-telegram-bot` library
- 
## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rayimbek/tgbot.git
   cd telegrambot


2. **Installation:**

   ```bash
   pip install django
   pip install djangorestframework
   pip install djoser

3. **You can install the required Python packages using `pip`::**


   ```bash
   pip install python-telegram-bot

4. **Make migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Create a superuser for accessing the Django admin panel::**

   ```bash
   python manage.py createsuperuser
6. **Start the Django development server:**
   ```bash
   python manage.py runserver
   
Access the Django admin panel at http://localhost:8000/admin/ and log in using the superuser credentials created earlier.

Create CustomUser records in the admin panel to simulate user registrations via the Telegram bot.

7. **Start the Telegram bot by running:**
   ```bash
   python telegrambot.py
   the username: @raikodrf_bot
## Usage
Start a conversation with your Telegram bot by sending the /start command.

Follow the prompts to provide your email, first name, surname, telephone, and password for registration.

The bot will create a new user account based on the provided information and store it in the database.

You can access the registered users in the Django admin panel.

## Contributing
Contributions are welcome! If you'd like to improve this project or report issues, please open an issue or submit a pull request.
