import sys
# coding:utf8


def Pop_stack(self):
    if len(self) == 0:
        print('STACK_UNDERFLOW')
        sys.exit()
    else:
        return self.pop()


def IN(self, word):  # положить число на стек
    self.append(word)


def OUT(self):  # взять число и напечатать
    print(Pop_stack(self), end = '')


def ADD(self):  # взять первый, взять второй операнд, результат сложения
    s1 = Pop_stack(self)
    s2 = Pop_stack(self)
    s3 = int(s1) + int(s2)
    self.append(s3)


def SUB(self):  # взять первый операнд, взять второй операнд, результат вычитания
    v1 = Pop_stack(self)
    v2 = Pop_stack(self)
    v3 = int(v1) - int(v2)
    self.append(v3)


def MUL(self):  # взять первый операнд, взять второй операнд, результат умножения
    u1 = Pop_stack(self)
    u2 = Pop_stack(self)
    u3 = int(u1) * int(u2)
    self.append(u3)


def DIV(self):  # взять первый операнд, взять второй операнд, результат целочисленного деления
    d1 = Pop_stack(self)
    d4 = Pop_stack(self)
    d2 = int(d4)
    if d2 == 0:
        print('DIVISION_BY_ZERO')
        sys.exit(0)
    d3 = int(d1) // int(d2)
    self.append(d3)


stack_m = []

for cmd in sys.stdin:
    if cmd == '':
        sys.exit(0)
    cmd = cmd.split(' ')
    word1 = cmd[0]
    word2 = 0
    if word1 == 'IN':
        word2 = cmd[1]

    if word1 == 'IN':
        IN(stack_m, word2)
    elif word1.startswith('OUT'):
        OUT(stack_m)
    elif word1.startswith('ADD'):
        ADD(stack_m)
    elif word1.startswith('SUB'):
        SUB(stack_m)
    elif word1.startswith('MUL'):
        MUL(stack_m)
    elif word1.startswith('DIV'):
        DIV(stack_m)
