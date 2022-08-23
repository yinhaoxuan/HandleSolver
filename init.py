from .read_text import s
from .idioms import dict
from .sounds import sounds

# 'yi1'
def unwrap0(snd):
    lst = []
    lens = len(snd) - 1
    if snd[0] == 'e':
        lst.append(" ")
        lst.append(snd[0])
        lst.append(snd[lens])
        return lst

    if snd[0] == 'c' or snd[0] == 's' or snd[0] == 'z':
        if snd[1] == 'h':
            lst.append(snd[0:2])
            lst.append(snd[2:lens])
            lst.append(snd[lens])
        else:
            lst.append(snd[0])
            lst.append(snd[1:lens])
            lst.append(snd[lens])
    else:
        lst.append(snd[0])
        lst.append(snd[1:lens])
        lst.append(snd[lens])
    return lst

tone = {'\u0101': ['a', '1'], '\u00E1': ['a', '2'], '\u01CE': ['a', '3'], '\u00E0': ['a', '4'],
        '\u0113': ['e', '1'], '\u00E9': ['e', '2'], '\u011B': ['e', '3'], '\u00E8': ['e', '4'],
        '\u014D': ['o', '1'], '\u00F3': ['o', '2'], '\u01D2': ['o', '3'], '\u00F2': ['o', '4'],
        '\u012B': ['i', '1'], '\u00ED': ['i', '2'], '\u01D0': ['i', '3'], '\u00EC': ['i', '4'],
        '\u016B': ['u', '1'], '\u00FA': ['u', '2'], '\u01D4': ['u', '3'], '\u00F9': ['u', '4'],
        '\u01D8': ['v', '2'], '\u01DA': ['v', '3'], '\u01DC': ['v', '4']}

uv = '\u00FC'

def is_yunmu_kaitou(c):
    return c == 'a' or c == 'o' or c == 'e' or c in tone.keys()

# 'lóng'
def unwrap1(snd):
    lst = []
    lens = len(snd) - 1
    if is_yunmu_kaitou(snd[0]):
        lst.append(" ")
        # 'āng'
        if snd[0] in tone.keys():
            c1, c2 = tone[snd[0]]
            # 'a', '1'
            lst.append(c1 + snd[1:])
            lst.append(c2)
        else:
            lst.append(snd)
            lst.append('0')
        return lst

    if (snd[0] == 'c' or snd[0] == 's' or snd[0] == 'z') and snd[1] == 'h':
        lst.append(snd[0:2])
        yunmu = ''
        yindiao = '0'
        for c in snd[2:]:
            if c in tone.keys():
                c1, yindiao = tone[c]
                yunmu += c1
            else:
                yunmu += c
        lst.append(yunmu)
        lst.append(yindiao)
    else:
        lst.append(snd[0:1])
        yunmu = ''
        yindiao = '0'
        for c in snd[1:]:
            if c in tone.keys():
                c1, yindiao = tone[c]
                yunmu += c1
            else:
                yunmu += c
        lst.append(yunmu)
        lst.append(yindiao)
    return lst

def init():
    idiom_list = []

    x = s.split(",")

    for x1 in x:
        y = x1.split(":")
        # idiom_list.append((y[0], y[1]))
        # print(y[0])
        # print(y[1])
        r = y[1]
        r = r.strip('"')
        z = r.split(" ")

        c = [[], [], [], []]

        for (i, z1) in enumerate(z):
            c[i] = unwrap0(z1)

        idiom_list.append((y[0], c))
    # print(idiom_list[0])
    # 带多音字的成语。已经全部把读音列出来了

    diction = {} # 汉字到读音的map
    for (snd, chars) in sounds.items():
        for char in chars:
            # 把snd转换成需要的格式
            # 'lóng' -> ['l', 'ong', '2']
            diction[char] = unwrap1(snd)

    # 不带多音字的成语。可以知道单独每个字的读音。
    for idiom in dict:
        sound = []
        ok = True
        for char in idiom:
            # print(char)
            if char in diction.keys():
                sound.append(diction[char])
            else:
                ok = False
                break
        if ok:
            idiom_list.append((idiom, sound))


    # print(idiom_list[-1])
    return idiom_list
