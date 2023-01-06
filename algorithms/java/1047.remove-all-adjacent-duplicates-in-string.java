import java.util.Deque;

/*
 * @lc app=leetcode id=1047 lang=java
 *
 * [1047] Remove All Adjacent Duplicates In String
 */

// @lc code=start
class Solution {
    public String removeDuplicates(String s) {
        Deque<Character> dq = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            if (!dq.isEmpty() && dq.peekLast() == c) {
                dq.pollLast();
            } else {
                dq.offer(c);
            }
         }
        StringBuilder sb = new StringBuilder();
        for (char c : dq) { 
            sb.append(c);
        }
        return sb.toString();
    }
}
// @lc code=end

