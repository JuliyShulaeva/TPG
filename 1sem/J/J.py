import sys


def map_seq(seq_num, action):
    return [eval(action) for x in seq_num]


def fil_seq(seq_num, action):
    return [x for x in seq_num if eval(action)]


def take_seq(seq_num, action):
    if action >= len(seq_num):
        return seq_num
    return seq_num[:action]


sequence_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for line in sys.stdin:
    if line.startswith('map'):
        sequence_of_numbers = map_seq(sequence_of_numbers, line[4:])
    elif line.startswith('filter'):
        sequence_of_numbers = fil_seq(sequence_of_numbers, line[7:])
    elif line.startswith('take'):
        sequence_of_numbers = take_seq(sequence_of_numbers, int(line[5:]))

for i in sequence_of_numbers:
    print(i, end=' ')