#### Task 1. Implement a Ring Buffer Data Structure
"""
A ring buffer is a non-growable buffer with a fixed size.
When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.
This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a
certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

Implement this behavior in the RingBuffer class.
RingBuffer has two methods, `append` and `get`.
The `append` method adds the given element to the buffer.
The `get` method returns all of the elements in the buffer in a list in their given order.
It should not return any `None` values in the list even if they are present in the ring buffer.

For example:

```python
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']

"""
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    def __str__(self):
        print(f'{self.value}, {self.prev}, {self.next}')
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            old_node = self.tail
            self.tail = new_node
            old_node.next = new_node
            new_node.prev = old_node


    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.head is None and self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return None
        self.delete(node)
        self.add_to_head(node.value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return None
        self.delete(node)
        self.add_to_tail(node.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value




class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = DoublyLinkedList()
        self.current = None


    def append(self, item):
        if len(self.buffer) == self.capacity:
            self.current.value = item
            if self.current.next is None:
                while self.current.prev is not None:
                    self.current = self.current.prev
            else:
                self.current = self.current.next
        if len(self.buffer) < self.capacity:
            self.buffer.add_to_tail(item)
            self.current = self.buffer.head


    def get(self):
        buffer_list = []
        current_node= self.buffer.head
        while buffer_list is not None and current_node.next is not None:
            buffer_list.append(current_node.value)
            current_node = current_node.next
        if current_node:
            buffer_list.append(current_node.value)
        return buffer_list
