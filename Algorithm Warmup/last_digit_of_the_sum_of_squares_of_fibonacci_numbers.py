# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    global st
    assert 0 <= n <= 10 ** 18

    # a = 0
    # b = 1
    # if n <= 1:
    #     return n
    #
    # k = 1
    # for i in range(2, n + 1):
    #     a,b = b%10,(a+b)%10
    #     k = (k+(b*b))%10
    # return k


    sum = [0,1,2,6]

    lis = [0,1,1,2]
    i = 4
    while i < 70:
        lis.append((lis[i-1] + lis[i-2])%10)
        sum.append((sum[i-1] + lis[i]**2)%10)
        su = sum[2:]
        st = "".join(map(str,su))
        if "01" in st:
            break


        i +=1

    st = "01" + st[:-2]


    k = n%len(st)

    return int(st[k])






if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
