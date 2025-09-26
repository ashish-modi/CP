class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        dictionary = {}
        i = maximum = 0
        prev = 1
        while(i < length):
            if(dictionary.get(s[i],0)):
                dictionary[s[i]] = i+1
                l_subs = (i - prev + 1)
                print("Lsubs : ", l_subs)
                maximum = max(l_subs, maximum)
                prev = i + 1
            else:
                dictionary[s[i]] = i+1
            i+=1
            print("Dictionary: ", dictionary)
        maximum = max(i - prev, maximum)
        return 1 if(maximum == 0) else maximum