"""primes=[]
count=0
for num in range(3000,7001):
    is_prime=True
    if num<=1:
        is_prime=False
    else:
        i=2
        while i*i<=num:
            if num%i==0:
                is_prime=False
                break
            i+=1
    if is_prime:
        primes.append(num)
        count+=1
print("Prime numbers between 3000 and 7000:")
print(primes)
print("Total count of prime numbers:")
print(count)

print("\nTotal count of prime numbers:")
print(count)"""


"""count = 0
for num in range(3000, 7001):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=' ')
            count += 1
print("\nTotal primes:", count)"""

"""import time

start_time=time.time()

count=0
total_iterations=0
steps=0

primes=[]

for num in range(3000,7001):
    steps+=1
    if num>1:
        is_prime=True
        steps+=1
        for i in range(2,num):
            total_iterations+=1
            steps+=1
            if num%i==0:
                steps+=1
                is_prime=False
                steps+=1
                break
        if is_prime:
            steps+=1
            count+=1
            primes.append(num)
            steps+=1

end_time=time.time()

execution_time=end_time-start_time

print("Total primes:", count)
print("Execution time:", execution_time, "seconds")
print("Total steps:", steps)
print("Total iterations", total_iterations)
print("Primes are:", primes)"""

"""import time

start_time = time.time()

count = 0
total_iterations = 0
steps = 0
primes = []

for num in range(3000, 7001):
    steps += 1  # Count each number checked
    if num > 1:
        is_prime = True
        # Only check for divisors up to the square root of num
        i = 2
        while i * i <= num:
            total_iterations += 1
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            count += 1
            primes.append(num)

end_time = time.time()
execution_time = end_time - start_time

print("Total primes:", count)
print(f"Execution time", execution_time, "seconds")
print("Total numbers of steps:", steps, "Total divisibility checks (iterations):", total_iterations)
print("Total divisibility checks (iterations):", total_iterations)
print("Primes are:", primes)"""


"""# The number for which to find the factorial
n = int(input("Enter a number:"))

# --- Initialize metrics ---
steps = 0
outer_loops = 0
inner_loops = 0

result = 1

# --- Main factorial loop ---
# This is our outer loop
outer_loops += 1
steps += 1  # Step for initializing the result variable and starting the loop

for i in range(1, n + 1):
    steps += 1  # Step for each iteration of the loop
    result *= i

# --- Print results ---
print("Factorial of", n, "is:", result)
print("Total Steps:", steps)
print("Outer Loops:", outer_loops)
print("Inner Loops:", inner_loops)
print("Total Iterations:", n)"""
