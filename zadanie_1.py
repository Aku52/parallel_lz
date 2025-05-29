import threading
import time
import random
import numpy as np


def write_file(file_name,data):
    f= open(file_name,'w')
    f.write(data)
    time.sleep(1)
    f.close()

#Общая запись

'''with open(file_name, "w") as afile:
    print("The 100 random integers written are: ")
    for i in range(100):
        line = str(random.randint(1,100))
        afile.write(line)
        afile.write("\n")
        print(line)

    '''
start = time.time()
for i in range(10):
    write_file(f"potok_{i}.txt")

results=[]
for i in range(1,7000000):
    a=(random.sample(range(1, 45), 6))
    results.append(a)

delta = time.time()-start
print(f"simple time of writing {i+1} files is:{delta}")


#Многопоточная запись
start = time.time()
threads=[]
for i in range(10):
    thread = threading.Thread(target=write_file,arges=(f"simple time of writing {i+1} files is:{delta}"))
    thread.start()
    threads.append(thread)

choices = tuple(range(1, 45)) 
results = []
for i in range(1, 7000000):
    a = random.sample(choices, 6)
    results.append(a)

#esults = np.random.randint(1, 45, (7000000, 6), np.uint8)

for t in threads:
    t.join()

delta= time.time()-start
print(f"simple time of writing {i+1} files is:{delta}")