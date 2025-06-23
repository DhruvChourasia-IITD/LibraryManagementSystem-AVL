class BookNode:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, book_id, title):
        if not root:
            return BookNode(book_id, title)
        elif book_id < root.book_id:
            root.left = self.insert(root.left, book_id, title)
        elif book_id > root.book_id:
            root.right = self.insert(root.right, book_id, title)
        else:
            return root  # Duplicate IDs not allowed

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance = self.get_balance(root)

        # Perform rotations if unbalanced
        if balance > 1 and book_id < root.left.book_id:
            return self.right_rotate(root)
        if balance < -1 and book_id > root.right.book_id:
            return self.left_rotate(root)
        if balance > 1 and book_id > root.left.book_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and book_id < root.right.book_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, book_id):
        if not root or root.book_id == book_id:
            return root
        elif book_id < root.book_id:
            return self.search(root.left, book_id)
        else:
            return self.search(root.right, book_id)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"{root.book_id} - {root.title}")
            self.inorder(root.right)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y
