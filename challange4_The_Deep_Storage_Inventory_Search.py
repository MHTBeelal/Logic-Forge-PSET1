def kth_smallest(matrix, k):
    n = len(matrix)
    left = matrix[0][0]
    right = matrix[n - 1][n - 1]

    def count_less_equal(mid):
        count = 0
        row = n - 1
        col = 0
        
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

size = int(input("size n x n: "))

matrix = []

print("matrix:")
for i in range(size):
    row = list(map(int, input().split(',')))
    matrix.append(row)


k = int(input("k: "))

print("\nOutput:",kth_smallest(matrix, k))
