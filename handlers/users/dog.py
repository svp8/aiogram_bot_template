from aiogram import types
from loader import dp
import requests



@dp.message_handler()
async def message(message: types.Message):
    # Command '/start' handler
    # The API endpoint
    url = "https://random.dog/woof.json"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json['url'])

    await message.answer(response_json['url'])
