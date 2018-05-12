list_l = [int(n) for n in input().split()]
new_list_l = sorted(set(list_l), reverse = True)
op = ' '.join(map(str, new_list_l))
print(op)
