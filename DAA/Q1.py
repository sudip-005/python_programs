arr = [1, 2, 4, 7, 11, 15]
X = 15
left, right = 0, len(arr) - 1
while left < right:
    s = arr[left] + arr[right]
    if s == X:
        print("Elements are", arr[left], "and", arr[right])
        break
    elif s < X:
        left += 1
    else:
        right -= 1
else:
    print("No such pair found")
