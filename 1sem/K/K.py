def maximum(seq):
    if len(seq) == 1:
        return seq[0]
    else:
        return max(maximum(seq[:-1]), seq[-1])


line = [int(a) for a in input().split()]
print(maximum(line))