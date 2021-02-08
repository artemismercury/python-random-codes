def report_status(scheduled_time, estimated_time):
    ''' (number, number) -> str

    Return the flight status (on time, early, delayed) for a flight that was scheduled to arrive at schedule_time, but is now estimated to arrive at estimated_time.

    Pre-condition: 0.0 <= scheduled_time < 24 and 0.0 <= estimated_time < 24
    
    >>> report_status(14.3, 14.3)
    'on time'
    >>> report_status(12.5, 11.5)
    'early'
    >>> report_status(9.0, 9.5)
    'delayed'
    '''

    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'

def is_even(num):
    '''(int) -> bool

    Return whether num is even.
    
    >>> is_even(4)
    True
    >>> is_even(77)
    False
    '''

    return num % 2 == 0
##    if num % 2 == 0:
##        return True
##    else:
##        return False

def inhospitable_weather(temp):
    ''' (number) -> bool

    Return True if and only if the given temperature in degrees Celsius is unpleasant (too hot or too cold).

    >>> inhospitable_weather(20)
    False
    '''
    
    return temp > 28 or temp < 12

##    if temp > 28:
##        return True
##    elif temp < 12:
##        return True
##    else:
##        return False

def num_passed(num):
    ''' (number) -> int

    '''

    if grade1 >= 50:
        num_passed = num_passed + 1
    if grade2 >= 50:
        num_passed = num_passed + 1


def grade_report(grade):
    if grade >= 80:
        return 'excellent'
    elif grade >= 50:
        return 'pass'


    
    
