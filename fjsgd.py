import random
import threading
import time
import random
import numpy as np

def write_file(file_name,data):
    f= open(file_name,'w')
    f.write(data)
    time.sleep(1)
    f.close()

start = time.time()

for i in range(10):
    with f"potok_{i}.txt" as file:
        print("The 100 random integers written are: ")
        for i in range(100):
            line = str(random.randint(1,100))
            file.write(line)
            file.write("\n")
            print(line)

    write_file(f"potok_{i}.txt", line )
               

delta = time.time()-start
print(f"simple time of writing {i+1} files is:{delta}")