def squares(n):
    i = 0
    l = []
    while i <= n:
        sq = int(i ** 0.5)
        if sq * sq == i:
            l.append(i)
        i += 1

    return l
print(squares(10))
