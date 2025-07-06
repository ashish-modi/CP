// Problem : Balanced binary tree (Easy)

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