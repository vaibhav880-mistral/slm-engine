#!/usr/bin/env python3
"""
Script to print the first 100 Fibonacci numbers with a 2-second interval between each.
"""

import time

def fibonacci(n):
    """Generate the first n Fibonacci numbers."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    """Print first 100 Fibonacci numbers with 2-second intervals."""
    fib_numbers = fibonacci(100)
    
    for i, num in enumerate(fib_numbers, 1):
        print(f"Fibonacci({i}): {num}")
        if i < 100:  # No delay after the last number
            time.sleep(2)

if __name__ == "__main__":
    main()