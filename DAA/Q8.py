import bisect

arr = [1,2,2,2,3,4]
x = 2
print("Occurrences =", bisect.bisect_right(arr,x)-bisect.bisect_left(arr,x))
