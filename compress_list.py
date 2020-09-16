def compress_list(L):
    '''(list) -> list

    Return a sum of every pair of numbers within a given list.
    Precondition: the given list need to have a even number of items.

    >>> compress_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [3, 7, 11, 15, 19]
    >>> compress_list([1, 2, 3, 4])
    [3, 7]

    '''
    
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list
