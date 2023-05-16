# python3

from sys import stdin


def get_weights(cost):
    #print(cost)
    k = 0
    ind = -1
    for i in range(len(cost)):
        if k < cost[i]:
            k = cost[i]
            ind = i

    return ind


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    lis = []
    for i in range(len(weights)):
        lis.append(prices[i] / weights[i])
    ans = 0
    #print("start")
    #print(capacity, weights, prices)
    while True:
        i = get_weights(lis)
        #print(i)

        wei = min(capacity, weights[i])
        capacity -= wei
        ans += wei * lis[i]

        weights.pop(i)
        prices.pop(i)
        lis.pop(i)
        #print(ans)

        if capacity == 0:
            return ans

        if len(weights) == 0:
            return ans



if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    # noinspection PyStringFormat
    print("{:.10f}".format(opt_value))
