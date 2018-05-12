def triangle(m, n, h):
    if m + n >= h and m + h >= n and n + h >= m:
        print("true")
    else:
        print("false")


length1, length2, length3 = input().split()
length1 = int(length1)
length2 = int(length2)
length3 = int(length3)

triangle(length1, length2, length3)