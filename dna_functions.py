def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    result = 0

    for c in dna:
        if nucleotide == c:
            result = result + 1

    return result


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid (that is,
    it contains no characters other than 'A', 'T', 'C' and 'G').

    Precondition: A string is not a valid DNA sequence if
    it contains lowercase letters.

    >>> is_valid_sequence('ATCCGG')
    True
    >>> is_valid_sequence('ATcccGg')
    False
    >>> is_valid_sequence('BDQ12')
    False
    """

    invalid = 0
    
    for c in dna:
        if not (c in ['A', 'T', 'C', 'G']):
            invalid = invalid + 1

    return invalid <= 0

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.
    
    >>> insert_sequence('ATCGAT', 'ATCG', 3)
    'ATCATCGGAT'
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 4)
    'CCGGAT'
    >>> insert_sequence('ATCGAT', 'ATCG', 0)
    'ATCGATCGAT'
    """

    return dna1[: index] + dna2 + dna1[index :]

def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement. If the given parameter is not an
    nucleotide, then print 'Invalid nucleotide'.

    Nucleotide and their complements:
    A T
    T A
    C G
    G C

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    >>> get_complement('a')
    Invalid nucleotide
    """

    if nucleotide == 'A':
        return('T')
    elif nucleotide == 'T':
        return('A')
    elif nucleotide == 'C':
        return('G')
    elif nucleotide == 'G':
        return('C')

    else:
        print('Invalid nucleotide')

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.
    Otherwise, return an empty string.
    
    Precondition: the parameter is a DNA sequence.    

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('TAGC')
    'ATCG'
    """

    complementary = ''

    for nucleotide in dna:
        if nucleotide in ['A', 'T', 'C', 'G']:
            if nucleotide == 'A':
                complementary = complementary + 'T'
            if nucleotide == 'T':
                complementary = complementary + 'A'
            if nucleotide == 'C':
                complementary = complementary + 'G'
            if nucleotide == 'G':
                complementary = complementary + 'C'


    return complementary    
    
    
    
