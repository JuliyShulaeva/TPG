# Метод hash() возвращает хеш-значение объекта, если оно есть.


def create_hash_set(dimension):
    return [[] for _ in range(dimension)]


def add_in_hash(the_value, new_hash_set):
    place = hash(the_value) % len(new_hash_set)
    if the_value not in new_hash_set[place]:
        new_hash_set[place].append(the_value)


def sort_hash(new_hash_set, reverse):
    new_list_sort = []
    for box in new_hash_set:
        new_list_sort += box

    return sorted(new_list_sort, reverse=reverse)


hash_set = create_hash_set(32)

for i in input().split(' '):
    add_in_hash(int(i), hash_set)

new_list = sort_hash(hash_set, reverse=True)

for i in new_list:
    print(i, end=' ')
