/*
 * @lc app=leetcode id=202 lang=java
 *
 * [202] Happy Number
 */

// @lc code=start
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> hash = new HashSet<>();
        while (n != 1 && !hash.contains(n)) {
            hash.add(n);
            n = updateN(n);
        }
        return n == 1;
    }
    private int updateN(int n) {
        int res = 0;
        while (n > 0) {
            int digit = n % 10;
            res += digit * digit;
            n /= 10;
        } 
        return res;
    }
}
// @lc code=end

