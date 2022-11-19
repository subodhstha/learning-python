from threading import Thread
import time
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)
        
threads = []
num_threads = 10

# create processes
for i in range(num_threads):
    thread = Thread(target=square_numbers)
    threads.append(thread)
    
# start
for thread in threads:
    thread.start()
    
# join 
for thread in threads:
    thread.join()
    
print("End main")
