import telebot
import time

bot_token = "5958984310:AAHys8YPS9hSAKPmYNei_EgkCO2_LT3tPVs"
bot = telebot.TeleBot(bot_token)

# Handle the '/start' command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to the Pizza Delivery Bot! Type /menu to see our menu.")

# Handle the '/menu' command
@bot.message_handler(commands=['menu'])
def menu(message):
    menu_text = "Pizza Menu:\n\n1. Margherita - $10\n2. Pepperoni - $12\n3. Veggie - $11\n4. BBQ Chicken - $13\n5. Meat Lovers - $14\n\nType /order [pizza number] to place an order."
    bot.reply_to(message, menu_text)

# Handle the '/order' command
@bot.message_handler(commands=['order', 'Order'])
def order(message):
    try:
        order_number = int(message.text.split()[1])
        order_time_client = time.strftime("%H:%M:%S")
        order_time = time.strftime("%Y-%m-%d %H:%M:%S")
        if order_number < 1 or order_number > 5:
            raise ValueError
        bot.reply_to(message, f'Your order № {order_number} at {order_time_client} has been placed! Your pizza will be delivered in 30 minutes.')
        print(f'Order for pizza № {order_number} at {order_time} has been placed')

    except (IndexError, ValueError):
        bot.reply_to(message, "Invalid order number. Type /menu to see the menu.")

# Start polling for updates
bot.polling()
