from sys import stdin

COCA_PRICE = 33  # константная цена колы


class FSM(object):  # автомат
    def __init__(self, condition, coins):  # конструктор
        self.condition = condition  # состояние
        self.coins = coins  # монеты

    def run(self):  # двиижение автомата
        while not self.condition.terminal:
            self.condition = self.condition.a_change_of_pace(self.coins)


class StateChange(object):  # состояние изенения
    def __init__(self):  # конструктор
        self.terminal = False

    def a_change_of_pace(self, coins):  # изменение шага
        for_out_money = []
        rem_change = sum(coins['user_money']) - COCA_PRICE  # сумма монет пользователя  - константная цена колы
        mon_auto = [el for el in coins['money']] + coins['user_money']

        for m in [10, 5, 2, 1]:  # проверка поданых монет
            while m in mon_auto and rem_change >= m:
                for_out_money.append(m)
                mon_auto.remove(m)
                rem_change -= m

        if rem_change != 0:
            for i in coins['user_money']:
                print("OUT ", i)  # выдача монет
            coins['user_money'] = []
            return StateMoney()  # возвращается состояние кола

        for m in for_out_money:  # выдача
            print("OUT ", m)

        coins['money'] = mon_auto
        coins['user_money'] = []

        return StateCoca()  # возвращается состояние кола


class StateMoney(object):  # состояние монет
    def __init__(self):  # конструктор
        self.terminal = False

    def a_change_of_pace(self, coins):  # изменение шага
        line = stdin.readline()
        if line.startswith("IN"):  # ввод монет
            money = int(line[3:])  # отрезание монет
            coins['user_money'].append(money)  # добавление к монетам пользователя
            return self
        elif line.startswith("PRESS"):  # конец ввода
            return StateChange()  # возвращается состояние изменения


class StateCoca(object):  # сосотояние кола
    def __init__(self):  # конструктор
        self.terminal = False

    def a_change_of_pace(self, coins):  # изменение шага
        print("OUT COCA")  # отдать колы
        return StateMoney()  # возвращается состояние монет


coins_in_the_machine = {'money': [1, 1, 1, 1, 1], 'user_money': []}  # монет для сдачи

auto_cola = FSM(StateMoney(), coins_in_the_machine)
auto_cola.run()  # запус автомата с колой
