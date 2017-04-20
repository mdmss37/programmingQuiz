# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    result = 0
    for i in list_of_numbers:
        if i > result:
            result = i
    return result

#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0