# Create function that takes in a number an returns if the number is prime
# or not prime
# For a number to be prime, it cannot be divisible by any number from 2 to the
# number before (x-1)

def prime_nonprime(x):
    Prime = True
    for i in range(2,x-1):
        if x%i == 0:
            Prime = False
    return Prime

print(prime_nonprime(5))
print(prime_nonprime(55))
print(prime_nonprime(250))
print(prime_nonprime(11))

# This function returns the same result, but is more efficient
# The range is chosen to iterate up to the square root of x because any factors
# larger than the square root would pair with factors smaller
# than the square root, and they would have been already checked in the loop.
# If no divisors are found during the loop, the function concludes that x is a prime number, and it returns True.

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False

    return True

print(is_prime(5))
print(is_prime(55))
print(is_prime(250))
print(is_prime(11))
