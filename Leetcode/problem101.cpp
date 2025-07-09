// Problem : Symmetric tree (Easy)

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