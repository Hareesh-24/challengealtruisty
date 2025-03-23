def power_consumption(v):
    for x in v:
        if x < 10 or x > 200:
            print("INVALID")
            return
    average = []
    for i in range(5):
        sum1 = 0
        for j in range(4):
            sum1 += v[i + j * 5]
        average.append(sum1 // 4)
    max_avg = max(average)
    if max_avg < 50:
        print("Energy consumption is optimal.")
    else:
        print("sensor number:",average.index(max_avg) + 1)




v = list(map(int, input().split()))
if len(v) != 20:
    print("INVALID")
else:
    power_consumption(v)
