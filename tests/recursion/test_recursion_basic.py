from pytest import raises

import recursion.basic as rb


def test_factorial_function():
    result = rb.factorial(n=4)
    expected = 24
    assert result == expected

    result = rb.factorial(n=5)
    expected = 120
    assert result == expected

    result = rb.factorial(n=1)
    expected = 1
    assert result == expected

    result = rb.factorial(n=0)
    expected = 1
    assert result == expected


def test_factorial_raise_assert_error():
    with raises(AssertionError):
        rb.factorial(-4)

    with raises(AssertionError):
        rb.factorial(4.0)

    with raises(AssertionError):
        rb.factorial("4.0")


def test_fibonacci_function():
    result = rb.fibonacci(n=0)
    expected = 0
    assert result == expected

    result = rb.fibonacci(n=1)
    expected = 1
    assert result == expected

    result = rb.fibonacci(n=2)
    expected = 1
    assert result == expected

    result = rb.fibonacci(n=7)
    expected = 13
    assert result == expected

    result = rb.fibonacci(n=10)
    expected = 55
    assert result == expected


def test_fibonacci_raise_assert_error():
    with raises(AssertionError):
        rb.fibonacci(-4)

    with raises(AssertionError):
        rb.fibonacci(4.0)

    with raises(AssertionError):
        rb.fibonacci("4.0")


def test_sum_of_digits_function():
    result = rb.sum_of_digits(n=0)
    expected = 0
    assert result == expected

    result = rb.sum_of_digits(n=1)
    expected = 1
    assert result == expected

    result = rb.sum_of_digits(n=10)
    expected = 1
    assert result == expected

    result = rb.sum_of_digits(n=54)
    expected = 9
    assert result == expected

    result = rb.sum_of_digits(n=112)
    expected = 4
    assert result == expected


def test_sum_of_digits_raise_assert_error():
    with raises(AssertionError):
        rb.sum_of_digits(-4)

    with raises(AssertionError):
        rb.sum_of_digits(4.0)

    with raises(AssertionError):
        rb.sum_of_digits("4.0")


def test_power_of_n_function():
    result = rb.power_of_n(base=0, exp=0)
    expected = 1
    assert result == expected

    result = rb.power_of_n(base=0, exp=1)
    expected = 0
    assert result == expected

    result = rb.power_of_n(base=245, exp=1)
    expected = 245
    assert result == expected

    result = rb.power_of_n(base=2, exp=2)
    expected = 4
    assert result == expected

    result = rb.power_of_n(base=6, exp=7)
    expected = 279936
    assert result == expected


def test_power_of_n_raise_assert_error():
    with raises(AssertionError):
        rb.power_of_n(base=-4, exp=-2)

    with raises(AssertionError):
        rb.power_of_n(base=4.0, exp=2.0)

    with raises(AssertionError):
        rb.power_of_n(base=4, exp="4.0")


def test_gcd_function():
    result = rb.greatest_common_divisor(a=0, b=0)
    expected = 0
    assert result == expected

    result = rb.greatest_common_divisor(a=1, b=0)
    expected = 1
    assert result == expected

    result = rb.greatest_common_divisor(a=48, b=18)
    expected = 6
    assert result == expected


def test_gcd_raise_assert_error():
    with raises(AssertionError):
        rb.greatest_common_divisor(a=4.0, b=2.0)

    with raises(AssertionError):
        rb.greatest_common_divisor(a=4, b="4.0")


def test_decimal_to_binary_function():
    result = rb.decimal_to_binary(n=0)
    expected = 0
    assert result == expected

    result = rb.decimal_to_binary(n=1)
    expected = 1
    assert result == expected

    result = rb.decimal_to_binary(n=10)
    expected = 1010
    assert result == expected

    result = rb.decimal_to_binary(n=2)
    expected = 10
    assert result == expected

    result = rb.decimal_to_binary(n=24568)
    expected = 101111111111000
    assert result == expected

    result = rb.decimal_to_binary(n=-24568)
    expected = 101111111111000
    assert result == expected

    result = rb.decimal_to_binary(n=1234469489123)
    expected = 10001111101101100000111011000100111100011
    assert result == expected


def test_decimal_to_binary_raise_assert_error():
    with raises(AssertionError):
        rb.decimal_to_binary(n=2.0)

    with raises(AssertionError):
        rb.decimal_to_binary(n="4.0")
