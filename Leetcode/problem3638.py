# Leetcode Problem 3638: Maximum Balanced Shipments
# Difficulty: Medium
# https://leetcode.com/problems/maximum-balanced-shipments/

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        length = len(weight)
        maximum = count = shipment = 0
        for i in range(length):
            count +=1
            if(maximum < weight[i]):
                maximum = weight[i]
            if(count > 1 and weight[i] < maximum):
                shipment +=1
                count = 0
                maximum = 0
        return shipment
                
# Time complexity: O(n)
# The loop iterates through the list once, making it O(n).
# Space complexity: O(1)
# No additional space is used that scales with input size.
# Explaination:
# The solution iterates through the weight list, keeping track of the maximum weight in the current shipment and the count of items.
# When it finds that the current item is less than the maximum weight and there are at least two items in the shipment, it counts that as a balanced shipment and resets the counters for the next shipment.
# Finally, it returns the total number of balanced shipments found.