/*
 * @lc app=leetcode id=513 lang=java
 *
 * [513] Find Bottom Left Tree Value
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
    public int findBottomLeftValue(TreeNode root) {
        int res = 0;
        Deque<TreeNode> dq = new ArrayDeque<>();
        if (root == null) {
            return res;
        }
        dq.add(root);
        while (!dq.isEmpty()) { 
            int size = dq.size();
            for (int i = 0; i < size; i++) {
                TreeNode cur = dq.pollFirst();
                if (i == 0) {
                    res = cur.val;
                }
                if (cur.left!= null) {
                    dq.add(cur.left);
                }
                if (cur.right != null) {
                    dq.add(cur.right); 
                }
            }
        }
        return res;
    }
}
// @lc code=end

/* class Solution {
    int res = 0;
    int max_depth = Integer.MIN_VALUE;
    public int findBottomLeftValue(TreeNode root) {
        traverse(root, 0);
        return res;
    }
    private void traverse(TreeNode root, int depth) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            if (depth > max_depth) {
                res = root.val;
                max_depth = depth;
            }
        }
        traverse(root.left, depth + 1);
        traverse(root.right, depth + 1);
    }
} */