/*
 * @lc app=leetcode id=654 lang=java
 *
 * [654] Maximum Binary Tree
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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if (nums == null || nums.length == 0) {
            return null;
        }
        return construct(nums, 0, nums.length);
    }
    private TreeNode construct(int[] nums, int start, int end) {
        if (start + 1 > end) {
            return null;
        }
        if (start + 1 == end) {
            return new TreeNode(nums[start]);
        }
        int maxIdx = getMaxIdx(nums, start, end);
        TreeNode root = new TreeNode(nums[maxIdx]);
        root.left = construct(nums, start, maxIdx);
        root.right = construct(nums, maxIdx + 1, end);
        return root;
    }
    private int getMaxIdx(int[] nums, int start, int end) {
        int maxIdx = start;
        for (int i = start; i < end; i++) {
            if (nums[i] > nums[maxIdx]) {
                maxIdx = i;
            }
        }
        return maxIdx;
    }
}
// @lc code=end