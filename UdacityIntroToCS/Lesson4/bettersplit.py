# 1 Gold Star

# The built-in <string>.split() procedure works
# okay, but fails to find all the words on a page
# because it only uses whitespace to split the
# string. To do better, we should also use punctuation
# marks to split the page into words.

# Define a procedure, split_string, that takes two
# inputs: the string to split and a string containing
# all of the characters considered separators. The
# procedure should return a list of strings that break
# the source string up by the characters in the
# splitlist.


def split_string(source, splitlist):
    result = []
    sublst = []
    for p in splitlist:
        print("punctuation:{}".format(p))
        if result:
            for word in result:
                word_lst = word.split(p)
                for w in word_lst:
                    sublst.append(w)
            result = sublst
            print("result:{}".format(result))
            sublst = []
            print("sublst:{}".format(sublst))
        else:
            word_lst = source.split(p)
            for w in word_lst:
                result.append(w)
                print("result:{}".format(result))
    while "" in result:
        result.remove("")
    return result

def split_string(source, splitlist):
    output = []
    atsplit = True
    for char in source:
        if char in splitlist:
            atsplit = True
        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                # concatenate char to the last element
                output[-1] = output[-1] + char
    return output

def split_string(source, splitlist):
    target = source
    if len(splitlist) == 1:
        p = splitlist[0]
        return [value for value in target.split(p) if value != ""]
    for p in splitlist:
        target = target.replace(p, " ")
        print("source:{}".format(source))
    return target.split() #[value for value in source.split(" ") if value != ""]

out = split_string("This is a test-of the,string separation-code!"," ,!-")
print(out)
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = split_string("After  the flood   ...  all the colors came out.", " .")
print(out)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print(out)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
