# Leetcode problem 881: Boats to Save People
# Difficulty: Medium
# URL : https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        length = len(people)
        boats = left = 0
        right = length-1
        
        while(left < right):
            if(people[left] + people[right] <= limit):
                left += 1
                right -=1
                boats +=1
            else:
                right -=1
                boats +=1
        if(left == right):
            boats +=1
        return boats
    
# Time complexity: O(nlogn)
# Space complexity: O(1)
# Explanation: We sort the array of people and use two pointers to find the minimum number of boats needed to save everyone. 
# We start with the lightest and heaviest person and check if they can be accommodated in the same boat.
# If they can, we move both pointers and increment the boat count.
# If they cannot, we move the right pointer and increment the boat count.

