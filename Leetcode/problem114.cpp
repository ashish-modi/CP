// Problem : Flatten binary tree into Linked list (Medium)

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