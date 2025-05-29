import threading
import time
import random

def write_file(file_name):
    # Записывает 100 случайных чисел в файл
    with open(file_name, "w") as f:
        numbers = [str(random.randint(1, 100)) for _ in range(100)]
        f.write("\n".join(numbers))

# Однопоточная запись
start = time.time()
for i in range(10):
    write_file(f"file_single_{i}.txt")

single_time = time.time() - start


# Многопоточная запись
start = time.time()
threads = []
for i in range(10):
    thread = threading.Thread(target=write_file, args=(f"file_multi_{i}.txt",))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join()

multi_time = time.time() - start

print(f"Сравнение времени выполнения:")
print(f"Однопоточный режим: {single_time}")
print(f"Многопоточный режим: {multi_time}")

