# Sparse Table Construction for Range Minimum Query (RMQ): 

# Intuition:
# The sparse table allows us to precompute answers for overlapping intervals of the array.
# This enables efficient range minimum queries in O(1) time after O(n log n) preprocessing time.

# Sparse table is particularly useful for immutable arrays where multiple range queries are needed.

arr = [ 7, 2, 3, 43, 5, 10, 3, 12, 18 ]

def build_table(arr):
    n = len(arr)
    k = n.bit_length()  # Calculate maximum power of 2 <= n
    st = [[0] * n for _ in range(k)]

    for i in range(n):
        st[0][i] = arr[i]

    for i in range(1, k):
        j = 0 
        while j + (1 << i) <= n:
            st[i][j] = min(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])
            j += 1

    return st

def query(st, L, R):
    j = (R - L + 1).bit_length() - 1
    return min(st[j][L], st[j][R - (1 << j) + 1])

sparse_table = build_table(arr)


for row in sparse_table:
    print(row)

# Time Complexity: O(n log n)
# Space Complexity: O(n log n)
# Explanation:
# 1. The first loop initializes the first row of the sparse table with the original array values.
# 2. The second nested loop fills in the rest of the table by combining results from previous rows.
# 3. Each entry st[i][j] represents the minimum value in the range of length 2^i starting at index j.

# Example Output:
# [7, 2, 3, 43, 5, 10, 3, 12, 18]
# [2, 2, 3, 5, 5, 3, 3, 12, 0]
# [2, 2, 3, 3, 3, 3, 0, 0, 0]
# [2, 2, 0, 0, 0, 0, 0, 0, 0]