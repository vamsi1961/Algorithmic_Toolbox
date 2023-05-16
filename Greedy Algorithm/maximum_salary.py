# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    # print("start")
    # print(numbers)
    n = len(numbers)
    # print("n",n)

    for j in range(n):
        for i in range(0, n - j - 1):
            if int(str(numbers[i]) + str(numbers[i + 1])) < int(str(numbers[i + 1]) + str(numbers[i])):
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            # print(numbers)

    # print(numbers)
    fin = int(''.join(map(str, numbers)))
    fin = max(0, fin)
    # print(fin)

    return fin


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
