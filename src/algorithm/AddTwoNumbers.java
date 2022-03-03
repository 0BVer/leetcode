package algorithm;

import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode firstNode;
        ListNode preNode = firstNode = new ListNode(l1.val + l2.val);
        while (true) {
            int temp = cut10(preNode);
            ListNode listNode = new ListNode(temp);
            int error = 0;
            if (l1.next != null) {
                listNode.val += l1.next.val;
                l1 = l1.next;
            } else {
                error++;
            }
            if (l2.next != null) {
                listNode.val += l2.next.val;
                l2 = l2.next;
            } else {
                error++;
            }

            if (error > 1) {
                if (listNode.val > 0)
                    preNode.next = listNode;
                break;
            } else {
                preNode.next = listNode;
                preNode = preNode.next;
            }
        }

        return firstNode;
    }

    int cut10(ListNode node) {
        if (node.val > 9) {
            node.val = node.val % 10;
            return 1;
        }
        return 0;
    }
}