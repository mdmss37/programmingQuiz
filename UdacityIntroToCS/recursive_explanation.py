# http://web.archive.org/web/20150307005946/http://forums.udacity.com/questions/2020957/stgs-recursion-collection-1st-draft


# http://web.archive.org/web/20150228204833/http://forums.udacity.com/questions/56990/understanding-recursion-the-stack-model

def deep_count(p):
    sum = 0
    for e in p:
        sum += 1
        if type(e) == list:
            sum += deep_count(e)
    return sum

print(deep_count([1, 3, [2, [7, 6], [], 5]]))

# http://web.archive.org/web/20150221052637/http://forums.udacity.com/questions/100023989/python-101-unit-6-yet-another-attempt-to-explain-recursion

def sumFirstN(n):
    if n == 0:
        return 0
    else:
        return sumFirstN(n-1) + n

print(sumFirstN(10))

def lucas(n):
    if n == 0: return 2
    elif n == 1: return 1
    else: return lucas(n-1) + lucas(n-2)

print(lucas(10))

import random

def quick_sort(A):
    if len(A) <= 1:
        return A
    else:
        pivot = A.pop(random.randint(0, len(A)-1))
        less, greater = [], []
        for val in A:
            if val < pivot:
                less.append(val)
            else:
                greater.append(val)

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([3, 4, 2, 5, 3, 8, 1]))

def list_binary_search(l, t):
    # print("list is {}, target is {}".format(l, t))
    if len(l) == 0 or len(l) == 1:
        if l == []:
            return False
        elif l[0] == t:
            return True
        else:
            return False
    else:
        mid_idx = len(l) // 2
        if t < l[mid_idx]:
            return list_binary_search(l[:mid_idx], t)
        else:
            return list_binary_search(l[mid_idx:], t)

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
assert( list_binary_search( A, 0) == False )
assert( list_binary_search( A, 1) == True )
assert( list_binary_search( A, 2) == True )
assert( list_binary_search( A, 13) == True )
assert( list_binary_search( A, 24) == False )
assert( list_binary_search( A, 25) == True )
assert( list_binary_search( A, 26) == False )
print("tests of list_binary_search() passed")


def list_binary_search_depth(l, t):
    print("list is {}, target is {}".format(l, t))
    if len(l) == 0 or len(l) == 1:
        if l == []:
            return [False, 0]
        elif l[0] == t:
            return [True, 0]
        else:
            return [False, 0]
    else:
        mid_idx = len(l) // 2
        if t < l[mid_idx]:
            result, depth = list_binary_search_depth(l[:mid_idx], t)
            print(result, depth)
            return [result, depth+1]
        else:
            result, depth = list_binary_search_depth(l[mid_idx:], t)
            print(result, depth)
            return [result, depth+1]

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]

assert( list_binary_search_depth( A, 0) == [False, 4] )
assert( list_binary_search_depth( A, 1) == [True, 4] )
assert( list_binary_search_depth( A, 2) == [True, 4] )
assert( list_binary_search_depth( A, 13) == [True, 4] )
assert( list_binary_search_depth( A, 24) == [False, 4] )
assert( list_binary_search_depth( A, 25) == [True, 4] )
assert( list_binary_search_depth( A, 26) == [False, 4] )
print("tests of list_binary_search_depth() passed")

def list_binary_search_where(l, t, list_first_index = 0):
    print("list is {}, target is {}".format(l, t))
    if len(l) == 0 or len(l) == 1:
        if l == []:
            return [False, None]
        elif l[0] == t:
            return [True, 0]
        else:
            return [False, None]
    else:
        mid_idx = len(l) // 2
        if t < l[mid_idx]:
            result, where = list_binary_search_where(l[:mid_idx], t, list_first_index)
            print(result, where)
            if where == None:
                return [result, None]
            else:
                print(result, where)
                return [result, where]
        else:
            result, where = list_binary_search_where(l[mid_idx:], t, list_first_index)
            print(result, where)
            if where == None:
                return [result, None]
            else:
                print(result, where + mid_idx)
                return [result, where + mid_idx]

