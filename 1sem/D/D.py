#coding: utf-8
a = int(input())
def fact(a):
    if a == 0:
         return 1
    return fact(a - 1) * a
print(fact(a))