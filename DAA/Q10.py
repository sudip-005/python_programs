arr = [3,5,2,3,0,9,1,5]
count = [0]*10

for x in arr:
    count[x] += 1

print("Sorted array:")
for i in range(10):
    print(i, end=" " * count[i])
