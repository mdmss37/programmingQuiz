
# http://stackoverflow.com/questions/25393659/python-list-comprehension-doesnt-work-when-converted-to-nested-for-loops
# https://docs.python.org/3/library/itertools.html#itertools.product
def product(repeat=1, *args):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    print(pools)
    result = [[]]
    for pool in pools:
        # result = [x+[y] for x in result for y in pool]
        result2 = result[:] # in first iteration, result2 = [[]] which comes from result = [[]]
        result = [] # result is now []
        for x in result2:
            print("x is ", x)
            for y in pool:
                print("y is ", y)
                result.append(x + [y])
        print(result)
    for prod in result:
        yield tuple(prod)

print(list(product(2,[1,2,3],[4,5,6],[7,8,9])))