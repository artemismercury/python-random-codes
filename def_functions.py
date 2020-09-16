def convert_to_minutes(num_hours):
    """(int) -> int

    Return the number of minutes there are in num_hours hours.

    >>> convert_to_minutes(2)
    120
    >>> convert_to_minutes(10)
    600
    """

    minutes = num_hours * 60
    return minutes

def convert_to_seconds(num_hours):
    """(int) -> int

    Return the number of seconds there are in num_hours.

    >>> convert_to_seconds(2)
    7200
    >>> convert_to_seconds(10)
    36000
    """

    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds

def is_passing_grade(grade):
    """(int, float) -> str

    Return 'pass' if grade is at least 50 and return 'fail' otherwise

    >>>is_passing_grade(45)
    'fail'
    >>>is_passing_grade(80.5)
    'pass'

    """

    if grade >= 50:
        print('pass')
    else:
        print('fail')

def count_vowels(s):
    """(str) -> int

    Return the number of vowels in s. Do not treat the letter y as a vowel.

    >>>count_vowels('Happy Anniversary!')
    5
    >>>count_vowels('xyz')
    0

    """

    num_vowels = 0

    for char in s:
        if char in 'aeiouAEIOU':
             num_vowels = num_vowels + 1

    return num_vowels
        
def collect_vowels(s):
    '''(str) -> str

    Return the vowels from s. Do not treat the letter y as a vowel.

    >>>collect_vowels('Happy Anniversary!')
    'aAiea'
    >>>collect_vowels('xyz')
    ''
    '''

    vowels = ''

    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels

def has_vowel(s):

    """(str) -> bool
    Return True if and only if s has at least one vowel, not including y.
    >>> has_vowel("Anniversary")
    True
    >>> has_vowel("xyz")
    False
    """

    vowel_found = False
    for char in s:
        if char in 'aeiouAEIOU':  
           vowel_found = True

    return vowel_found

def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that appear at least
    once in s2. The characters in the result will appear in the same order
    as they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a' 
    >>> common_chars('abb', 'ab')
    'abb' 
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''


    res = ''
    for ch in s1:
        if ch in s2:
            res = res + ch
    return res

##s1.find(s2, (s1.find(s2) + 1))
##
##Return de second appearance of a variable inside another variable

##i = 0
##
##	print(s[i])
##	i = i + 1

def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but not
    including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''

    before_vowel = ''
    i = 0

    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel

def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives a
    valid response. Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer

def last_vowel(s):
    ''' (str) -> str
    Return the last vowel in s if one exists; otherwise,
    return None.

    >>> last_vowel('cauliflower')
    'e'
    >>> last_vowel('pfft')
    None
    '''

    i = len(s) - 1
    while i >=0:
        if s[i] in 'aeiouAEIOU':
            return s[i]
        i = i - 1
    print(None)

##colours = []
##prompt = 'Enter another one of your favourite colours (type return to end):'
##
##colour = input(prompt)
##
##while colour != '':
##    colours.append(colour)
##    colour = input(prompt)

def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result


def example(L):
    ''' (list) -> list
    '''

    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3

    return result

def compress_list(L):

    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list

def while_version(L):
    ''' (list of number) -> number

     >>> while_version([1, 3, 5, 4])
     9
     '''

    i = 0
    total = 0
    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total

def for_version(L):
    found_even = False
    total = 0

    for num in L:
        if num % 2 != 0:
            total = total + num
        found_even = True

    return total

def cap_song_repetition(playlist, song):

    while playlist.count(song) > 3:
        playlist.remove(song)

    print(playlist)

def cap_song_repetition_1(playlist, song):

    while playlist.count(song) > 3:
        playlist.pop(playlist.index(song))
        
    print(playlist)

    
def sum_odd(L):

    i = 0
    total = 0

    while i < (len(L) + 1) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total


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

for metal in ['Li', 'Na']:
    for gas in ['F', 'Cl', 'Br']:
        print(metal + gas)

def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

mystery('civil')

def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item
    
shift_right([1, 2, 3, 4])

def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    for i in range(len(list1)):
        pairs.append([list1[i], list2[i]])

    return pairs

def contains(value, lst):
    
    found = False
    
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
            
    return found

##ou
##
##for sublist in lst:
##        if value in sublist:
##            found = True

def lines_startswith(file, letter):

    matches = []

    for line in file:
        if letter in line:
            matches.append(line.rstrip('\n'))
            

##    for line in file:
##        if letter == line[0]:
##            matches.append(line.rstrip('\n'))

    return matches

def write_to_file(file, sentences):

    for s in sentences:
        file.write(s)

##    file.write(sentences)

##    for s in sentences:
##        file.write(s)
##        file.write('\n')

##    for s in sentences:
##        file.write(s + '\n')

##    for s in sentences:
##        file.write(s)
##    file.write('\n')



        
    









