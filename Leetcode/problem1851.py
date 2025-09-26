# Leetcode Problem 1851: Minimum Interval to Include Each Query
# Difficulty : Hard
# Link : https://leetcode.com/problems/minimum-interval-to-include-each-query/
# Based on Sorting and Min-Heap (Priority Queue)

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        length = len(intervals)
        q_length = len(queries)
        queries_with_index = [(q, i) for i, q in enumerate(queries)]
        result = [0]*q_length
        intervals.sort()
        min_heap = []
        j = 0
        for q, idx in sorted(queries_with_index):
            element = q
            while(j < length and intervals[j][0] <= element):
                heapq.heappush(min_heap, (intervals[j][1] - intervals[j][0] + 1, intervals[j][1]))
                j+=1
            while(min_heap and min_heap[0][1] < element):
                heapq.heappop(min_heap)
            result[idx] = min_heap[0][0] if min_heap else -1
        return result

# Time Complexity : O(N log N + Q log Q) where N is the number of intervals and Q is the number of queries.
# Space Complexity : O(N) as we are using extra space for the min-heap.
