import java.util.Map;

/*
 * @lc app=leetcode id=266 lang=java
 *
 * [266] Palindrome Permutation
 */

// @lc code=start
class Solution {
    public boolean canPermutePalindrome(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        }
        int cnt = 0;
        for (char key: map.keySet()) {
            if (map.get(key) % 2 != 0) {
                cnt++;
                if (cnt > 1) {
                    return false;
                }
            }
        }
        return true;
    }
}
// @lc code=end