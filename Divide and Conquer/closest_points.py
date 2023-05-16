# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,distance_squared(p, q))

    return min_distance_squared

def strip_d(points,min_d):

    mid = len(points)//2
    mid_point =points[mid][0]
    strip_points = []

    for point in points:
        if abs(point[0] - mid_point) < min_d:
            strip_points.append(point)

    points_y = sorted(strip_points , key = lambda p:p[1])
    len_strip = len(points_y)

    if len_strip < 2:
        return min_d

    else:
        min_d2 = distance_squared(points_y[0] , points_y[1])
        for i in range(len_strip-1):
            for j in range(i+1 , min(i+7,len_strip)):
                min_d2 = min(min_d2 , distance_squared(points_y[i], points_y[j]))
        return min_d2



def minimum_distance_squared(points):



    points_x_sorted = sorted(points , key = lambda p:p[0])

    len_p = len(points_x_sorted)

    if len_p <= 3:
        return minimum_distance_squared_naive(points_x_sorted)

    else:

        mid = len(points_x_sorted)//2
        min_l = minimum_distance_squared(points_x_sorted[:mid])
        min_r = minimum_distance_squared(points_x_sorted[mid:])
        min_d = min(min_r,min_l)
        min_d2 = strip_d(points_x_sorted,min_d)
        result = min(min_d,min_d2)

    return result




if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
