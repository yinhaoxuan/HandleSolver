import read_text

def init():
    list1 = []

    x = read_text.s.split(",")

    for x1 in x:
        y = x1.split(":")
        list1.append((y[0], y[1]))

    return list1
