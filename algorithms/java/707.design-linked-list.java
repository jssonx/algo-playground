/*
 * @lc app=leetcode id=707 lang=java
 *
 * [707] Design Linked List
 */

// @lc code=start

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}
// 链表的基本属性：长度和头
class MyLinkedList {
    int size = 0;
    ListNode dummy = null;

    public MyLinkedList() {
        size = 0;
        dummy = new ListNode();
    }
    
    public int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        ListNode cur = dummy;
        for (int i = 0; i <= index; i++) {
            cur = cur.next;
        }
        return cur.val;
    }
    
    public void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    public void addAtIndex(int index, int val) {
        if (index > size) {
            return;
        }
        if (index < 0) {
            index = 0;
        }
        ListNode newnode  = new ListNode(val);
        ListNode pre = dummy;
        for (int i = 0; i < index; i++) {
            pre = pre.next;
        }
        newnode.next = pre.next;
        pre.next = newnode;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        ListNode pre = dummy;
        for (int i = 0; i < index; i++) {
            pre = pre.next;
        }
        pre.next = pre.next.next;
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */
// @lc code=end

