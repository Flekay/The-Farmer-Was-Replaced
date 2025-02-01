# Sympy

This folder contains functions that are useful for working with prime numbers.

## Functions

### primerange.py
Returns a list of prime numbers in the given range.
```python
primes = primerange(10, 50)  # e.g., [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

### prevprime.py
Finds the largest prime less than a given number.
```python
prime = prevprime(20)  # 19
```

### nextprime.py
Finds the smallest prime greater than a given number.
```python
prime = nextprime(20)  # 23
```

### isprime.py
Checks if a given number is prime.
```python
result = isprime(29)  # True
```
