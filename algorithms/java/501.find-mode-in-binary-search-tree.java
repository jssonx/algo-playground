/*
 * @lc app=leetcode id=501 lang=java
 *
 * [501] Find Mode in Binary Search Tree
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
    int cur_len = 0;
    int max_len = Integer.MIN_VALUE;
    TreeNode prev = null;
    ArrayList<Integer> resList = new ArrayList<>();;
    public int[] findMode(TreeNode root) {
        traverse(root);

        int[] res = new int[resList.size()];
        for (int i = 0; i < resList.size(); i++) {
            res[i] = resList.get(i);
        }
        return res;

    }
    private void traverse(TreeNode node) {
        if (node == null) {
            return;
        }
        traverse(node.left);
        if (prev == null || prev.val != node.val) {
            cur_len = 1;
        } else {
            cur_len++;
        }
        if (cur_len > max_len) {
            resList.clear();
            resList.add(node.val);
            max_len = cur_len;
        } else if (cur_len == max_len) {
            resList.add(node.val); 
        }
        prev = node;
        traverse(node.right);
    }
}
// @lc code=end

