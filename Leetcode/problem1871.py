# LeetCode Problem 1871: Jump Game VII
# Difficulty: Medium
# URL: https://leetcode.com/problems/jump-game-vii/

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        length = len(s)
        queue = deque()
        queue.append(0)
        farthest = 0
        while(queue):
            ele = queue.popleft()
            start = max(ele + minJump, farthest + 1)
            for i in range(start, min(ele + maxJump + 1, length)):
                if (s[i] == "0"):
                    queue.append(i)
                    if(i == length-1):
                        return True
            farthest = ele + maxJump
        return False
    
# Time Complexity: O(N) where N is the length of the string s.
# Space Complexity: O(N) for the queue used in BFS.
# Explanation:
# 1. We use a BFS approach to explore all reachable indices in the string s.
# 2. We maintain a queue to keep track of the current positions we can jump from.
# 3. For each position, we calculate the valid jump range [minJump, maxJump] and enqueue all reachable indices that contain '0'.
# 4. We also keep track of the farthest index we have processed to avoid redundant checks.
# 5. If we reach the last index of the string, we return True. If we exhaust all possibilities without reaching the end, we return False.