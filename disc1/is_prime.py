def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    if n <= 1 or not isinstance(n,int):
        return False
    for i in (2,n//2 + 1):# should not begin with 1
        if n % i == 0:
            return False
    return True