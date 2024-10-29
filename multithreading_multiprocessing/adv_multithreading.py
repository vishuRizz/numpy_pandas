from concurrent.futures import ThreadPoolExecutor
import time

def print_num():
    for i in range(5):
        print(i)
        time.sleep(1)  # Simulating a task that takes time

def print_let():
    for i in 'abcde':
        time.sleep(1)  # Simulating a task that takes time
        print(i)

# Using ThreadPoolExecutor to run both tasks concurrently
with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks individually
    future_num = executor.submit(print_num)
    future_let = executor.submit(print_let)

# We do not need to collect or print results here, as the functions themselves handle output
