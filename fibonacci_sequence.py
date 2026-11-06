#!/usr/bin/env python3
"""
Script to print the first 50 Fibonacci numbers with 2-second intervals between each number.
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

def print_fibonacci_with_delay():
    """Print first 50 Fibonacci numbers with 2-second intervals."""
    fib_numbers = generate_fibonacci(50)
    
    print("First 50 Fibonacci numbers:")
    print("-" * 40)
    
    for i, num in enumerate(fib_numbers, 1):
        print(f"F({i}) = {num}")
        if i < 50:  # Don't wait after the last number
            time.sleep(2)
    
    print("-" * 40)
    print("Completed printing 50 Fibonacci numbers!")

if __name__ == "__main__":
    print_fibonacci_with_delay()
