matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

key = 16
n, m = len(matrix), len(matrix[0])

low, high = 0, n*m - 1

while low <= high:
    mid = (low + high) // 2
    row, col = mid // m, mid % m

    if matrix[row][col] == key:
        print(f"Element found at position ({row}, {col})")
        break
    elif matrix[row][col] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")