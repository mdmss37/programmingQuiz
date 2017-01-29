# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

NON_LEAP_DAYS = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_DAYS = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    if year % 4 != 0:# (year is not exactly divisible by 4) then (it is a common year)
        return NON_LEAP_DAYS
    elif year % 100 != 0: #(year is not exactly divisible by 100) then (it is a leap year)
        return LEAP_DAYS
    elif year % 400 != 0: #(year is not exactly divisible by 400) then (it is a common year)
        return NON_LEAP_DAYS
    else: #(it is a leap year)
        return LEAP_DAYS

# y1,m1,d1 is birthday, y2,m2,d2 is current date
def days_between_dates(y1,m1,d1,y2,m2,d2):
    if (y1 > y2) or (y1 == y2 and m1 > m2) or (y1 == y2 and m1 == m2 and d1 > d2):
        print('incorrect input!')
        return None
    counter = 0
    while (y1 < y2) or (m1 < m2) or (d1 < d2):
        # year end pattern
        if m1 == 12 and d1 == isLeapYear(y1)[11]:
            y1, m1, d1, counter = y1 + 1, 1, 1, counter + 1
            # month end pattern
        elif d1 == isLeapYear(y1)[m1-1]:
            m1, d1, counter = m1 + 1, 1, counter + 1
                # not year and or month end
        else:
            d1, counter = d1 + 1, counter + 1
    return counter

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523),
                  ((1901,12,1,1900,1,31), None),
                  ((1900,12,1,1900,1,1), None),
                  ((1900,12,1,1900,12,1), 0)
                  ]

    for (args, answer) in test_cases:
        result = days_between_dates(*args)
        if result != answer:
            print "Test with data:", args, "failed" , result
        else:
            print "Test case passed!", result

test()