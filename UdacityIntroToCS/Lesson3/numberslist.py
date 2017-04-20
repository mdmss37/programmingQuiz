# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

def numbers_in_lists(string):
    # YOUR CODE
    result = []
    y = 0
    for i in string:

        if result == []:
            result.append(int(i))

        elif type(result[-1]) is list:
            if y < int(i):
                result.append(int(i))
            else:
                result[-1].append(int(i))

        elif type(result[-1]) is int:
            if result[-1] >= int(i):
                y = result[-1]
                result.append([int(i)])

            else:
                result.append(int(i))
    return result

def numbers_in_lists(string):
    # YOUR CODE
    y = -42 # something less than the numbers from 1-9
    result_list, sub_list = [], []
    for x in map(int, string):
        print(x, y, result_list, sub_list)
        if x <= y:
            sub_list.append(x)
        else: # x > y
            if sub_list:
                result_list.append(sub_list)
                sub_list = []
            result_list.append(x)
            y = x
    if sub_list:
        result_list.append(sub_list)
    return result_list

def numbers_in_lists(string):
    y = -10
    result_list, sub_list = [], []
    for x in map(int, string):
        if x <= y:
            sub_list.append(x)
        else:
            if sub_list:
                result_list.append(sub_list)
                sub_list = []
            result_list.append(x)
            y = x
    if sub_list:
        result_list.append(sub_list)
    return result_list

#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print(numbers_in_lists(string))
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print(numbers_in_lists(string))
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result

