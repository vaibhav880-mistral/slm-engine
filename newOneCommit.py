def fibonacci_up_to(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for number in fibonacci_up_to(100):
        print(number)
