# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from init import init
from feedback import get_feedback
from remove import remove
from guess import guess


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l = init() # init data
    while 1:
        word = guess(l)
        print(word)
        feedback = get_feedback()
        l = remove(l, feedback)
        if len(l) == 1:
            print(l[0])
            break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
