"""
https://leetcode.com/problems/copy-list-with-random-pointer/

### 1. Question Explanation:
----------------------------
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
None of the pointers in the new list should point to nodes in the original list.
For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.

### 2. HashMap Based Solution:
----------------------------
Video link: https://youtu.be/HQbBCHoIIFU
1. Edge Case Handling:
    - If the input list is empty (head is None), return immediately.
2. First Pass: Creating Copy Nodes
    - Iterate through the original list.
    - For each node, create a new copy node.
    - Link the copy nodes together using the 'next' pointer.
    - Store a mapping of original nodes to their copies in a dictionary (original_to_copy).
3. Second Pass: Setting Random Pointers
   - Iterate through the original list again.
   - For each node, set the random pointer of its copy:
   - If the original node has a random pointer, find the corresponding copy node using the dictionary and set it as the random pointer of the current copy node.

### 3. Complexity Analysis:
----------------------------
Time: O(N)
Space: O(N)

"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]'):
        if not head: return
        original_to_copy = {} # HashMap
        cur_node, copy_prev = head, None

        # First Pass: Create cloned nodes with next pointer
        while cur_node:
            copy_node = Node(cur_node.val)
            if copy_prev: copy_prev.next = copy_node
            original_to_copy[cur_node] = copy_node
            copy_prev = copy_node
            cur_node = cur_node.next

        # Second Pass: Setting random Pointer
        cur_node = head
        while cur_node:
            copy_node = original_to_copy[cur_node]
            if cur_node.random:
                copy_node.random = original_to_copy[cur_node.random]
            cur_node = cur_node.next

        return original_to_copy[head]
        
