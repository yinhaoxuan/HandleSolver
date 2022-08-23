import json
import random

from .feedback import IdiomResult, CharResult
from .guess import guess
from .init import init
from .remove import remove

lists = {}
guesses = {}

def get_result(clientID):
    guesses[clientID] = guess(lists[clientID])
    return guesses[clientID]

def get_start(clientID):
    lists[clientID] = init()
    return get_result(clientID)

def put_response(clientID, resp):
    i_result = IdiomResult()
    for char_result in resp:
        c_result = CharResult(shengmu=char_result['sm'], yunmu=char_result['ym'],
                              yindiao=char_result['yd'], zi=char_result['zi'])
        i_result.c_list.append(c_result)
    lists[clientID] = remove(lists[clientID], i_result, guesses[clientID])
    if len(lists[clientID]) == 0:
        return 0
    else:
        return 1


def test():
    # aaa:春暖花开 bbb:兴高采烈 ddd:怨天尤人
    random.seed(44)
    print('aaa receives the guess: ' + json.dumps(get_start('aaa')))  # 嵬目鸿耳
    print('aaa is updated: ' + str(put_response('aaa',
                                                [{'sm': 0, 'ym': 0, 'yd': 0, 'zi': 0},
                                                 {'sm': 0, 'ym': 0, 'yd': 0, 'zi': 0},
                                                 {'sm': 1, 'ym': 0, 'yd': 0, 'zi': 0},
                                                 {'sm': 0, 'ym': 0, 'yd': 2, 'zi': 0}])))
    print('aaa receives the guess: ' + json.dumps(get_result('aaa')))  # 春暖花开

    print('bbb receives the guess: ' + json.dumps(get_start('bbb')))  # 载欢载笑
    print('bbb is updated: ' + str(put_response('bbb',
                                                [{'sm': 0, 'ym': 0, 'yd': 1, 'zi': 0},
                                                 {'sm': 0, 'ym': 0, 'yd': 1, 'zi': 0},
                                                 {'sm': 0, 'ym': 1, 'yd': 0, 'zi': 0},
                                                 {'sm': 2, 'ym': 0, 'yd': 1, 'zi': 0}])))
    print('bbb receives the guess: ' + json.dumps(get_result('bbb')))  # 兴高采烈

    print('ccc receives the guess: ' + json.dumps(get_start('ccc')))  # 一高二低
    print('ccc is updated: ' + str(put_response('ccc',
                                                [{'sm': 0, 'ym': 2, 'yd': 1, 'zi': 1},
                                                 {'sm': 0, 'ym': 0, 'yd': 1, 'zi': 0},
                                                 {'sm': 0, 'ym': 1, 'yd': 2, 'zi': 2},
                                                 {'sm': 2, 'ym': 0, 'yd': 1, 'zi': 1}])))
    # 没有符合要求的成语

    print('ddd receives the guess: ' + json.dumps(get_start('ddd')))  # 偷天换日
    print('ddd is updated: ' + str(put_response('ddd',
                                                [{'sm': 0, 'ym': 2, 'yd': 0, 'zi': 0},
                                                 {'sm': 1, 'ym': 1, 'yd': 1, 'zi': 1},
                                                 {'sm': 0, 'ym': 2, 'yd': 2, 'zi': 0},
                                                 {'sm': 1, 'ym': 0, 'yd': 0, 'zi': 0}])))
    print('ddd receives the guess: ' + json.dumps(get_result('ddd')))  # 怨天尤人