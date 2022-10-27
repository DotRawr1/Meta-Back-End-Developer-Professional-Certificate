import time
start_time = time.time()

for x in range(1000):
    for y in range(1000):
        print(0, end = " ")
    print()
    
print(round((time.time() - start_time), 2))