/*
 * @lc app=leetcode id=704 lang=java
 *
 * [704] Binary Search
 */

// @lc code=start
class Solution {
    public int search(int[] nums, int target) {
        int left = -1;
        int right = nums.length; 
        while (left + 1 != right) {
            int mid = left + (right - left) / 2;
            if (target <= nums[mid]) {
                right = mid;
            } else if (target > nums[mid]) {
                left = mid;
            }
        }
        if (right < nums.length && right > -1 && nums[right] == target) {
            return right;
        } else {
            return -1;
        }
    }
}
// @lc code=end

