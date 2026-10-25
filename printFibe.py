"""Print the first 200 prime numbers, one every 30 seconds."""

import time


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def main() -> None:
    count = 0
    candidate = 1
    while count < 200:
        candidate += 1
        if is_prime(candidate):
            count += 1
            print(f"{count}: {candidate}")
            if count < 200:
                time.sleep(30)


if __name__ == "__main__":
    main()
