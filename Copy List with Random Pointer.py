"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None : None}
        temp = head
        while temp:
            hashmap[temp] = Node(temp.val)
            temp = temp.next

        temp = head
        while temp:
            hashmap[temp].next = hashmap[temp.next]
            hashmap[temp].random = hashmap[temp.random]
            temp = temp.next

        return hashmap[head]