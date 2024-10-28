import time
import threading

def print_num():
    for i in range(5):
        print(i)
        time.sleep(1) # analogy with some actual task that requires time to execute
def print_let():
    for i in 'abcde':
        time.sleep(1) # analogy with some actual task that requires time to execute
        print(i)
# create two threads
t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_let)
#start the thread
t1.start()
t2.start()
# wait for the threads to complete
t1.join()
t2.join()