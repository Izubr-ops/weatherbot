import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import ApplicationBuilder, InlineQueryHandler, ContextTypes

from Token import TOKEN
from weatherDef import weather

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query
    if query == "":
        results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Moscow",
            input_message_content=InputTextMessageContent(weatherMos),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Tokyo⛩",
            input_message_content=InputTextMessageContent(weatherTok),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="New York",
            input_message_content=InputTextMessageContent(weatherNY),
        )]

    else:

        results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="Your city",
            input_message_content=InputTextMessageContent(weather(query))
        )]
    await update.inline_query.answer(results)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    weatherTok = weather("Tokyo")
    weatherMos = weather("Moscow")
    weatherNY = weather("New York")
    application.add_handler(InlineQueryHandler(inline_query))
    application.run_polling()