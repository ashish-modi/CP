# Leetcode Problem 787: Cheapest Flights Within K Stops
# Difficulty: Medium
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Based on Bellman-Ford Algorithm 

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        length = len(flights)
        cost = [float('inf')]*n
        temp = [float('inf')]*n
        cost[src] = 0
        temp[src] = 0
        for i in range(k+1):
            for j in range(length):
                source, dest, price = flights[j]
                if(cost[source] + price < temp[dest]):
                    temp[dest] = cost[source] + price
            for m in range(n):
                cost[m] = temp[m]
        return -1 if(cost[dst] == float('inf')) else cost[dst]

# Time Complexity: O(k * E) where E is the number of flights
# Space Complexity: O(V) where V is the number of vertices (cities) 