# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    lis = [0,1,1]
    i =3
    sum = [0,1,2]
    while(True):
        lis.append((lis[i-1] + lis[i-2])%10)
        k = sum[i-1] + lis[i]
        sum.append(k%10)
        li = sum[2:]
        st = "".join(map(str,li))

        if "01" in st:
            break
        i +=1

    sum = sum[:-2]

    k = n%len(sum)

    return sum[k]

if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
