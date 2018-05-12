#__author__ = 'student'


# coding:utf8

def add(x, y):
    s = x + y
    return s


def sub(x, y):
    v = x - y
    return v


def mul(x, y):
    u = x * y
    return u


def div(x, y):
    if y == 0:
        d = 0
    else:
        d = x / y
    return d
#ADD 1 1

line = input()
parsed = line.split(' ')
cmd = line[0:3]
arg1 = int(line[4])
arg2 = int(line[6])
d1 = {"ADD": add, "SUB": sub, "MUL": mul, "DIV": div}
print(d1[cmd](arg1, arg2))