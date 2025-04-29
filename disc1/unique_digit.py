def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    for i in range(10):
        if has_digit(n,i):
            print(i)

    
def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10,"k should be a positive integer less than 10"
    "*** YOUR CODE HERE ***"
    sum = 0
    for i in str(n):
        if i == str(k):
            sum += 1
    if sum == 1: 
        return True
    else:
        return False
#I don't really make a has_digit function,because i don't really know how to don't count the digit before
#maybe there is a str operation?
#ok i misunderstand the meaning of the topic,is every unique digit,not digit only appears one time

#here is the right answer
def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    sum = 0
    for i in range(10):
        if has_digit(n,i):
            sum += 1
    return sum

    
def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10,"k should be a positive integer less than 10"
    "*** YOUR CODE HERE ***"
    sum = 0
    for i in str(n):
        if i == str(k):
            return True
    return False

"""
Q5: Bottles
Answer the following questions with your group. Step through the diagram to check your answers.

1) What determines how many different frames appear in an environment diagram?
a) The number of functions defined in the code
b) The number of call expressions in the code
c) The number of return statements in the code
d) The number of times user-defined functions are called when running the code
a

2) What happens to the return value of pass_it(bottles)?
a) It is used as the new value of remaining in the global frame
b) It is used as the new value of bottles in the global frame
c) It is used as the new value of pass_it in the global frame
d) None of the above
c

3) What effect does the line bottles = 98 have on the global frame?
a) It temporarily changes the value bound to bottles in the global frame.
b) It permanently changes the value bound to bottles in the global frame.
c) It has no effect on the global frame.
c
"""