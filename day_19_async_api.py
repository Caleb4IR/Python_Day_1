import requests
from pprint import pprint
import aiohttp
import asyncio


# def get_temperature(city_name):
#     response = requests.get(
#         f"http://api.weatherapi.com/v1/current.json?key=87613a288f054a97bb293328241503&q={city_name}&aqi=no",
#         verify=False,
#     )
#     weather = response.json()

#     return f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"


# print(get_temperature("Cape Town"))
# get_temperature("Johannesburg")


# Async - aiohttp
# async def get_city_temp(city_name):
#     print(f"Getting temp of {city_name}")
#     await asyncio.sleep(2)
#     url = f"http://api.weatherapi.com/v1/current.json?key=87613a288f054a97bb293328241503&q={city_name}&aqi=no"
#     # Menory Management - Error
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             print(
#                 f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"
#             )


# async def main():
#     await get_city_temp("Johannesburg")
#     await get_city_temp("Durban")
#     await get_city_temp("London")


# asyncio.run(main())


# # Task 1
# # Clue: Gather


# async def get_city_temp(city_name):
#     print(f"Getting temp of {city_name}")
#     await asyncio.sleep(2)
#     url = f"http://api.weatherapi.com/v1/current.json?key=87613a288f054a97bb293328241503&q={city_name}&aqi=no"
#     # Menory Management - Error
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             print(
#                 f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"
#             )


# async def main():
#     all_co_routines = [
#         get_city_temp("Johannesburg"),
#         get_city_temp("Durban"),
#         get_city_temp("London"),
#     ]

#     asyncio.gather(*all_co_routines)


# asyncio.run(main())


# # Task 2
# # Clue gather & create_task


# async def get_city_temp(city_name):
#     print(f"Getting temp of {city_name}")
#     await asyncio.sleep(2)
#     url = f"http://api.weatherapi.com/v1/current.json?key=87613a288f054a97bb293328241503&q={city_name}&aqi=no"
#     # Menory Management - Error
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             print(
#                 f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"
#             )


# async def main():
#     all_co_routines = [
#         asyncio.create_task(get_city_temp("Johannesburg")),
#         asyncio.create_task(get_city_temp("Durban")),
#         asyncio.create_task(get_city_temp("London")),
#     ]

#     await asyncio.gather(*all_co_routines)


# asyncio.run(main())

# # Task 3
# # DRY


# async def get_city_temp(city_name):
#     print(f"Getting temp of {city_name}")
#     await asyncio.sleep(2)
#     url = f"http://api.weatherapi.com/v1/current.json?key=87613a288f054a97bb293328241503&q={city_name}&aqi=no"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             print(
#                 f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"
#             )


# async def main(cities):
#     all_coroutines = [get_city_temp(city) for city in cities]
#     await asyncio.gather(*all_coroutines)


# cities = [
#     "New York",
#     "Tokyo",
#     "London",
#     "Paris",
#     "Dubai",
#     "Singapore",
#     "Sydney",
#     "Istanbul",
#     "Hong Kong",
#     "Cape Town",
# ]

# asyncio.run(main(cities))

# Task 4
# Async
# Create a function which takes a list of cities and provides the corresponding temperature in a dictionary

import asyncio
import aiohttp


# async def get_city_temp(city_name):
#     print(f"Getting temp of {city_name}")
#     url = f"http://api.weatherapi.com/v1/current.json?key=87613a288f054a97bb293328241503&q={city_name}&aqi=no"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             weather = await response.json()
#             return city_name, weather["current"]["temp_c"]


# async def main(cities):
#     temperatures = await asyncio.gather(*[get_city_temp(city) for city in cities])
#     return dict(temperatures)


# cities = [
#     "New York",
#     "Tokyo",
#     "London",
#     "Paris",
#     "Dubai",
#     "Singapore",
#     "Sydney",
#     "Istanbul",
#     "Hong Kong",
#     "Cape Town",
# ]

# temperatures = asyncio.run(main(cities))
# pprint(temperatures)


# # Task 5
# async def fetch_users():
#     url = "https://65f8284cb4f842e808871337.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return users


# async def main():
#     user_data = await fetch_users()
#     user_names = [user["name"] for user in user_data]

#     pprint("\n".join(user_names))


# asyncio.run(main())


# Delete user ID 15 with async


# async def delete_user_by_id(id):
#     url = f"https://65f8284cb4f842e808871337.mockapi.io/users/{id}"
#     async with aiohttp.ClientSession() as session:
#         async with session.delete(url) as response:
#             user = await response.json()
#             return user


# async def main(id):
#     user = await delete_user_by_id(id)
#     pprint(user)


# asyncio.run(main(10))

# Task 1
# Delete the first 5 users
# Performant < 0.5s


# async def get_users():
#     url = f"https://65f8284cb4f842e808871337.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             return users


# async def delete_user_by_id(id):
#     url = f"https://65f8284cb4f842e808871337.mockapi.io/users/{id}"
#     print(f"Deleting user...{id}")
#     async with aiohttp.ClientSession() as session:
#         async with session.delete(url) as response:
#             user = await response.json()
#             return user


# Task - 1
# Delete the first 5 users
# Performant < 0.5s
# Clue: 2 Steps
# Clue: GET & Delete


# async def main():
#     users = await get_users()
#     first_five_users = users[:5]  # slice
#     first_five_users_co_routine = [
#         delete_user_by_id(user["id"]) for user in first_five_users
#     ]
#     deleted_users = await asyncio.gather(*first_five_users_co_routine)
#     pprint(deleted_users)
#     # pprint(first_five_users)
#     # print(len(first_five_users))


# asyncio.run(main())


# Task
# Create user


# async def create_user(new_user):
#     print(new_user)
#     url = f"https://65f8284cb4f842e808871337.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=new_user) as response:
#             user = await response.json()
#             return user


# async def main():
#     new_user = {
#         "name": "Caleb",
#         "avatar": "https://avatars.githubusercontent.com/u/113150837?v=4",
#     }
#     user_data = await create_user(new_user)
#     print(user_data)

# asyncio.run(main())

# Task 2
# Create 5 users
# user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]


# async def create_user(new_user):
#     url = "https://65f8284cb4f842e808871337.mockapi.io/users"
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=new_user) as response:
#             user = await response.json()
#             return user


# async def main():
#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     avatar_url = "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg"
#     new_users = [{"name": name, "avatar": avatar_url} for name in user_list]

#     user_tasks = [create_user(user) for user in new_users]
#     user_data = await asyncio.gather(*user_tasks)
#     print(user_data)


# asyncio.run(main())


# async def main():
#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     flag_url = "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg"

#     user_co_routines = []
#     for user_name in user_list:
#         new_user = {
#             "name": user_name,
#             "avatar": flag_url
#         }

#         user_co_routines.append(create_user(new_user))
#     users_data = await asyncio.gather(*user_co_routines)
#     print(users_data)

# asyncio.run(main())

# # OR List Comprehension

# async def main():
#     user_list = ["Alex", "Gemma", "Thato", "Lilitha", "Dhara"]
#     flag_url = "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg"

#     user_co_routines = [create_user({ "name": user_name, "avatar": flag_url})for user_name in user_list]

#     users_data = await asyncio.gather(*user_co_routines)
#     print(users_data)

# asyncio.run(main())


# Update to change the avatar link to a picture of human rights flag


async def get_users():
    url = "https://65f8284cb4f842e808871337.mockapi.io/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def update_avatar(user_id, new_avatar_link):
    url = f"https://65f8284cb4f842e808871337.mockapi.io/users/{user_id}"
    data = {"avatar": new_avatar_link}
    async with aiohttp.ClientSession() as session:
        async with session.put(url, json=data) as response:
            return await response.json()


async def main():
    users = await get_users()
    avatar_url = "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg"  # Replace with the new avatar link
    tasks = [update_avatar(user["id"], avatar_url) for user in users]
    await asyncio.gather(*tasks)


asyncio.run(main())
