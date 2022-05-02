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
        self.result = []

def get_feedback():
    result = IdiomResult
    for i in range(4):
        # TODO
        # read result of one char
        # add this result to idiom result

    return result