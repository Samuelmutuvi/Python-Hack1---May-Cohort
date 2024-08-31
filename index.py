def reverse_string(s: str) -> str:
    stack = []  # Initialize an empty stack
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    reversed_string = ""  # Initialize an empty string to store the reversed string
    # Pop all characters from the stack and append to the result string
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage:
# print(reverse_string("hello"))  # Output should be "olleh"


class QueueWithStacks:
    def __init__(self):
        self.stack1 = []  # Stack to handle enqueue operations
        self.stack2 = []  # Stack to handle dequeue operations

    def enqueue(self, x: int):
        self.stack1.append(x)  # Push element to stack1

    def dequeue(self) -> int:
        if not self.stack2:  # If stack2 is empty, transfer all elements from stack1
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:  # If stack2 is still empty, queue is empty
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()  # Pop from stack2, which represents the front of the queue

# Example usage:
q = QueueWithStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_max(self) -> int:
        if not self.head:
            raise ValueError("The list is empty")

        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        return max_value

# Example usage:
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
