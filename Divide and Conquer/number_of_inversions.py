# Uses python3
import sys


def merge(a, b, left, ave, right):
    inv_count = 0
    i, j, k = left, ave, left
    while i <= ave - 1 and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            inv_count += ave - i
        k += 1
    while i <= ave - 1:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        a[i] = b[i]
    return inv_count


def compute_inversions(a, b, left, right):
    inv_count = 0
    if right > left:
        ave = (left + right) // 2
        inv_count += compute_inversions(a, b, left, ave)
        inv_count += compute_inversions(a, b, ave + 1, right)
        inv_count += merge(a, b, left, ave + 1, right)

    return inv_count


def compute_inversions_naive(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += compute_inversions_naive(a, b, left, ave)
    number_of_inversions += compute_inversions_naive(a, b, ave, right)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(compute_inversions(a, b, 0, len(a) - 1))
