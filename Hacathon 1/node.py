class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value: int):
        # Create a new node
        new_node = Node(value)
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
        
      
        max_value = self.head.value
        current = self.head
        
        # Traverse the list to find the maximum value
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        
        return max_value

# Example usage
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)
print(ll.find_max())  # Output: 4
