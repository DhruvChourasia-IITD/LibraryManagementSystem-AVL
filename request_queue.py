class RequestQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, student_name, book_id):
        self.queue.append((student_name, book_id))

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def show_requests(self):
        for i, (student, book_id) in enumerate(self.queue, start=1):
            print(f"{i}. {student} requested Book ID {book_id}")
