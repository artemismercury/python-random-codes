##def sum_odd(L):
##
##    i = 0
##    total = 0
##
##    while i < (len(L) + 1) and L[i] % 2 != 0:
##        total = total + L[i]
##        i = i + 1
##
##    return total


def create_list(num1, num2):

    return list(range(num1, num2 + 1))

def sum_odds(L):

    ''' ([int, int]) -> int

    Return the sum of the odd numbers from a given list of int's.

    >>> sum_odds([1, 2, 3, 4])
    4

    >>> sum_odds(list(range(10, 19 + 1)))
    75

    '''

    odd = []
    i = 0

    while i < len(L):
        if L[i] % 2 != 0:
            odd.append(L[i])
        i = i + 1

    return sum(odd)
