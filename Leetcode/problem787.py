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
# Explanation:
# 1. We initialize a cost array to keep track of the minimum cost to reach each city.
# 2. We perform k+1 iterations to allow for up to k stops.
# 3. In each iteration, we go through all the flights and update the cost to reach the destination city if a cheaper cost is found.
# 4. We use a temporary array to store the updated costs for the current iteration.
# 5. After k+1 iterations, we check the cost to reach the destination city. If it is still infinity, we return -1, otherwise we return the cost.