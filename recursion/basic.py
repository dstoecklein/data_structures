"""
step 1: identify recursive case:
step 2: the stop criterion
step 3: uninentional case
"""


def factorial(n):
    """
    Product of all positive integers, less than or equal to n
    Example: 4! -> 4*3*2*1 = 24
    """
    assert isinstance(n, int) and n >= 0, "The number must be a positive integer!"

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    """
    The sum of proceeding nums
    Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    f(n) = f(n-1) + f(n-2)
    """
    assert isinstance(n, int) and n >= 0 , "The number must be a positive integer!"
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sum_of_digits(n):
    """
    Find the sum of digits of a positive integer
    Example: 10 = 1 + 0, 54 = 5 + 4, 112 = 1+1+2
    f(n) = n%10 + f(n/10)
    """
    assert isinstance(n, int) and n >= 0 , "The number must be a positive integer!"
    if n == 0:
        return 0
    else:
        return int(n%10) + sum_of_digits(int(n/10))


def power_of_n(base, exp):
    """
    Example: x^n = x*x*x ...
    x^n = x * x^n-1
    """
    assert isinstance(exp, int) and exp >= 0, "The number must be a positive integer!"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power_of_n(base, exp-1)


def greatest_common_divisor(a, b):
    """
    GCD is the largest positive integer that divides numbers without rest
    euclidean(48, 18)
    48/18 = 2 rest 12
    18/12 = 1 rest 6
    12/6 = 2 rest 0
    gcd = 6
    gcd(a, 0) = a
    gcd(a, b) = gcd(b, a % b)
    """
    assert isinstance(a, int) and isinstance(b, int), "The number must be a integer!"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def decimal_to_binary(n):
    """
    Step1: divide by 2
    Step2: Get integer quotient for next iteration
    Step3: Get rest for the binary digit
    Step4: Repeat until quotient is 0
    Example: 10 to binary
    12/2 = 5, rest 0
    5/2 = 2, rest 1
    2/2 = 1, rest 0
    1/2 = 0, rest 1
    = 1010
    f(n) = n % 2 + 10 * f(n/2)
    """
    assert isinstance(n, int), "The number must be a integer!"
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimal_to_binary(int(n/2))
