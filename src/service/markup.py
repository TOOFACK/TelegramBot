from aiogram import types


class ReplyMarkup:
    def __init__(self) -> None:
        self.keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    def firstButton(
        self,
    ):
        button = types.KeyboardButton(text="Первая кнопка!")
        self.keyboard.add(button)
        return self.keyboard

    def secondButton(
        self,
    ):
        button1 = types.KeyboardButton(text="Photo from highschool")
        button2 = types.KeyboardButton(text="Last selfie")

        self.keyboard.add(button1, button2)
        return self.keyboard

    def clear(
        self,
    ):
        self.keyboard.clean()
