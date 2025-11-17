# Leetcode Problem 846: Hand of Straights
# Difficulty : Medium
# Link : https://leetcode.com/problems/hand-of-straights/
# Based on HashMap and Sorting

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        length = len(hand)
        dictionary = {element:0 for element in hand}
        for i in range(length):
            dictionary[hand[i]]+=1
        
        length_dict = len(dictionary)
        i = 0
        sorted_dict = [0]*length_dict
        for key, value in dictionary.items():
            sorted_dict[i] = [key, value]
            i+=1
        sorted_dict = sorted(sorted_dict)
        index = 0
        result = []
        while(True):
            while(index < length_dict and sorted_dict[index][1] == 0):
                index +=1
            if(index == length_dict):
                break
            item = sorted_dict[index][0]
            sorted_dict[index][1]-=1
            k = 1
            itr = 1
            res = [item]
            while(itr < groupSize):
                while((index + k) < length_dict and sorted_dict[index+k][1] <= 0):
                    k+=1
                
                if(index+k >= length_dict):
                    return False
                new_val = sorted_dict[index + k][0]
                if(new_val == item +1):
                    item = new_val
                    sorted_dict[index + k][1] -=1
                    k+=1
                    itr +=1
                else:
                    return False
        return True  

# Time Complexity : O(N log N) where N is the number of elements in the input array.
# Space Complexity : O(N) as we are using extra space for the dictionary and sorted list.   
# Explanation:
# 1. We create a dictionary to count the occurrences of each card in the hand.
# 2. We sort the unique cards to process them in order.
# 3. We iterate through the sorted cards and for each card, we try to form a group of consecutive cards of size `groupSize`.
# 4. If we can successfully form groups for all cards, we return True; otherwise, we return False.