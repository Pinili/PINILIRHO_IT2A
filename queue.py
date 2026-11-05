

from collections import deque

name = input("Enter a word/last name: ").strip().upper()
queue = deque()

print("\n--- ENQUEUE ---")
for letter in name:
    queue.append(letter)
    rear = len(queue) - 1
    print(f"Enqueued: {letter}   (rear = {rear})")

print("\n--- DEQUEUE ---")
front = 0
while queue:
    letter = queue.popleft()
    front += 1
    print(f"Dequeued: {letter}   (front = {front})")

print("\nQueue is now empty.")
