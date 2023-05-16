# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops.append(d)
    travelled = 0
    tank = m
    count = 0
    for i in range(len(stops)-1):
        #print(i)
        #print("new tank",tank)
        if tank >= stops[i] - travelled:
            tank -= (stops[i] - travelled)
            #print("tank" , tank)
            #print("next distance" , stops[i+1] - stops[i])
            travelled = stops[i]
            #print("travelled", travelled)
            if tank < (stops[i+1] - stops[i]):
                tank = m
                count +=1
                #print("count incremented........")
                if stops[i+1] >tank + stops[i]:
                    return -1
        elif tank == 0:
            tank = m
            count += 1
            #print("count incremented")
            #print("tank is filled")
            tank -= (stops[i] - travelled)
            travelled = stops[i]
        else:
            #print("wtf")
            return -1
        travelled =stops[i]
    #print("count",count)
    return count


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
