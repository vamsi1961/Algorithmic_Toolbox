# python3 (this comment tells the grading system at Coursera to use python3 rather than python3)


def sum_of_two_digits(first,second):
    return first + second


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
