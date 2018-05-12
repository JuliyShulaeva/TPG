def gluing(number1, number2):
    return str(number1) + '/' + str(number2)


def calc(the_numerator, the_denominator):
    def nod(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    nod1 = nod(the_numerator, the_denominator)
    the_numerator = int(the_numerator) // nod1  # числитель
    the_denominator = int(the_denominator) // nod1  # знаменатель
    return gluing(the_numerator, the_denominator)


def add(x1, y1):
    s1 = int(x1[0])  # числитель
    s2 = int(x1[1])  # знаменатель
    s3 = int(y1[0])  # числитель
    s4 = int(y1[1])  # знаменатель
    s5 = s1 * s4
    s6 = s3 * s2
    s7 = s5 + s6
    s8 = s2 * s4
    print(calc(s7, s8))


def sub(x1, y1):
    v1 = int(x1[0])  # числитель
    v2 = int(x1[1])  # знаменатель
    v3 = int(y1[0])  # числитель
    v4 = int(y1[1])  # знаменатель
    v5 = v1 * v4
    v6 = v2 * v3
    v7 = v5 - v6
    v8 = v2 * v4
    print(calc(v7, v8))


def mul(x1, y1):
    u1 = int(x1[0])  # числитель
    u2 = int(x1[1])  # знаменатель
    u3 = int(y1[0])  # числитель
    u4 = int(y1[1])  # знаменатель
    u5 = u1 * u3
    u6 = u2 * u4
    print(calc(u5, u6))


def div(x1, y1):
    d1 = int(x1[0])  # числитель
    d2 = int(x1[1])  # знаменатель
    d3 = int(y1[0])  # числитель
    d4 = int(y1[1])  # знаменатель
    d5 = d1 * d4  # числитель
    d6 = d2 * d3  # знаменатель
    print(calc(d5, d6))


line = input()
parsed = line.split(' ')
x = parsed[0]
action = parsed[1]
y = parsed[2]

x1 = x.split('/')

y1 = y.split('/')

the_first_fraction = (x1[0], x1[1])  # первая дробь
the_second_fraction = (y1[0], y1[1])  # вторая дробь

if action == '/':
    div(the_first_fraction, the_second_fraction)
elif action == '*':
    mul(the_first_fraction, the_second_fraction)
elif action == '+':
    add(the_first_fraction, the_second_fraction)
else:
    sub(the_first_fraction, the_second_fraction)
