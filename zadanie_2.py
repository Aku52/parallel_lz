import multiprocessing
import time
import random
import string

def write_file(lock, file_name, num_chars):
    # Записывает случайные символы в один файл без конфликтов
    random_chars = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_chars))
    
    with lock: 
        with open(file_name, "a") as f:
            f.write(random_chars )
            
# 10 - количество процессов, ограничиваем количество случайных символов: их будет 100
def record (file_name="parent_file.txt", quantity_process=10, quantity__chars=100):
    lock = multiprocessing.Lock() 
    
    spisok_process = []
    start = time.time()
    
    for _ in range(quantity_process):
        new_process = multiprocessing.Process(target=write_file, args=(lock, file_name, quantity__chars))
        new_process.start()
        spisok_process.append(new_process)

    for p in spisok_process:
        p.join()

    delta= time.time() - start
    print(f"Время синхронизации: {delta} ")

if __name__ == "__main__":
    record()



