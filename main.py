from random import randint
from re import Match

import pyrootutils
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiohttp import web
from sqlalchemy.dialects.postgresql import insert

from conf.config import Configurator_yml

pyrootutils.setup_root(__file__, indicator=".project", pythonpath=True)
from src.service.service import *

app = web.Application()

TOKEN_API = Configurator_yml().get_bot_token()
bot = Bot(token=TOKEN_API)

Bot.set_current(bot)

dp = Dispatcher(bot)


webhook_path = f"/{TOKEN_API}"


async def set_webhook():
    webhook_uri = f"{Configurator_yml().get_domen()}{webhook_path}"
    await bot.set_webhook(webhook_uri)


async def on_startup(_):
    await set_webhook()


async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind("/")
    token = url[index + 1 :]

    if token == TOKEN_API:
        request_data = await request.json()
        update = types.Update(**request_data)
        await dp.process_update(update)
        return web.Response()

    else:
        return web.Response(status=403)


app.router.add_post(f"/{TOKEN_API}", handle_webhook)
# if __name__ == "__main__":
#     app.on_startup.append(on_startup)
#     web.run_app(
#         app,
#         host="0.0.0.0",Settings
#         port=8000,
#     )

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

dp.register_message_handler(
    lambda message: all_msg(bot, message), content_types={"voice"}
)

dp.register_message_handler(service.send_passion_post, commands={"tell_about_passion"})
dp.register_message_handler(service.send_project_info, commands={"project_info"})

# if __name__ == "__main__":
#     from aiogram import executor

#     # set_bd()
#     executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    app.on_startup.append(on_startup)
    web.run_app(
        app,
        host="0.0.0.0",
        port=8000,
    )
