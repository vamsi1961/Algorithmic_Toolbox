# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, low, high, query):
    r = -1
    if low <= high:

        mid = (low + high) // 2
        # print("low and mid",  low,mid)
        if keys[mid] == query:

            return mid

        elif query < keys[mid]:
            high = mid - 1
            return binary_search(keys, low, high, query)

        else:

            low = mid + 1
            return binary_search(keys, low, high, query)

    return r


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        low, high = 0, num_keys - 1
        print(binary_search(input_keys, low, high, q), end=' ')
