from random import randint
from re import Match

import pyrootutils
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.executor import start_webhook
from aiohttp import web
from sqlalchemy.dialects.postgresql import insert

from conf.config import Configurator_yml

pyrootutils.setup_root(__file__, indicator=".project", pythonpath=True)
from src.service.service import *

token = Configurator_yml().get_bot_token()
bot = Bot(token)
dp = Dispatcher(bot)
WEBHOOK_DOMAIN = Configurator_yml().get_domen()
WEBAPP_HOST = "127.0.0.1"
WEBAPP_PORT = "8000"


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_DOMAIN, drop_pending_updates=True)


async def on_shutdown(dp):
    await bot.delete_webhook()


service = Service(bot)

dp.register_message_handler(service.send_info, commands={"start", "help"})
dp.register_message_handler(service.pick_photo, commands={"show_photo"})
dp.register_message_handler(service.send_selfie, regexp="Last selfie")
dp.register_message_handler(
    service.send_highschool_photo, regexp="Photo from highschool"
)
dp.register_message_handler(service.send_how_gpt_work, commands={"explain_GPT"})
dp.register_message_handler(service.explain_sql_nosql, commands={"sql_vs_nosql"})
dp.register_message_handler(service.send_love_story, commands={"love_story"})


dp.register_message_handler(service.send_passion_post, commands={"tell_about_passion"})
dp.register_message_handler(service.send_project_info, commands={"project_info"})

if __name__ == "__main__":
    from aiogram import executor

    executor.start_polling(dispatcher=dp, skip_updates=True)
    # start_webhook(
    #     dispatcher=dp,
    #     webhook_path="",
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT,
    # )
