# Factorial Function
# One time I had a data science interview and one of the questions was to complete
# a factorial function
# It started like this:
# They showed me a Jupyter Notebook and said, can you complete this function?
# def factorial():


# First, we need to specify a variable
def factorial(n):
    # Check if the input is a negative number
    if n < 0:
        return "Factorial is undefined for negative numbers."
# Then we need to specify the base case, when the input is zero
    elif n == 0:
        return 1
# write the recursive part of the function. Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)


# Example usage:
user_input = int(input("Enter a number to calculate its factorial: "))
result = factorial(user_input)
print(result)


# Another way to code this is to use a loop

def factorial_loop(n):
    # Check if the input is a negative number
    if n < 0:
        return "Factorial is undefined for negative numbers."
    
    # Initialize the result to 1
    result = 1
    
    # Calculate the factorial using a loop
    for i in range(1, n + 1):
        result *= i
    
    return result

# Lets time each function to measure which one is faster
# first, import the time module in Python
import time


# Time the recursive implementation
start_time_recursive = time.time()
result_recursive = factorial(1000)  # Change the input as needed
end_time_recursive = time.time()
print(f"Recursive Result: {result_recursive}")
print(f"Recursive Time: {end_time_recursive - start_time_recursive} seconds")

# Time the loop implementation
start_time_loop = time.time()
result_loop = factorial_loop(1000)  # Change the input as needed
end_time_loop = time.time()
print(f"Loop Result: {result_loop}")
print(f"Loop Time: {end_time_loop - start_time_loop} seconds")

# I tested both function's time to complete the 1000! calculation. The loop performs slightly better

# The iterative (loop) implementation is perform better than the recursive implementation for calculating the factorial, especially for large input values.
# This is because Python does not optimize tail recursion, and each recursive call in the factorial_recursive function adds a new frame to the call stack.
# On the other hand, the iterative implementation uses a loop and doesn't rely on the call stack, making it more memory-efficient and avoiding potential issues with recursion depth.
# The time complexity of both implementations is O(n), but the constant factors and memory usage may differ.
