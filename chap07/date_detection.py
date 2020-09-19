import re
import sys

def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            if year % 400 == 0:
                return True
    return False

date_regex = re.compile(
    r'''(
    (0[1-9]|[12][0-9]|3[01])/
    (0[1-9]|1[012])/
    ([12]\d{3})
    )''',
    re.VERBOSE
)

test_date = input('Enter a test date: ')
mo = date_regex.search(test_date)

if not mo:
    print(':: Invalid date format.')
    sys.exit(1)
else:
    valid_date = True
    invalid_reason = ''
    day, month, year = (int(x) for x in mo.groups()[1:])
    is_leap = is_leap_year(year)
    if month == 2:
        if is_leap:
            if day > 29:
                valid_date = False
                invalid_reason = 'Feb can have at most 29 days in a leap year.'
        else:
            if day > 28:
                valid_date = False
                invalid_reason = 'Feb can have at most 28 days in a non-leap year.'

    if month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            valid_date = False
            invalid_reason = 'This month can have at most 30 days.'
    else:
        if day > 31:
            valid_date = False
            invalid_reason = 'This month can have at most 31 days.'

if valid_date:
    print(f':: {test_date} is a valid date.')
    sys.exit(0)
else:
    print(f':: {test_date} is an invalid date.')
    print(f'::: Reason: {invalid_reason}')
    sys.exit(2)
