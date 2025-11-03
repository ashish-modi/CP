# LeetCode Problem 818 : Race Car
# Difficulty: Hard
# URL: https://leetcode.com/problems/race-car/

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0,0,1))
        visited = {}
        while(queue):
            moves, position, speed = queue.popleft()
            if(position == target):
                return moves
            
            if (not visited.get((position, speed), 0)):
                queue.append((moves +1, position + speed, speed*2))
                visited[(position, speed)] = 1
                if(position + speed > target and speed > 0) or (position + speed < target and speed < 0 ):          
                    new_speed = 1 if speed < 0 else -1
                    queue.append((moves + 1, position, new_speed))


# Time complexity: O(N log N) where N is the target position.
# Space complexity: O(N) for the queue and visited dictionary.
# # Explanation: The solution uses a breadth-first search (BFS) approach to explore all possible positions and speeds of the race car. 
# It keeps track of the number of moves taken to reach each position and speed combination, and returns the minimum number of moves required to reach the target position.