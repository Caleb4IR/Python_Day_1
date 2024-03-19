import asyncio


# async def hello_world():
#     print("Started 🌍")
#     await asyncio.sleep(3)  # sleep is async function
#     print("Hello World 🌍")


# asyncio.run(hello_world())


# Task countdown
# 3
# 2
# 1
# Happy New Year


# async def new_year():
#     print("3")
#     await asyncio.sleep(1)
#     print("2")
#     await asyncio.sleep(1)
#     print("1")
#     await asyncio.sleep(1)
#     print("HAPPY NEW YEAR🎊")


# asyncio.run(new_year())


# Task 2 - Make it reusable and dry

# async def countdown():
#     for i in range(3, 0, -1):
#         print(i)
#         await asyncio.sleep(1)
#     print("Happy New Year!🎆")


# asyncio.run(countdown())

# Task 3 - Without loop
# DRY: Clue is to create a reusable async function


# async def countdown(number):
#     if number > 0:
#         print(number)
#         await asyncio.sleep(1)
#         await countdown(number - 1)
#     else:
#         print("Happy New Year!")


# async def start_countdown():
#     await countdown(3)

# asyncio.run(start_countdown())


# async def count_and_sleep(message):
#     print(message)
#     await asyncio.sleep(1)  # Sleep --> inbuilt async function


# async def countdown():
#     await count_and_sleep("3")
#     await count_and_sleep("2")
#     await count_and_sleep("1")
#     await count_and_sleep("Happy New Year")


# asyncio.run(countdown())


# async def background_task():
#     print("Start background task")
#     await asyncio.sleep(3)


# async def main():
#     await background_task()
#     # Waiting for background task
#     print("Main function says - Hi")


# asyncio.run(main())


# async def cooking_eggs():
#     print("Egg cooking 🥚")
#     await asyncio.sleep(3)
#     print("Eggs cooked 🍳")


# async def make_coffee():
#     print("Coffee Brewing ☕")
#     await asyncio.sleep(2)
#     print("Coffee Done 🍵")


# # Async with event loop
# async def main():
#     # Request to event loop to schedule task
#     task1 = asyncio.create_task(cooking_eggs())  # Run concurrently
#     task2 = asyncio.create_task(make_coffee())
#     print("Main function says - Hi")
#     print("Main function says - Hi")
#     print("Main function says - Hi")
#     print("Main function says - Hi")
#     await task1

#     #OR
#     # Wait till longest one completes
#     await asyncio.wait({task1, task2}) # Takes in a set


# async def cooking_eggs():
#     print("Egg cooking 🥚")
#     await asyncio.sleep(3)
#     print("Eggs cooked ✅")
#     return f"Data - Eggs 🥚"


# async def make_coffee():
#     print("Coffee brewing ☕")
#     await asyncio.sleep(2)
#     print("Coffee done ✅")
#     return f"Data - Coffee ☕"


# async def make_cereal():
#     print("Making Cereal bowl 🧃")
#     await asyncio.sleep(5)
#     print("Cereal done ✅")
#     return f"Data - Cereal 🧃"


# async def main():
#     # Request to event loop to schedule
#     all_tasks = [
#         asyncio.create_task(cooking_eggs()), # create_task scheduling happens here already
#         asyncio.create_task(make_coffee()),
#         asyncio.create_task(make_cereal()),
#     ]

#     # Waiting for the background_task
#     print("Bread Toast 1")
#     print("Bread Toast 2")
#     print("Bread Toast 3")
#     print("Bread Toast 4")

#     #  Wait till the longest one completes
#     # await asyncio.gather(all_tasks[0], all_tasks[1],  all_tasks[2])
#     # Order of data == Order given in create_task
#     data = await asyncio.gather(*all_tasks) # With gather you can unpack from a list
#     print(data)


# asyncio.run(main())


async def cooking_eggs():
    print("Egg cooking 🥚")
    await asyncio.sleep(3)
    print("Eggs cooked ✅")
    return f"Data - Eggs 🥚"


async def make_coffee():
    print("Coffee brewing ☕")
    await asyncio.sleep(2)
    print("Coffee done ✅")
    return f"Data - Coffee ☕"


async def make_cereal():
    print("Making Cereal bowl 🧃")
    await asyncio.sleep(5)
    print("Cereal done ✅")
    return f"Data - Cereal 🧃"


# All async function returns coroutines
async def main():
    # Request to event loop to schedule
    all_co_routines = [
        cooking_eggs(),
        make_coffee(),
        make_cereal(),
    ]

    # Waiting for the background_task
    print("Bread Toast 1")
    print("Bread Toast 2")
    print("Bread Toast 3")
    print("Bread Toast 4")

    data = await asyncio.gather(  # gather schedules here
        *all_co_routines
    )  # With gather you can unpack from a list
    print(data)


asyncio.run(main())
