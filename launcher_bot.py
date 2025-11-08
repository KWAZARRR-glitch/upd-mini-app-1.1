import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# ⚠️ ЗАМЕНИ ЭТИ ЗНАЧЕНИЯ НА СВОИ ⚠️
BOT_TOKEN = "7538452613:AAH6PafgCJ8eB5bI3kAmXb2PxR9tYzqABCD"  # Твой токен от @BotFather
MINI_APP_URL = "https://твой-логин.github.io/clicker-prestige-fixed"  # Твой GitHub Pages

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    # Создаем кнопку для Mini App
    markup = InlineKeyboardMarkup()
    
    web_app_button = InlineKeyboardButton(
        text="🎮 ЗАПУСТИТЬ КЛИКЕР", 
        web_app=WebAppInfo(url=MINI_APP_URL)
    )
    markup.add(web_app_button)

    # Отправляем сообщение с кнопкой
    bot.send_message(
        message.chat.id,
        "🎮 *Добро пожаловать в Мега Кликер!*\n\n"
        "Нажмите кнопку ниже чтобы начать играть:\n"
        "👇👇👇",
        parse_mode='Markdown',
        reply_markup=markup
    )

@bot.message_handler(commands=['game', 'play'])
def game_command(message):
    """Альтернативные команды для запуска"""
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        "🚀 ИГРАТЬ", 
        web_app=WebAppInfo(url=MINI_APP_URL)
    ))

    bot.send_message(
        message.chat.id,
        "Запускаем игру...",
        reply_markup=markup
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    """Помощь"""
    help_text = """
🎮 *Мега Кликер - Помощь*

*Команды:*
/start - Запустить игру
/game - Альтернативный запуск  
/help - Эта справка

*Игра открывается в Mini App прямо в Telegram!*
    """
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

# Запуск бота
if name == "main":
    print("🤖 Бот-запускатель запущен!")
    print("📍 Команда /start откроет Mini App")
    print("🚀 Ожидаю сообщений...")
    bot.polling(none_stop=True)