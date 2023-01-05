/*
 * @lc app=leetcode id=1002 lang=java
 *
 * [1002] Find Common Characters
 */

// @lc code=start
class Solution {
    public List<String> commonChars(String[] words) {
        List<String> res = new ArrayList<>();
        if (words.length == 0) {
            return res;
        }
        int[] hash = new int[26];
        for (int i = 0; i < words[0].length(); i++) {
            hash[words[0].charAt(i) - 'a'] += 1;
        }
        // System.out.println(Arrays.toString(hash));
        for (int i = 1; i < words.length; i++) {
            int[] otherHash = new int[26];
            for (int j = 0; j < words[i].length(); j++) {
                otherHash[words[i].charAt(j) - 'a'] += 1;
            }
            for (int k = 0; k < 26; k++) {
                hash[k]  = Math.min(otherHash[k], hash[k]);
            }
        }
        for (int i = 0; i < 26; i++) {
            while (hash[i] != 0) {
                char c = (char) (i + 'a');
                res.add(String.valueOf(c));
                hash[i]--;
            }
        }
        return res;
    }
}
// @lc code=end



