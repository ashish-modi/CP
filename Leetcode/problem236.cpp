// Problem 236 : Lowest common ancestor of a binary tree
// Difficulty: Medium
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    struct LCAresult{
        bool foundP;
        bool foundQ;
        TreeNode* result;

        };
    LCAresult lca(TreeNode* root, TreeNode* p, TreeNode* q){
        bool p_bool = false, q_bool = false;
        if(root == nullptr){
            return {false, false, root};
        }
        if(root->val == p->val)
            p_bool = true;
        if(root->val == q->val)
            q_bool = true;
        LCAresult left = lca(root->left, p, q);
        if(left.result != nullptr)
            return left;
        p_bool = left.foundP || p_bool;
        q_bool = left.foundQ || q_bool;
        if(p_bool == true && q_bool == true)
            return {true, true, root};
        
        LCAresult right = lca(root->right, p, q);
        if(right.result != nullptr)
            return right;
        p_bool = right.foundP || p_bool;
        q_bool = right.foundQ || q_bool;
        if(p_bool == true && q_bool == true)
            return {true, true, root};
        
        return {p_bool, q_bool, nullptr};
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        LCAresult res = lca(root, p, q);
        return res.result;
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack).
// Explanation:
// 1. We define a helper struct `LCAresult` to store whether we have found nodes p and q, and the result node if found.
// 2. We define a recursive function `lca` that traverses the binary tree.
// 3. The base case checks if the current node is null; if so, we return false for both p and q found, and null for the result.
// 4. We check if the current node matches either p or q and update the corresponding boolean flags.
// 5. We recursively call `lca` on the left and right subtrees.
// 6. If either subtree returns a non-null result, we propagate that result up the recursion stack.
// 7. We update the boolean flags for p and q found based on the results from the left and right subtrees.
// 8. If both p and q are found at the current node, we return the current node as the result.
// 9. Finally, we return the result from the main function `lowestCommonAncestor`.