# Leetcode Problem 735 : Asteroid Collision
# Difficulty : Medium
# URL : https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        length = len(asteroids)
        stack = deque()
        for i in range(length):
            element = asteroids[i]
            flag=0
            while(stack and stack[-1] > 0 and element < 0):
                if(abs(element) == abs(stack[-1])):
                    stack.pop()
                    flag = 1
                    break
                elif(abs(element) > abs(stack[-1])):
                    stack.pop()
                else:
                    flag = 1
                    break
            if flag:
                continue
            else:
                stack.append(element)
        return list(stack)          
    
# Time complexity : O(n)
# Space complexity : O(n)
# Explaination : The solution uses a stack to keep track of the asteroids that are still in motion. 
# It iterates through the list of asteroids and for each asteroid, it checks if there is a collision with the last asteroid in the stack. 
# If there is a collision, it compares the sizes of the two asteroids and determines which one will survive. 
# If the current asteroid is larger than the last asteroid in the stack, 
# it pops the last asteroid from the stack and continues checking for collisions until it finds an asteroid that is larger or equal in size to the current asteroid. 
# If the current asteroid is smaller than the last asteroid in the stack, it simply ignores it and moves on to the next asteroid. Finally, it returns a list of the remaining asteroids in the stack.    