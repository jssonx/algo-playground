/*
 * @lc app=leetcode id=24 lang=java
 *
 * [24] Swap Nodes in Pairs
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode dummy = new ListNode(-1, head);
        ListNode prev = dummy;
        ListNode cur = head;
        while (prev.next != null && prev.next.next != null) {
            ListNode tmp = cur.next.next;
            prev.next = cur.next;
            cur.next.next = cur;
            cur.next = tmp;
            prev = cur;
            cur = cur.next;
        }
        return dummy.next;
    }
}
// @lc code=end

