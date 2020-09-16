def while_version(L):
    ''' (list of number) -> number

    Return a sum of the items from a given list up to the first even number
    found in the list.

    >>> while_version([1, 3, 5, 4])
     9
    >>> while_version([5, 5, 5, 2])
    15

    '''

    i = 0
    total = 0
    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total

def for_version(L):
    ''' (list of number) -> number

    Return a sum of the items from a given list up to the first even number
    found in the list.

    >>> while_version([1, 3, 5, 4])
     9
    >>> while_version([5, 5, 5, 2])
    15

    '''

    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total
