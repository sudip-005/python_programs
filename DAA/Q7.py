def solve(a):
    if len(a) == 1:
        return a[0], float('inf'), a[0], float('-inf')
    m = len(a)//2
    l = solve(a[:m])
    r = solve(a[m:])
    mn = min(l[0], r[0])
    mx = max(l[2], r[2])
    smin = min(l[1], r[0]) if l[0] < r[0] else min(r[1], l[0])
    smax = max(l[3], r[2]) if l[2] > r[2] else max(r[3], l[2])
    return mn, smin, mx, smax

arr = [4,1,7,3,9,5]
_, smin, _, smax = solve(arr)
print("Second Smallest =", smin)
print("Second Largest =", smax)
