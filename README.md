# Library Management System (AVL Tree)

A command-line library management system implemented using a self-balancing AVL Tree and FIFO queue to handle book records and borrowing requests efficiently.

## Features
- Efficient book management with AVL Tree (O(log n) insert/search)
- Queue-based request management (FIFO)
- Persistent storage of book data using JSON
- Interactive console interface

## Files
- `avl.py`: AVL Tree implementation for book storage
- `request_queue.py`: FIFO queue for managing book requests
- `main.py`: Main program logic, user interface, file handling
- `books.json`: Stores book data persistently (auto-created)

## How to Run
1. Clone the repository
2. Run `main.py` using Python 3:
   ```bash
   python main.py
