// Leetcode Problem 105: Construct binary tree from preorder and inorder traversal
// Difficulty: Medium
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    pair<TreeNode*, int> tree(vector<int>& preorder,  vector<int>& inorder, map<int,int>& dict, int start, int end, int root_index){
        if(start > end)
            return {nullptr, root_index};
        TreeNode * node = new TreeNode(preorder[root_index]);
        int index = dict.at(node->val);

        auto l = tree(preorder, inorder, dict, start, index -1, root_index +1);
        node->left = l.first;
        
        auto r = tree(preorder, inorder, dict, index + 1, end, l.second);
        node->right = r.first;
        return {node, r.second};
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int length = inorder.size();
        map<int,int> dict = {};
        for(int i = 0; i< length ; i++)
            dict[inorder[i]] = i;
        pair<TreeNode*, int> p = tree(preorder, inorder, dict, 0, length-1, 0);
        return p.first;
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack) and O(N) for the hashmap.
// Explanation:
// 1. We create a hashmap to store the indices of the inorder traversal for quick access.
// 2. We define a recursive function that takes the current range of inorder indices and the current root index in the preorder traversal.
// 3. The base case checks if the start index is greater than the end index; if so, we return nullptr.
// 4. We create a new TreeNode with the value from the preorder traversal at the current root index.
// 5. We find the index of this value in the inorder traversal using the hashmap.
// 6. We recursively build the left and right subtrees using the appropriate ranges of inorder indices and updated root indices from the preorder traversal.
// 7. Finally, we return the constructed tree's root node.