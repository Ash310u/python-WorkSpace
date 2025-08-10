for x in range (100, 1000):
    z = x
    sum = 0
    while (z > 0):
        y = z % 10
        sum += y*y*y
        z = z // 10

    if sum == x:
        print(x);