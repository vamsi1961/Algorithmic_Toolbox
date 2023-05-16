# python3

import random


def partition3(a, left, right):
    pivot_value = a[left]
    p_l = i = left
    p_e = right
    while i <= p_e:
        if a[i] < pivot_value:
            a[i], a[p_l] = a[p_l], a[i]
            p_l += 1
            i += 1
        elif a[i] == pivot_value:
            i += 1
        else:
            a[i], a[p_e] = a[p_e], a[i]
            p_e -= 1
        pIndexes = [p_l, p_e]
    return pIndexes


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    #print("k",k , array[k])
    array[left], array[k] = array[k], array[left]
    #print("q")
    #print("initial array" , array)
    m = partition3(array, left, right)
    randomized_quick_sort(array, left, m[0] - 1)
    randomized_quick_sort(array, m[1] + 1, right)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
