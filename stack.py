# Assessment 3.2 - Stack (LIFO)
# Last name: PINILI

name = input("Enter a word/last name: ").strip().upper()
stack = []

print("\n--- PUSHING LETTERS ---")
for letter in name:
    stack.append(letter)
    print(f"Pushed: {letter}   (top = {len(stack) - 1})")

print("\n--- POPPING LETTERS ---")
while stack:
    removed = stack.pop()
    print(f"Popped: {removed}   (top = {len(stack) - 1})")

print("\nStack is now empty.")
