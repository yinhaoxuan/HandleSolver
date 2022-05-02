import random

# find a word to guess from l
def guess(l):
    n = len(l)
    print(n)
    idx = random.randint(0, n-1)
    return l[idx]