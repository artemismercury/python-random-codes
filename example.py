def example(L):
    ''' (list) -> list

    Return every third number from a given list, starting
    from index 0 up to the lenght of the list.

    >>> example([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    [1, 4, 7, 10]
    >>> example(range(20, 31))
    [20, 23, 26, 29]

    '''

    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3

    return result
