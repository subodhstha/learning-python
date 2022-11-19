# from multiprocessing import Process
# import os
# import time
# def square_numbers():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count()

# # create processes
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)
    
# # start
# for p in processes:
#     p.start()

# # join
# for p in processes:
#
#     p.join()

# print("end main")


from multiprocessing import Process
import os
def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()






# from threading import Thread
# import time
# def square_numbers():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)
        
# threads = []
# num_threads = 10

# # create processes
# for i in range(num_threads):
#     t = Thread(target=square_numbers)
#     threads.append(t)
    
# # start
# for t in threads:
#     t.start()
    
# # join 
# for t in threads:
#     t.join()
    
# print("End main")
