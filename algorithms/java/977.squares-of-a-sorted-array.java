/*
 * @lc app=leetcode id=977 lang=java
 *
 * [977] Squares of a Sorted Array
 */

// @lc code=start
class Solution {
    public int[] sortedSquares(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int[] res = new int[nums.length];
        int index = nums.length - 1;
        while (left <= right) {
            int ls = nums[left] * nums[left];
            int rs = nums[right] * nums[right];
            if (ls > rs) {
                res[index] = ls;
                index--;
                left++;
            } else {
                res[index] = rs;
                index--;
                right--;
            }
        }
        return res;
    }
}
// @lc code=end

