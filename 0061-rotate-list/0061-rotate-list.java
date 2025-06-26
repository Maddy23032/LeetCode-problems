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
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || k==0) return head;
        ListNode temp=head;
        int len=1;
        while(temp.next!=null){
            temp=temp.next;
            len++;
        }
        if(k%len==0) return head;
        k=k%len;
        temp.next=head;
        ListNode nln=findnth(head,len-k);
        head=nln.next;
        nln.next=null;
        return head;

    }
    private ListNode findnth(ListNode temp,int k){
        int cnt=1;
        while(temp!=null){
            if(cnt==k) return temp;
            temp=temp.next;
            cnt++;
        }
        return temp;
    }
}