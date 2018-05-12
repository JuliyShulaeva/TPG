def calc(the_numerator, the_denominator):
    def nod(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    nod1 = nod(the_numerator, the_denominator)
    the_numerator = int(the_numerator) // nod1
    the_denominator = int(the_denominator) // nod1
    return the_numerator, the_denominator


class Rat:
    def from_string(self):
        line1 = self.split('/')
        number1, number2 = calc(int(line1[0]), int(line1[1]))
        return Rat(number1, number2)

    def __init__(self, f_num, s_num):
        self.f_num, self.s_num = calc(int(f_num), int(s_num))

    def __add__(self, other):
        self.f_num = self.f_num * other.s_num + self.s_num * other.f_num
        self.s_num = self.s_num * other.s_num
        return Rat(self.f_num, self.s_num)

    def __sub__(self, other):
        self.f_num = self.f_num * other.s_num - self.s_num * other.f_num
        self.s_num = self.s_num * other.s_num
        return Rat(self.f_num, self.s_num)

    def __mul__(self, other):
        self.f_num = self.f_num * other.f_num
        self.s_num = self.s_num * other.s_num
        return Rat(self.f_num, self.s_num)

    def __truediv__(self, other):
        self.f_num = self.f_num * other.s_num
        self.s_num = self.s_num * other.f_num
        return Rat(self.f_num, self.s_num)

    def __str__(self):
        return str(self.f_num) + '/' + str(self.s_num)

fir_num, action, sec_num = input().split(' ')
fir_num, sec_num = Rat.from_string(fir_num), Rat.from_string(sec_num)

the_result = None

if action == '/':
    the_result = fir_num / sec_num
elif action == '*':
    the_result = fir_num * sec_num
elif action == '+':
    the_result = fir_num + sec_num
else:
    the_result = fir_num - sec_num

print(the_result)
