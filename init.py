import read_text
import idioms

def init():
    polyphones_list = []

    x = read_text.s.split(",")

    for x1 in x:
        y = x1.split(":")
        # polyphones_list.append((y[0], y[1]))
        # print(y[0])
        # print(y[1])
        r = y[1]
        r = r.strip('"')
        z = r.split(" ")

        c = [[], [], [], []]

        for (i, z1) in enumerate(z):
            lens = len(z1) - 1
            if z1[0] == 'e':
                c[i].append(" ")
                c[i].append(z1[0])
                c[i].append(z1[lens])
                continue

            if z1[0] == 'c' or z1[0] == 's' or z1[0] == 'z':
                if z1[1] == 'h':
                    c[i].append(z1[0:2])
                    c[i].append(z1[2:lens])
                    c[i].append(z1[lens])
                else:
                    c[i].append(z1[0])
                    c[i].append(z1[1:lens])
                    c[i].append(z1[lens])
            else:
                c[i].append(z1[0])
                c[i].append(z1[1:lens])
                c[i].append(z1[lens])

        # print(c)

        polyphones_list.append((y[0], c))

    # print(polyphones_list[0])
    return polyphones_list

