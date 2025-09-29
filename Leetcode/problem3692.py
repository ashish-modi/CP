# Leetcode problem : Majority Frequency characters
# Difficulty : easy
# Link : https://leetcode.com/problems/majority-frequency-characters/

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        length = len(s)
        dictionary = {element : 0 for element in s}
        count = {}
        store = [0]*(length+1)
        freq = maximum = 0
        for i in range(length):
            dictionary[s[i]] +=1
        # print(dictionary)
        for key,value in dictionary.items():
            if(count.get(value, 0)):
                count[value].append(key)
                store[value]+=1
            else:
                count[value] = [key]
                store[value] = 1
        # print("count: ", count)
        # print("store: ", store)
        for key,value in count.items():
            l = len(value)
            if(l == maximum and freq < key):
                maximum = l
                freq = key
                answer = value
            if(l > maximum):  
                maximum = l
                freq = key
                answer = value
        return("").join(answer)

# Time Complexity : O(N) where N is the number of characters in the input string.
# Space Complexity : O(1) as we are using only constant space.