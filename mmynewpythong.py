#!/usr/bin/env python3
"""
Script to print 100 Fibonacci numbers at 2-second intervals.
"""

import time

def generate_fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    """Print 100 Fibonacci numbers at 2-second intervals."""
    fib_numbers = generate_fibonacci(100)
    
    for i, num in enumerate(fib_numbers, 1):
        print(f"Fibonacci({i}): {num}")
        time.sleep(2)

if __name__ == "__main__":
    main()