// Problem 236 : Lowest common ancestor of a binary tree (Medium)

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