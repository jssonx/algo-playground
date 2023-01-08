/*
 * @lc app=leetcode id=530 lang=java
 *
 * [530] Minimum Absolute Difference in BST
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    TreeNode pre;
    int res = Integer.MAX_VALUE;
    public int getMinimumDifference(TreeNode root) {
        if(root == null) {
            return 0;
        }
        traverse(root);
        return res;
    }
    public void traverse(TreeNode root){
        if(root == null){
            return;
        }
        traverse(root.left);
        if(pre != null){
            res = Math.min(res, root.val - pre.val);
        }
        pre = root;
        traverse(root.right);
    }
}
// @lc code=end

