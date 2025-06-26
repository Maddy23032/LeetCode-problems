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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head==null || left==right) return head;
        ListNode dummy=new ListNode(0);
        dummy.next=head;
        ListNode pre=dummy;
        for(int i=1;i<left;i++){
            pre=pre.next;
        }
        ListNode st=pre.next;
        ListNode th=st.next;
        for(int i=0;i<right-left;i++){
            st.next=th.next;
            th.next=pre.next;
            pre.next=th;
            th=st.next;
        }
        return dummy.next;
    }
}