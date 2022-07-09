from init import init
from feedback import get_feedback
from remove import remove
from guess import guess
import random

if __name__ == '__main__':
    random.seed(44)
    l = init() # init data
    while 1:
        word = guess(l)
        print(word)
        feedback = get_feedback()
        l = remove(l, feedback, word)
        if len(l) == 1:
            print(l[0])
            break

