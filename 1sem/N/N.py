__author__ = 'student'


def create_hash_set(dimension):
    return {'data': [[] for _ in range(dimension)], 'size': 0}


def add_in_hash(the_value, new_hash_set):
    place = hash(the_value) % len(new_hash_set['data'])
    if the_value not in new_hash_set['data'][place]:
        new_hash_set['data'][place].append(the_value)
        new_hash_set['size'] += 1
    test =  new_hash_set['size'] / len(new_hash_set['data'])
    if test >= 0.75:
        load_factor(new_hash_set)


def sort_hash(new_hash_set, reverse):
    new_list_sort = []
    for box in new_hash_set['data']:
        new_list_sort += box
    return sorted(new_list_sort, reverse=reverse)


def load_factor(r):
    t = len(r['data'])
    new_set = create_hash_set(t * 2)
    for bucket in r['data']:
        for el in bucket:
            add_in_hash(el, new_set)

    r['data'] = new_set['data']
    r['size'] = new_set['size']


hash_set = create_hash_set(5)

for i in input().split(' '):
    add_in_hash(int(i), hash_set)

new_list = sort_hash(hash_set, reverse=True)

for i in new_list:
    print(i, end=' ')