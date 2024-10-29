from concurrent.futures import ProcessPoolExecutor
import time

def print_num():
    for i in range(5):
        print(i)
        time.sleep(1)  # Simulating a time-consuming task

def print_let():
    for i in 'abcde':
        print(i)
        time.sleep(1)  # Simulating a time-consuming task

# Using ProcessPoolExecutor to run both tasks concurrently in separate processes
with ProcessPoolExecutor(max_workers=2) as executor:
    # Submit each function as a separate process
    future_num = executor.submit(print_num)
    future_let = executor.submit(print_let)

# We don’t need to capture any results, as each function handles output directly.
 