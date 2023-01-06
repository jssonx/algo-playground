/*
 * @lc app=leetcode id=239 lang=java
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        ArrayDeque<Integer> deque = new ArrayDeque<>(); 
        int n = nums.length;
        int[] res = new int[n - k + 1];
        int idx = 0;
        for(int right = 0; right < n; right++) {
            int left = right - k + 1;
            while(!deque.isEmpty() && deque.peek() < left){
                deque.pollFirst();
            }
            while(!deque.isEmpty() && nums[deque.peekLast()] < nums[right]) {
                deque.pollLast();
            }
            deque.offer(right);
            if(left >= 0){
                res[idx++] = nums[deque.peek()];
            }
        }
        return res;
    }
}
// @lc code=end

