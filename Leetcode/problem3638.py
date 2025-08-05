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
# The variables used are constant space.
# The space complexity is O(1) since we only use a few integer variables.
# The algorithm does not require any additional data structures that grow with input size.
# The space used is constant, regardless of the input size.
# The space complexity is O(1) as it uses a fixed number of variables.