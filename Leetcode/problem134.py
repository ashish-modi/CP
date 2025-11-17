# Leetcode Problem 134: Gas Station
# Difficulty : Medium
# Link : https://leetcode.com/problems/gas-station/
# Based on Greedy Approach and Simulation

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        i = 0
        count = 0
        res = [False]*length
        start = 0
        curr = 0
        while True:
            if(count >= 2*length):
                break
            curr+= gas[i]
            
            if(curr - cost[(i)%length] >=0):
                curr -= cost[(i)%length]
                res[i] = True
            else:
                curr = 0
                start = (i+1)% length
            
            i+=1
            count +=1
            i = i% length
        
        for i in range(length):
            if(not res[i]):
                return -1
        return start

# Time Complexity : O(N) where N is the number of gas stations.
# Space Complexity : O(N) as we are using extra space for the res array.
# Explanation:
# 1. We initialize variables to keep track of the current index, count of iterations,
#    starting index, and current gas in the tank.
# 2. We use a while loop to simulate the process of traveling through the gas stations.
# 3. For each gas station, we add the gas available and check if we can reach the next station.
# 4. If we can reach the next station, we update the current gas and mark the station as reachable in the res array.
# 5. If we cannot reach the next station, we reset the current gas and update the starting index to the next station.