
from collections import deque

name = "PINILI"
queue = deque()

print("Enter a word/last name:", name)
print()

# ENQUEUE
for letter in name:
    queue.append(letter)
    rear = len(queue) - 1
    print(f"Enqueued: {letter}   (rear = {rear})")

print()

# DEQUEUE
front = 0

while queue:
    letter = queue.popleft()
    front += 1
    print(f"Dequeued: {letter}   (front = {front})")

print()
print("Queue is now empty.")
