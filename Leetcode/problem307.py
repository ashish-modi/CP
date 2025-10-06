# LeetCode Problem 307: Range Sum Query - Mutable
# Difficulty: Medium
# Link: https://leetcode.com/problems/range-sum-query-mutable/

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)
        self.tree = [0]*(4*self.length)
        # self.dictionary = {}
        self.buildTree(0,0,self.length-1)
        # print("Tree : ", self.tree)
        
    
    def buildTree(self, index, left, right):
        # self.dictionary[(left,right)] = index
        if(left == right):
            # print("INDEX : ", index)
            self.tree[index] = self.nums[left]
            return 
        mid = (left + right)//2
        # print("Mid : ", mid)
        self.buildTree(2*index+1, left, mid)
        self.buildTree(2*index+2, mid+1, right)
        self.tree[index] = self.tree[2*index+1] + self.tree[2*index+2]
        return 

    def updateTree(self, tree_index, left, right, index, value):
        if(left == right == index):
            # print("left : ", left, "Right : ", right, "Index : ", index)

            self.tree[tree_index] = value
            return 
        mid = (left + right) //2
        if(index <= mid):
            self.updateTree(2*tree_index+1, left, mid, index, value)
        else:
            self.updateTree(2*tree_index+2, mid+1, right, index, value)

        self.tree[tree_index] = self.tree[2*tree_index+1] + self.tree[2*tree_index + 2]
        return 

    def update(self, index: int, val: int) -> None:
        self.updateTree(0, 0, self.length-1, index, val)
        # print("tree : ", self.tree)

    def calculate_sum(self, tree_index, tree_left, tree_right, left, right):
        
        if((tree_left >= left) and (tree_right <= right)):
            
            return self.tree[tree_index]
        elif(tree_right < left or tree_left > right):
            
            return 0
        mid = (tree_left + tree_right)//2
        ans_left = self.calculate_sum(2*tree_index + 1, tree_left, mid, left, right)
        ans_right = self.calculate_sum(2*tree_index + 2, mid+1, tree_right, left, right)
        return ans_left + ans_right

    def sumRange(self, left: int, right: int) -> int:
        return self.calculate_sum(0, 0, self.length-1, left, right)
        # return self.tree[self.dictionary[(left,right)]]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# Time Complexity: O(log n) for update and sumRange operations
# Space Complexity: O(n) for the segment tree storage   