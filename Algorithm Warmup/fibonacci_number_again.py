# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    lis = [0,1,1]
    i =3

    while True:
        lis.append((lis[i-1] + lis[i-2]) %m)
        if i>2:
            #print(lis)
            if (lis[i] == 1) and (lis[i-1] == 1) and (lis[i-2] == 0):
                lis = lis[:-3]

                break

        i+=1
    #print(lis)
    _,car = divmod(n,len(lis))
    return lis[car]


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
