import java.util.Arrays;

/*
 * @lc app=leetcode id=349 lang=java
 *
 * [349] Intersection of Two Arrays
 */

// @lc code=start
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums1) {
            set.add(num);
        }
        System.out.println(set);
        // List<Integer> res = new ArrayList<>();
        Set<Integer> res = new HashSet<>();
        for (int num : nums2) {
            if (set.contains(num)) {
                res.add(num);
            }
        }
        return res.stream().mapToInt(i -> i).toArray();
    }
}
// @lc code=end

