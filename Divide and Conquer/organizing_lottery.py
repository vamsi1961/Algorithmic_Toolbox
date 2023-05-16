# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    #print("wtf")
    start_label = 0
    point_label = 1
    end_label = 2

    point_count = [0] * len(points)
    combined = []
    point_map = {}

    for s in starts:
        combined.append((s, start_label))

    for e in ends:
        combined.append((e, end_label))

    for i, p in enumerate(points):
        combined.append((p, point_label))
        if p not in point_map:
            point_map[p] = [i]

        else:
            point_map[p].append(i)

    comb_sort = sorted(combined, key=lambda c: (c[0], c[1]))
    count = 0
    for item in comb_sort:

        if item[1] == start_label:
            count += 1

        elif item[1] == end_label:
            count -= 1

        elif item[1] == point_label:
            indices = point_map[item[0]]
            for i in indices:
                point_count[i] = count

    return point_count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
