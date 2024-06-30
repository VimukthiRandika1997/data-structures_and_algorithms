from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(head: Optional[ListNode]) -> bool:
    # two pointer method: fast and slow
    # slow increases by one step, while fast is by two steps
    # at some point in time, if there is cycle they should meet
    # as fast pointer chases slow pointer from back

    fast, slow = head, head

    while fast and fast.next:
        # increment fast pointer by two steps
        fast = fast.next.next
        # increment slow pointer by one step
        slow = slow.next

        # check if two pointers meet each other
        if fast == slow: return True
    return False

'''

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

# --Example 01:

head = [3, 2, 0, -4], pos = 1
3 -> 2 -> 0 -> -4
     |__________|
    
There is a cycle in the linked list, where the tail connects to 1st node(0-index)


# -- Example 02:

head = [1], pos = -1
1 -> null

There is no cycle in the linked list.

'''

### -- C++ -- ###

'''

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* fast = head;
        ListNode* slow = head;

        while (fast != nullptr and fast->next != nullptr)
        {
            fast = fast->next->next;
            slow = slow->next;

            if (fast == slow)
                return true;
        }
        return false;
    }
};

'''


### -- Java -- ###

'''

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow)
                return true;
        }
        return false;
    }
}

'''