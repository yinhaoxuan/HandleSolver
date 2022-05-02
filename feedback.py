from enum import Enum

# 0: completely wrong (grey)
# 1: completely right (green)
# 2: occurs in the wrong place (orange)

INIT = -1
WRONG = 0
RIGHT = 1
OCCUR = 2

class CharResult:
    def __init__(self):
        self.shengmu = INIT
        self.yunmu = INIT
        self.yindiao = INIT
        self.zi = INIT

class IdiomResult:
    def __init__(self):
        self.c_list = []

def get_feedback():
    i_result = IdiomResult()
    for i in range(4):
        # read result of one char
        # add this result to idiom result
        c_result = CharResult()
        c_result.shengmu = int(input())
        c_result.yunmu = int(input())
        c_result.yindiao = int(input())
        c_result.zi = int(input())
        i_result.c_list.append(c_result)

    return i_result
