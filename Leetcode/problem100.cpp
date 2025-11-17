// Leetcode Problem 100 : Same Tree
// Difficulty : Easy
// Link : https://leetcode.com/problems/same-tree/


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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == nullptr && q == nullptr)
            return true;
        if((p == nullptr && q != nullptr) || (q == nullptr && p != nullptr))
            return false;
        bool left = false, right = false;
        left = isSameTree(p->left, q->left);
        right = isSameTree(p->right, q->right);
        if(p->val == q->val && left && right)
            return true;
        else
            return false;
    }
};

// Time Complexity: O(min(m, n)) where m and n are the number of nodes in trees p and q respectively.
// Space Complexity: O(min(h1, h2)) where h1 and h2 are the heights of trees p and q respectively due to the recursion stack in the worst case (skewed tree).
// Note: This solution uses recursion to traverse both trees simultaneously and compare their structure and node values.
// Explanation:
// 1. We check if both nodes are null, in which case they are the same (return true).
// 2. If one node is null and the other is not, they are different (return false).
// 3. We recursively check the left and right subtrees of both nodes.
// 4. Finally, we compare the values of the current nodes and the results of the left and right subtree comparisons to determine if the trees are the same.