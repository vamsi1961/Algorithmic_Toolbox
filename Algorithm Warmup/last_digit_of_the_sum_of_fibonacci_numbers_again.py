# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    lis = [0, 1, 1]
    i = 3
    sum = [0, 1, 2]
    while True:
        lis.append((lis[i - 1] + lis[i - 2]) % 10)
        k = sum[i - 1] + lis[i]
        sum.append(k % 10)
        li = sum[2:]
        st = "".join(map(str, li))

        if "01" in st:
            break
        i += 1

    sum = sum[:-2]

    k_start = from_index % len(sum)
    k_end = to_index % len(sum)

    # print(sum[k_start])
    # print(sum[k_end])

    if (sum[k_end] - sum[k_start-1]) < 0:
        return sum[k_end] - sum[k_start-1] +10

    else:
        return sum[k_end] - sum[k_start-1]


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
