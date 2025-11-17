// Leetcode Problem 104 : Maximum Depth of Binary Tree 
// Difficulty: Easy
// https://leetcode.com/problems/maximum-depth-of-binary-tree/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == nullptr)
            return 0;
        int left = 0, right = 0;
        if(root-> left != nullptr)
            left = maxDepth(root->left);
        if(root-> right != nullptr)
            right = maxDepth(root->right);
        return 1 + max(left,right);
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack).
// Explanation:
// 1. We check if the current node is null; if so, we return a depth of 0.
// 2. We recursively calculate the maximum depth of the left and right subtrees.
// 3. We return the maximum of the two depths plus one (to account for the current node).