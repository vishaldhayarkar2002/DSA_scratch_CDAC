class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    current = head
    
    while current:
        # Save the next node before we change current.next
        next_temp = current.next
        
        # Reverse the current node's pointer
        current.next = prev
        
        # Move prev and current one step forward
        prev = current
        current = next_temp
    
    # At the end, prev will be pointing to the new head
    return prev
