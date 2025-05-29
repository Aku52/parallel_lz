import asyncio
import random

async def read_file(file_name):
    
    delay = random.uniform(0.1, 5) 
    await asyncio.sleep(delay) 
    print(f"Файл {file_name} прочитан за {delay}")

async def create_read():
    quantity_files = 10  
    tasks = [read_file(f"file_{i}.txt") for i in range(quantity_files)]
    await asyncio.gather(*tasks)

# Запуск асинхронного чтения
asyncio.run(create_read())