A = [1, 2, 3, 3, 3, 6, 8, 9, 13, 13, 14, 17, 21, 22, 23, 25]
assert( list_binary_search_where( A, 0) == [False, None] )
assert( list_binary_search_where( A, 1) == [True, 0] )
assert( list_binary_search_where( A, 2) == [True, 1] )
assert( list_binary_search_where( A, 13) == [True, 9] )
assert( list_binary_search_where( A, 24) == [False, None] )
assert( list_binary_search_where( A, 25) == [True, 15] )
assert( list_binary_search_where( A, 26) == [False, None] )
print("tests of list_binary_search_where() passed")


def list_binary_search_depth_2(l, t):
    print("list is {}, target is {}".format(l, t))
    if len(l) == 0 or len(l) == 1:
        if l == []:
            return [False, 0]
        elif l[0] == t:
            return [True, 0]
        else:
            return [False, 0]
    else:
        mid_idx = len(l) // 2
        if l[mid_idx] == t:
            return [True, 0]

        if t < l[mid_idx]:
            result, depth = list_binary_search_depth_2(l[:mid_idx], t)
            return [result, depth+1]
        else:
            result, depth = list_binary_search_depth_2(l[mid_idx+1:], t)
            return [result, depth+1]


assert( list_binary_search_depth_2( A, 0) == [False, 4] )
assert( list_binary_search_depth_2( A, 1) == [True, 4] )
assert( list_binary_search_depth_2( A, 2) == [True, 3] )
assert( list_binary_search_depth_2( A, 13) == [True, 0] )
assert( list_binary_search_depth_2( A, 24) == [False, 3] )
assert( list_binary_search_depth_2( A, 25) == [True, 3] )
assert( list_binary_search_depth_2( A, 26) == [False, 3] )
print("tests of list_binary_search_depth_2() passed")


###################-Solution Code-###################
def list_binary_search(my_list, the_value):
    print(my_list)
    # indicates whether the_value is in my_list
    if len(my_list) == 0:
        return False
    elif len(my_list) == 1:
        return my_list[0] == the_value
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
        else:
            new_list = my_list[mid_index:]
        return list_binary_search(new_list, the_value)

def list_binary_search_depth(my_list, the_value):
    print(my_list)
    # indicates whether the_value is in my_list and how deep we search for it
    if len(my_list) == 0:
        return [False, 0]
    elif len(my_list) == 1:
        return [my_list[0] == the_value, 0]
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
        else:
            new_list = my_list[mid_index:]
        result, depth = list_binary_search_depth(new_list, the_value)
        return ( [result, depth+1] )

def list_binary_search_where(my_list, the_value, list_first_index = 0):
    print(my_list, list_first_index)
    # indicates whether the_value is in my_list and where it is
    if len(my_list) == 0:
        return [False, None]
    elif len(my_list) == 1:
        if my_list[0] != the_value:
            return [False, None]
        else:
            return [True, list_first_index]
    else:
        mid_index = len(my_list) // 2
        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
            list_first_index += 0
        else:
            new_list = my_list[mid_index:]
            list_first_index += mid_index
        return list_binary_search_where(new_list, the_value, list_first_index)

def list_binary_search_depth_2(my_list, the_value):
    print(my_list)
    # indicates whether the_value is in my_list and how deep we searched for it
    if len(my_list) == 0:
        return [False, 0]
    elif len(my_list) == 1:
        return [my_list[0] == the_value, 0]
    else:
        mid_index = len(my_list) // 2
        if the_value == my_list[mid_index]:
            return [True, 0]

        if the_value < my_list[mid_index]:
            new_list = my_list[:mid_index]
        else:
            new_list = my_list[mid_index+1:]  # we start at mid_index+1 now
        result, depth = list_binary_search_depth_2(new_list, the_value)
        return ( [result, depth+1] )