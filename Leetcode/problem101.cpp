// Leetcode Problem 101: Symmetric tree (Easy)
// Difficulty: Easy
// https://leetcode.com/problems/symmetric-tree/

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
    
    bool helper(TreeNode* node1, TreeNode* node2){
        if(node1 == nullptr && node2 == nullptr)
            return true;
        if((node1 == nullptr && node2 != nullptr ) || (node1 != nullptr && node2 == nullptr))
            return false;
        if(node1->val == node2->val){
            bool left = helper(node1->left, node2->right);
            bool right = helper(node1->right, node2->left);
            if(left && right)
                return true;
            else
                return false;
        }
        else
            return false;
    }
    bool isSymmetric(TreeNode* root) {
        return helper(root->left, root->right);
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack).
// Explanation:
// 1. We define a helper function that takes two nodes and checks if they are mirror images of each other.
// 2. The base case checks if both nodes are null (return true) or if one is null and the other is not (return false).
// 3. If the values of the two nodes are equal, we recursively check the left subtree of the first node with the right subtree of the second node and vice versa.
// 4. If both recursive calls return true, we return true; otherwise, we return false.
// 5. The main function calls the helper function with the left and right children of the root node.