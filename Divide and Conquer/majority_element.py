# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr,l,r):

    if l < r:

        m = l + (r - l)//2

        #print(l,m,r)
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)

        merge(arr,l,m,r)
def majority_element(arr):
    assert len(arr) <= 10 ** 5
    count = 0
    k = arr[0]
    n = len(arr)
    l = 0
    # mergesingle(arr)
    merge_sort(arr, l, n - 1)
    for i in range(len(arr)):
        if k == arr[i]:
            count += 1

        elif k != arr[i] and count < n / 2:
            k = arr[i]
            count = 1

        if count > len(arr) / 2:
            return 1

    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
