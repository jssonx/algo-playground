/*
 * @lc app=leetcode id=112 lang=java
 *
 * [112] Path Sum
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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return traverse(root, targetSum);
    }
    private boolean traverse(TreeNode root, int targetSum) { 
        if (root == null) {
            return false;
        }
        if (root.left == null && root.right == null && root.val == targetSum) {
            return true;
        }
        if (root.left == null && root.right == null) {
            return false;
        }
        if (root.left != null) {
            if (traverse(root.left, targetSum - root.val)) {
                return true;
            }
        }
        if (root.right != null) {
            if (traverse(root.right, targetSum - root.val)) {
                return true;
            }
        }
        return false;
    }
}
// @lc code=end

