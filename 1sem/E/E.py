# coding:utf8
import copy


def polidrom(a):
    b = copy.copy(a)
    list.reverse(a)
    if a == b:
        return print('true')
    else:
        return print('false')


a = list(input())
polidrom(a)
