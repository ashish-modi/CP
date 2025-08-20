class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        max_length = max(map(len, wordDict))
        answer = [False]*length
        word = []
        i=0
        last_match = 0
        while(i < length):
            flag = 0
            for j in range(min(i+max_length -1, length-1), i-1, -1):
                if(s[i:j+1] in wordDict):
                    word.append(s[i:j+1])
                    i = j+1
                    last_match = j+1
                    flag = 1
                    break
            if(not flag):
                i+=1
                    
        return last_match == length