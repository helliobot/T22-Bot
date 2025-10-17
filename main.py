from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import sqlite3

TOKEN = "7981112534:AAG_Nr71zpXC4CQA-KjYK_gUc7wFCpxK0Vk"

def init_db():
    conn = sqlite3.connect('t22.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, xp INTEGER DEFAULT 0)')
    conn.commit()
    conn.close()

async def dashboard(update, context):
    keyboard = [[InlineKeyboardButton("🥇 Leaderboard", callback_data='lb')], [InlineKeyboardButton("🏆 Rank", callback_data='rank')]]
    await update.message.reply_text("🚀 **T22 DASHBOARD**", reply_markup=InlineKeyboardMarkup(keyboard))

async def button(update, context):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text("✅ **T22 LIVE!**")

def main():
    init_db()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("dashboard", dashboard))
    app.add_handler(CallbackQueryHandler(button))
    print("🤖 T22 LIVE!")
    app.run_polling()

if __name__ == '__main__':
    main()
