#coding:utf8
def rle(l):
    if l:
        acc = []
        current = l[0]
        counter = 0
        for e in l:
            if e == current:
                counter += 1
            else:
                acc.append(str(counter))
                acc.append(str(current))
                current = e
                counter = 1
        acc.append(str(counter))
        acc.append(str(current))
        acc = " ".join(acc)
    return acc

l = [int(n) for n in input('Числа через пробел - ').split()]

print(rle(l))