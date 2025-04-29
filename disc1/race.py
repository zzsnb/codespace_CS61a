def race(x, y):
    """The tortoise always walks x feet per minute, while the hare repeatedly
    runs y feet per minute for 5 minutes, then rests for 5 minutes. Return how
    many minutes pass until the tortoise first catches up to the hare.

    >>> race(5, 7)  # After 7 minutes, both have gone 35 steps
    7
    >>> race(2, 4) # After 10 minutes, both have gone 20 steps
    10
    """
    assert y > x and y <= 2 * x, 'the hare must be fast but not too fast'
    tortoise, hare, minutes = 0, 0, 0
    while minutes == 0 or tortoise - hare:#here should not be this boole judge,but tortoise>=hare.
        tortoise += x
        if minutes % 10 < 5:
            hare += y
        minutes += 1
        print(minutes)
    return minutes


#endless loop:race(11,19)
#wrong answer:race(8,12)(return 15)(all that return more than 10 is wrong)