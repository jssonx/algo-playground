/*
 * @lc app=leetcode id=383 lang=java
 *
 * [383] Ransom Note
 */

// @lc code=start
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < magazine.length(); i++) {
            map.put(magazine.charAt(i), map.getOrDefault(magazine.charAt(i), 0) + 1);
        }
        for (char r : ransomNote.toCharArray()) {
            if (map.containsKey(r)) {
                if (map.get(r) > 0) {
                    map.put(r, map.get(r) - 1);
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }
}