# Leetcode problem 3691: Maximum Total subarray value II
# Difficulty: Hard
# Link: https://leetcode.com/problems/maximum-total-subarray-value-ii/


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        heap = []
        seen = set()
        length = len(nums)
        size = length.bit_length() 
        max_st = [[0]* length for _ in range(size)]
        min_st = [[0]* length for _ in range(size)]
        total  = 0

        def build_table(arr):
            
            
            for i in range(length):
                max_st[0][i] = arr[i]
                min_st[0][i] = arr[i]

            for i in range(1, size):
                j = 0 
                while j + (1 << i) <= length:
                    max_st[i][j] = max(max_st[i - 1][j], max_st[i - 1][j + (1 << (i - 1))])
                    min_st[i][j] = min(min_st[i - 1][j], min_st[i - 1][j + (1 << (i - 1))])
                    j += 1

        def query_min(L, R):
            j = (R - L + 1).bit_length() - 1
            return min(min_st[j][L], min_st[j][R - (1 << j) + 1])

        def query_max(L, R):
            j = (R - L + 1).bit_length() - 1
            return max(max_st[j][L], max_st[j][R - (1 << j) + 1])


        build_table(nums)        
        heapq.heappush(heap, (-(query_max(0,length-1) - query_min(0, length -1)),0, length-1) )
        seen.add((0,length-1))
        for i in range(k):
            score, l, r = heapq.heappop(heap)
            total += -score
            if(l+1 <= r and (l+1, r) not in seen):
                heapq.heappush(heap, (-(query_max(l+1, r) - query_min(l+1, r)), l+1, r))
                seen.add((l+1, r))
            if(r-1 >= l and (l, r-1) not in seen):
                heapq.heappush(heap, (-(query_max(l, r-1) - query_min(l, r-1)), l, r-1))
                seen.add((l, r-1))
        return total        

# Time Complexity: O(n log n + k log k)
# Space Complexity: O(n log n + k)
# Explanation:
# 1. We build two sparse tables, one for range maximum queries and another for range minimum queries.
# 2. We use a max-heap to keep track of the maximum subarray values and their corresponding indices.
# 3. We pop the maximum value from the heap, add it to the total, and push the next possible subarrays into the heap.
# 4. We repeat this process k times to get the maximum total value of k subarrays.