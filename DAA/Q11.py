def partition(a, l, r):
    pivot = a[r]
    i = l
    for j in range(l, r):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r] = a[r], a[i]
    return i

def quick_select(a, l, r, k):
    if l <= r:
        p = partition(a, l, r)
        if p == k:
            return p
        elif p > k:
            return quick_select(a, l, p-1, k)
        else:
            return quick_select(a, p+1, r, k)

arr = [7,2,1,6,8,5,3]
n = len(arr)
m = n//2

idx = quick_select(arr, 0, n-1, m)

print("Median =", arr[idx])
print("Neighbors =", arr[idx-1], "and", arr[idx+1])
