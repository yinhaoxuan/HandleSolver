import read_text

list1 = []

x = read_text.s.split(",")

for x1 in x:
    y = x1.split(":")
    list1.append((y[0], y[1]))

print(list1[1][0])