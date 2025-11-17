// Leetcode Problem 114 : Flatten binary tree into Linked list
// Difficulty: Medium
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

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
    TreeNode* construct_tree(TreeNode* root){
        if(root == nullptr)
            return root;
        
        // TreeNode* node = new TreeNode(root->val);
        TreeNode* leftTail = construct_tree(root->left);
        TreeNode* rightTail = construct_tree(root->right);

        // root->right = left_subtree;
        if (root->left) {
            if (leftTail)
                leftTail->right = root->right;
            root->right = root->left;
            root->left = nullptr;
        }

        if (rightTail)
            return rightTail;      
        else if (leftTail)
            return leftTail;       
        else
            return root;           
            
    }
    void flatten(TreeNode* root) {
        construct_tree(root);
        
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack).
// Explanation:
// 1. We define a recursive function `construct_tree` that flattens the binary tree.
// 2. The base case checks if the current node is null; if so, we return null.
// 3. We recursively flatten the left and right subtrees and obtain their tails.
// 4. If the left subtree exists, we attach it to the right of the current node and connect the original right subtree to the tail of the left subtree.
// 5. We return the tail of the flattened subtree, which is either the right tail, left tail, or the current node itself if both subtrees are null.
// 6. The main function calls the `construct_tree` function to flatten the entire tree.