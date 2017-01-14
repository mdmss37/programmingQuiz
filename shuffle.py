import random

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def shuffle(deck):
    "Knuth's Algorighm P."
    N = len(deck)
    for i in range(0, N-1):
        swap(deck, i, random.randrange(i, N))
    return deck

def swap(deck, i, j):
    "Swap elements i and j of a collection."
    print("swap:position {} and position {}".format(i, j))
    deck[i], deck[j] = deck[j], deck[i]

print(shuffle(mydeck))

# https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
# https://www.quora.com/What-is-an-easy-way-to-understand-Knuth-shuffles-algorithm
# https://spin.atomicobject.com/2014/08/11/fisher-yates-shuffle-randomization-algorithm/