/*
 * @lc app=leetcode id=242 lang=java
 *
 * [242] Valid Anagram
 */

// @lc code=start
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int [] words = new int[26];
        for (int i = 0; i < s.length(); i++) {
            words[s.charAt(i) - 'a']++;
            words[t.charAt(i) - 'a']--;
        }
        // System.out.println(Arrays.toString(words));
        for (int i = 0; i < 26; i++) {
            if (words[i]!= 0) {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

