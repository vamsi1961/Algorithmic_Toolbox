# python3


def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(lis):
    assert len(lis) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in lis)
    max_index = 0
    for i in range(len(lis)):
        if lis[i] >= lis[max_index]:
            max_index = i
    max1 = lis[max_index]
    lis.pop(max_index)

    max_index = 0
    for j in range(len(lis)):
        if lis[j] >= lis[max_index]:
            max_index = j

    max2 = lis[max_index]

    return max1 *max2


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
