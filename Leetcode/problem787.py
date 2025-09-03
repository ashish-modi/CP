class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        length = len(flights)
        graph = [[] for _ in range(n)]
        for i in range(length):
            source, dst, price = flights[i]
            graph[source].append((price, dst))
        p = [] # heap
        visited = [0]*n
        cost = [float('inf')]*n
        heapq.heappush(p,(0,src))
        cost[src] = 0
        while(p):
            price, source = heapq.heappop(p)
            if(not visited[source]):
                for wt, neigh in graph[source]:
                    if(cost[neigh] > wt + price):
                        cost[neigh] = wt + price
                        heapq.heappush(p,(cost[neigh], neigh))
        print("COST : ", cost)