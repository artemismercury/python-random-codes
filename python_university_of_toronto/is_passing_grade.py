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
