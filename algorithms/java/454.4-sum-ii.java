/*
 * @lc app=leetcode id=454 lang=java
 *
 * [454] 4Sum II
 */

// @lc code=start
class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Map<Integer, Integer> map = new HashMap<>();
        int tmp;
        int res = 0;
        for (int i : nums1) {
            for (int j : nums2) {
                tmp = i + j;
                if (map.containsKey(tmp)) {
                    map.put(tmp, map.get(tmp) + 1);
                } else {
                    map.put(tmp, 1);
                }
            }
        }
        for (int i : nums3) {
            for (int j : nums4) {
                tmp = i + j;
                if (map.containsKey(0 - tmp)) {
                    res += map.get(0 - tmp);
                }
            }
        }
        return res;
    }
}
// @lc code=end

