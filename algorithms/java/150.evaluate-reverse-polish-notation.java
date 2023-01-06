/*
 * @lc app=leetcode id=150 lang=java
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
class Solution {
    public int evalRPN(String[] tokens) {
        int a, b;
        Stack<Integer> stk = new Stack<>();
        for (String t: tokens) { 
            if (t.equals("+")) {
                stk.push(stk.pop() + stk.pop());
            } else if (t.equals("-")) {
                a = stk.pop();
                b = stk.pop();
                stk.push(b - a);
            } else if (t.equals("*")) {
                stk.push(stk.pop() * stk.pop());
            } else if (t.equals("/")) {
                a = stk.pop();
                b = stk.pop();
                stk.push(b / a);
            } else {
                stk.push(Integer.parseInt(t));
            }
        }
        return stk.pop();
    }
}
// @lc code=end

