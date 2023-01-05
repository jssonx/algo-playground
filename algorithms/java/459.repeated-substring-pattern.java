/*
 * @lc app=leetcode id=459 lang=java
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start
class Solution {
    public boolean repeatedSubstringPattern(String s) {
        int slen = s.length();
        int[] next = new int[slen];
        getNext(next, s);
        // System.out.println(Arrays.toString(next));
        int last = next.length - 1;
        int small = slen - next[last];
        int tmp = slen % small;
        if (next[last] != 0 && tmp == 0) {
            return true;
        } else {
            return false;
        }
    }
    private void getNext(int[] next, String s) {
        int j = 0;
        next[0] = 0;
        for (int i = 1; i < s.length(); i++) {
            while (j != 0 && s.charAt(j) != s.charAt(i)) 
                j = next[j - 1];
            if (s.charAt(j) == s.charAt(i)) 
                j++;
            next[i] = j; 
        }
    }
}
// @lc code=end

