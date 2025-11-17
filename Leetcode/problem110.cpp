// Leetcode Problem 110 : Balanced binary tree 
// Difficulty: Easy
// https://leetcode.com/problems/balanced-binary-tree/

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
    pair<int,bool> height(TreeNode* root){
        if(root == nullptr)
            return {0,true};
        int left = 0, right = 0;
        bool left_bal = false, right_bal = false;
        if(root->left != nullptr){
            auto p = height(root->left);
            left = p.first;
            left_bal = p.second;


        }
        if(root->right != nullptr){
            auto p = height(root->right);
            right = p.first;
            right_bal = p.second;

        }
        int h = 1 + max(left,right);
        if(root->left == nullptr)
            left_bal = true;
        if(root->right == nullptr){
            right_bal = true;
        }
        if(abs(left - right) <=1 && left_bal && right_bal){
            return {h, true};
        }
        else{
            return {h, false};
        }
    }
    bool isBalanced(TreeNode* root) {
        auto p = height(root);
        return p.second;
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack).
// Explanation:
// 1. We define a helper function that returns a pair containing the height of the subtree and a boolean indicating whether the subtree is balanced.
// 2. The base case checks if the current node is null; if so, we return a height of 0 and true for balanced.
// 3. We recursively calculate the height and balance status of the left and right subtrees.
// 4. We calculate the height of the current node as 1 plus the maximum height of the left and right subtrees.
// 5. We check if the current subtree is balanced by ensuring the absolute difference in heights is at most 1 and both subtrees are balanced.
// 6. Finally, we return the balance status of the entire tree from the main function.

