// Problem : Diameter of Binary Tree (Easy)

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
    

pair<int,int> height(TreeNode* root) {
    if(root == nullptr)
        return {0, 0};
    // cout << "root : " << root->val << endl;
    int left = 0, right = 0, max_left_h = 0, max_right_h = 0;
    if(root-> left != nullptr){
        auto p = height(root->left);
        left = p.first;
        max_left_h = p.second;
        // cout << "left : " << left << " for " << root->val << endl;
    }
    if(root-> right != nullptr){
        auto p = height(root-> right);
        right = p.first;
        max_right_h = p.second;
        // cout << "right : " << right << " for " << root->val << endl;
    }
    int h = max({left + right, max_left_h, max_right_h});
    return {1 + max(left, right), h};
}
int diameterOfBinaryTree(TreeNode* root) {
    auto [h, diameter] = height(root);
    // cout << "Max height : " <<  h << endl;
    return diameter;
}
};