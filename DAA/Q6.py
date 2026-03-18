value = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50

ratio = [v / w for v, w in zip(value, weight)]

total_value = 0

for i in range(len(value)):
    if capacity >= weight[i]:
        capacity -= weight[i]
        total_value += value[i]
    else:
        total_value += ratio[i] * capacity
        break

print("Maximum value =", round(total_value, 2))
