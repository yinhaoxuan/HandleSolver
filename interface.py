import json
import random

from .feedback import IdiomResult, CharResult
from .guess import guess
from .init import init
from .remove import remove

lists = {}
guesses = {}


def get_result(clientID):
    if clientID not in lists.keys():
        lists[clientID] = init()
    guesses[clientID] = guess(lists[clientID])
    return guesses[clientID]


def put_response(clientID, resp):
    i_result = IdiomResult()
    for char_result in json.loads(resp):
        c_result = CharResult(shengmu=char_result['shengmu'], yunmu=char_result['yunmu'],
                              yindiao=char_result['yindiao'], zi=char_result['zi'])
        i_result.c_list.append(c_result)
    lists[clientID] = remove(lists[clientID], i_result, guesses[clientID])


def test():
    # aaa:春暖花开 bbb:兴高采烈
    random.seed(44)
    print('aaa receives the guess: ' + json.dumps(get_result('aaa')))  # 嵬目鸿耳
    put_response('aaa', json.dumps(
        [{'shengmu': 0, 'yunmu': 0, 'yindiao': 0, 'zi': 0}, {'shengmu': 0, 'yunmu': 0, 'yindiao': 0, 'zi': 0},
         {'shengmu': 1, 'yunmu': 0, 'yindiao': 0, 'zi': 0}, {'shengmu': 0, 'yunmu': 0, 'yindiao': 2, 'zi': 0}]))
    print('aaa receives the guess: ' + json.dumps(get_result('aaa')))  # 春暖花开

    print('bbb receives the guess: ' + json.dumps(get_result('bbb')))  # 载欢载笑
    put_response('bbb', json.dumps(
        [{'shengmu': 0, 'yunmu': 2, 'yindiao': 1, 'zi': 0}, {'shengmu': 0, 'yunmu': 0, 'yindiao': 1, 'zi': 0},
         {'shengmu': 0, 'yunmu': 1, 'yindiao': 2, 'zi': 0}, {'shengmu': 2, 'yunmu': 0, 'yindiao': 1, 'zi': 0}]))
    print('bbb receives the guess: ' + json.dumps(get_result('bbb')))  # 兴高采烈
