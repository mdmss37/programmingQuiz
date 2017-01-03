def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def reduction_fraction(numer, denom):
    if numer == 0:
        raise ZeroDivisionError
    common_divisor = gcd(numer, denom)
    reduced_numer, reduced_denom = numer / common_divisor, denom / common_divisor

    if reduced_denom == 1:
        return reduced_numer
    else:
        return reduced_numer, reduced_denom

def mixed_fraction(s):
    temp = s.split("/")
    # handle as positive fraction, in case either one is negative, adjust when return the value.
    numer, denom = abs(int((temp[0]))), abs(int(temp[1]))

    if denom == 0:
        raise ZeroDivisionError
    if numer == 0:
        return "0"

    int_part = numer / denom
    if int_part == 0: int_part = ""
    else: int_part = str(int_part)

    fraction_part = ""

    # denominator < numerator
    numer = numer % denom
    if numer == 0:
        pass
    else:
        reduced_numer, reduced_denom = reduction_fraction(numer, denom)
        fraction_part = "{}/{}".format(reduced_numer, reduced_denom)

    if (int(temp[0]) / int(temp[1])) < 0:
            if int_part == "":
                return "-" + fraction_part
            elif fraction_part == "":
                return "-" + int_part
            else:
                return "-" + int_part + " "  + fraction_part
    elif int_part == "":
        return fraction_part
    elif fraction_part == "":
        return int_part
    else:
        return int_part + " "  + fraction_part

# print(mixed_fraction('42/9'))
# print(mixed_fraction('6/3'))
# print(mixed_fraction('4/6'))
# print(mixed_fraction('0/18891'))
# print(mixed_fraction('-10/7'))
# print(mixed_fraction('-22/-7'))

print(mixed_fraction('-2844566/3272981'))