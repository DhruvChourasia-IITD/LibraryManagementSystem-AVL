from avl import AVLTree, BookNode
from request_queue import RequestQueue
import json

def save_books_to_file(root, filename="books.json"):
    books = []

    def inorder_store(node):
        if node:
            inorder_store(node.left)
            books.append({"book_id": node.book_id, "title": node.title})
            inorder_store(node.right)

    inorder_store(root)

    with open(filename, "w") as f:
        json.dump(books, f)
    print(f"Saved {len(books)} books to {filename}")

def load_books_from_file(avl, filename="books.json"):
    root = None
    try:
        with open(filename, "r") as f:
            books = json.load(f)
            for book in books:
                root = avl.insert(root, book["book_id"], book["title"])
        print(f"Loaded {len(books)} books from {filename}")
    except FileNotFoundError:
        print(f"No existing book data found at {filename}, starting fresh.")
    return root

avl = AVLTree()
root = None
request_queue = RequestQueue()

# Sample data
root = load_books_from_file(avl)


while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Search Book")
    print("3. View All Books")
    print("4. Request Book")
    print("5. Process Request")
    print("6. View Pending Requests")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        bid = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        root = avl.insert(root, bid, title)
        print("Book added.")
        save_books_to_file(root)  # Save after insertion
    elif choice == '2':
        bid = int(input("Enter Book ID to search: "))
        result = avl.search(root, bid)
        if result:
            print(f"Found: {result.book_id} - {result.title}")
        else:
            print("Book not found.")
    elif choice == '3':
        print("\nAvailable Books (Inorder):")
        avl.inorder(root)
    elif choice == '4':
        student = input("Enter student name: ")
        bid = int(input("Enter Book ID to request: "))
        request_queue.enqueue(student, bid)
        print("Request added to queue.")
    elif choice == '5':
        req = request_queue.dequeue()
        if req:
            print(f"Processing request: {req[0]} gets Book ID {req[1]}")
        else:
            print("No pending requests.")
    elif choice == '6':
        print("Pending Requests:")
        request_queue.show_requests()
    elif choice == '0':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
