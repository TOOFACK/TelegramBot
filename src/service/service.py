import pyrootutils
from aiogram import Bot, Dispatcher, types
from sqlalchemy import select, text
from sqlalchemy.dialects.postgresql import insert

pyrootutils.setup_root(__file__, indicator=".project", pythonpath=True)
from src.db_controller.db import Session, engine
from src.db_controller.tables import Content
from src.service.markup import ReplyMarkup
from src.service.service import *


class Service:
    def __init__(self, bot: Bot) -> None:
        self.content_controller = ContentController()
        self.bot = bot

    async def send_info(self, message):
        await message.answer(
            "Awailable commands \
            \n /show_photo \
            \n /explain_GPT \
            \n /sql_vs_nosql \
            \n /love_story \
            \n /tell_about_passion\
            \n /project_info"
        )

    # show photos
    async def pick_photo(self, message: types.Message):
        keyboard = ReplyMarkup()
        await message.answer("Pick photo to show", reply_markup=keyboard.secondButton())

    async def send_selfie(self, message):
        await self.bot.send_photo(
            chat_id=message.from_user.id,
            photo=self.content_controller.select_data("last_selfie")
            # "AgACAgIAAxkBAAPcZNdawdne4wjELq0MFvQD1wFBHLoAAvLIMRvfnLhKWY9OAq6w1e8BAAMCAAN5AAMwBA",
            # reply_markup=types.ReplyKeyboardRemove(),
        )

    async def send_highschool_photo(self, message):
        await self.bot.send_photo(
            chat_id=message.from_user.id,
            photo=self.content_controller.select_data("photo_from_highschool"),
            # reply_markup=types.ReplyKeyboardRemove(),
        )

    # explain gpt
    async def send_how_gpt_work(self, message: types.Message):
        await self.bot.send_voice(
            chat_id=message.from_user.id,
            voice=self.content_controller.select_data("voice_gpt"),
            reply_markup=types.ReplyKeyboardRemove(),
        )

    # love story
    async def send_love_story(self, message: types.Message):
        await self.bot.send_voice(
            chat_id=message.from_user.id,
            voice=self.content_controller.select_data("love_story"),
            reply_markup=types.ReplyKeyboardRemove(),
        )

    # sql vs nosql
    async def explain_sql_nosql(self, message: types.Message):
        await self.bot.send_voice(
            chat_id=message.from_user.id,
            voice=self.content_controller.select_data("nosql_vs_sql"),
            reply_markup=types.ReplyKeyboardRemove(),
        )

    async def send_project_info(self, message: types.Message):
        await self.bot.send_message(
            chat_id=message.from_user.id,
            text=self.content_controller.select_data("repo_url"),
            reply_markup=types.ReplyKeyboardRemove(),
        )

    async def send_passion_post(self, message: types.Message):
        await self.bot.send_message(
            chat_id=message.from_user.id,
            text=self.content_controller.select_data("passion_story"),
            reply_markup=types.ReplyKeyboardRemove(),
        )


class ContentController:
    def __init__(
        self,
    ) -> None:
        self.session = Session()

    def select_data(self, key):
        query = select(Content).where(Content.content_name == key)
        res = self.session.execute(query)
        all_rows = res.fetchone()
        return all_rows[0].content_value

    def insert_data(self, data):
        query = text(
            f"INSERT INTO content (content_name, content_value) VALUES (:content_name, :content_value)"
        )
        try:
            self.session.execute(query, data)
            self.session.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.session.rollback()

        self.session.close()


async def all_msg(bot: Bot, message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=message)
