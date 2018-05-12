#coding:utf8
import re


def rle(l):
    if l != "":
        repeat = {}
        for el in l:
            repeat[el] = (repeat.get(el) or 0) + 1
            counts = list(repeat.items())
            acc = []
            for el in counts:
                acc.append(str(el[1]))
                acc.append(el[0])
                str(acc)
        return acc
    else:
        return l

l = [int(n) for n in input('Числа через пробел - ').split()]

#if l == 0:
print(rle(l))
#else:
    #print('Список пуст')