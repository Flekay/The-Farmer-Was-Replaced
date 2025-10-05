# Sympy

This folder contains functions for mathematical computations using the Sympy library. The functions include calculations for Fibonacci numbers, prime checking, and prime number generation.

## Functions

### fibonacci.py
Calculates the Fibonacci number at a given position.
```python
result = fibonacci(10)  # 55
```

### isprime.py
Checks if a given number is prime.
```python
result = isprime(29)  # True
```

### nextprime.py
Finds the smallest prime greater than a given number.
```python
prime = nextprime(20)  # 23
```

### prevprime.py
Finds the largest prime less than a given number.
```python
prime = prevprime(20)  # 19
```

### primerange.py
Returns a list of prime numbers in the given range.
```python
primes = primerange(10, 50)  # e.g., [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```
