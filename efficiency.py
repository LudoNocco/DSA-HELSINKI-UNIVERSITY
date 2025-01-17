#The course material includes two different ways to implement the function count_even:

#Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen numbers.
#In this exercise, you get a point automatically when you submit the test results and the code that you used.
#Implementation 1 run time:  s
#Implementation 2 run time:  s
#The code you used in the test:
 
import time
import numpy as np

def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__ == "__main__":
    random_numbers = np.random.randint(0, 101, size=10_000_000).tolist()

    start_time = time.time()
    result1 = count_even1(random_numbers)
    end_time = time.time()
    print(f"count_even1 result: {result1}, runtime: {end_time - start_time:.6f} s")

    start_time = time.time()
    result2 = count_even2(random_numbers)
    end_time = time.time()
    print(f"count_even2 result: {result2}, runtime: {end_time - start_time:.6f} s")