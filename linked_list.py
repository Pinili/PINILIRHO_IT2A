
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        print(f"Inserted: {data}   (node = {self.size})")
        self.size += 1

    def delete_first(self):
        if self.head is None:
            return
        removed = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        print(f"Deleted: {removed}")
        self.size -= 1

name = input("Enter a word/last name: ").strip().upper()
linked_list = LinkedList()

print("\n--- INSERTING NODES ---")
for letter in name:
    linked_list.append(letter)

print("\n--- DELETING NODES ---")
while linked_list.head is not None:
    linked_list.delete_first()

print("\nLinked list is now empty.")
