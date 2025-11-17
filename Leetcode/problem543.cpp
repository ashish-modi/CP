// Leetcode Problem 543: Diameter of Binary Tree (Easy)
// Difficulty: Easy
// https://leetcode.com/problems/diameter-of-binary-tree/

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

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack).
// Explanation:
// 1. We define a helper function `height` that returns a pair containing the height of the subtree and the maximum diameter found in that subtree.
// 2. The base case checks if the current node is null; if so, we return a height of 0 and diameter of 0.
// 3. We recursively calculate the height and diameter of the left and right subtrees.
// 4. The height of the current node is 1 plus the maximum height of its left and right subtrees.
// 5. The diameter at the current node is the sum of the heights of the left and right subtrees.
// 6. We return the maximum diameter found in the subtree.
// 7. The main function calls the `height` function and returns the diameter.