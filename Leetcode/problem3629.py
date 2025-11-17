# Test cases
# [1,2,4,6]
# [2,3,4,7,9]
# [4,6,5,8]
# [2,3,4,5,6,7,8]
# [5,7,9,5,1]
# [17,114,68,110,9,100,7,19,111,65,28]
# [893,786,607,137,69,381,790,233,15,42,7,764,890,269,84,262,870,514,514,650,269,485,760,181,489,107,585,428,862,563]
# [7,17,19,23,39,11,29,31,13,14,47,53,59,61,55]


# Problem : Minimum jumps to reach end via prime teleportation (medium)

class Solution:
    def bfs(self, start, primes, nums, length):
        q = []
        q.append([start])
        visited = [0]*length
        visited[start]= 1
        q_index = 0
        elements = 1
        while(True):
            node = q[q_index]
            new_nodes = []
            ele = 0
            flag = 0
            for i in range(elements):
                curr_index = node[i]
                if(curr_index == length -1):
                    return q_index
                if(curr_index -1 >= 0 and not visited[curr_index -1]):  # adjacent step
                    new_nodes.append(curr_index-1)
                    ele +=1
                    flag = 1
                    visited[curr_index-1] = 1
                if(primes[nums[curr_index]]):
                    for j in range(length):
                        if(curr_index != j and not visited[j] and nums[j] % nums[curr_index] == 0):   # prime element
                            new_nodes.append(j)
                            ele+=1
                            flag = 1
                            visited[j] = 1
                if(curr_index + 1 < length and not visited[curr_index + 1]):  # adjacent step
                    new_nodes.append(curr_index + 1)
                    ele+=1
                    flag = 1
                    visited[curr_index + 1] = 1

            elements = ele
            if(flag):
                q_index +=1
                q.append(new_nodes)

    def primes(n):
        primes = [True]*(n+1)
        primes[0] = primes[1] = False
        for i in range(2,int(sqrt(n))+1):
            t = i+i
            if(primes[i]):
                while(t < (n+1)):
                    primes[t] = False
                    t+=i
        return primes
        
    
    def minJumps(self, nums: List[int]) -> int:
        length= len(nums)
        return self.bfs(0, primes_list, nums, length)

primes_list = Solution.primes(1000000)

                