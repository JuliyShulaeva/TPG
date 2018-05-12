import sys


def receiving_key(couple):
    return couple[1]


couples = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0,
           '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0,
           '13': 0, '14': 0, '15': 0, '16': 0}

number_of_sms = int(input())

for i in range(0, number_of_sms):
    pair_number = input()
    couples[pair_number] += 1
pairs = couples.items()

new_pairs = sorted(pairs, key=receiving_key, reverse=True)

for item in new_pairs:
    if item[1] == 0:
        sys.exit(0)
    print(item[0], item[1])

