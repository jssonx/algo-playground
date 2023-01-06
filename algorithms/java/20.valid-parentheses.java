/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();
        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[' ) {
                stk.push(s.charAt(i));
                continue;
            } 
            if (stk.size() == 0 || map.get(stk.pop()) != s.charAt(i)) {
                return false;
            }
        }
        return stk.size() == 0;
    }
}
// @lc code=end

