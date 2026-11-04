def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []
num = 2
while len(primes) < 50:
    if is_prime(num):
        primes.append(num)
    num += 1

print("First 50 prime numbers:")
for i, prime in enumerate(primes, 1):
    print(f"{prime:3}", end=" ")
    if i % 10 == 0:
        print()