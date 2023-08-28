from collections import deque


class Node:
    def __init__(self, key):
        # Initialize all attributes to null and color of node to Red
        self.value = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RBTree:
    def __init__(self):
        self.root = None

    def insert_node(self, key):

        if self.root is None:
            self.root = Node(key)
            self.root.color = 0
            # print("Size: " + str(self.size()))
            # print("Height: " + str(self.height()))
            return

        node = Node(key)

        self.where_to_insert(node, self.root)

        self.fix_insert(node)

        # print("Size: " + str(self.size()))
        # print("Height: " + str(self.height()))

    @staticmethod
    def get_uncle(node: Node):
        if node.parent is None:
            return None

        grandparent = node.parent.parent
        if grandparent is None:
            return None

        if grandparent.right == node.parent:
            return grandparent.left
        else:
            return grandparent.right

    @staticmethod
    def is_black(node: Node):
        if node is None:
            return True
        return node.color == 0

    def fix_insert(self, node: Node):
        # if node is root then change colour to black
        if node.parent is None:
            node.color = 0
            return

        # if root of Red Black Tree is Black continue / if not, change it to Black
        if RBTree.is_black(node.parent):
            return

        uncle = RBTree.get_uncle(node)

        # if Uncle is Red, change color of uncle and parent to Black and color of grandparent to Red and make the grandparent x
        if not RBTree.is_black(uncle):
            node.parent.color = 0
            uncle.color = 0
            node.parent.parent.color = 1
            self.fix_insert(node.parent.parent)
            return

        parent = node.parent
        grandparent = node.parent.parent

        # Case Left Left
        if parent == grandparent.left and node == parent.left:
            parent.color = 0
            grandparent.color = 1
            self.rotate_right(grandparent)
        # Case Left Right
        elif parent == grandparent.left and node == parent.right:
            self.rotate_left(parent)
            node.color = 0
            grandparent.color = 1
            self.rotate_right(grandparent)
        # Case Right Right
        elif parent == grandparent.right and node == parent.right:
            parent.color = 0
            grandparent.color = 1
            self.rotate_left(grandparent)
        # Case Right Left
        elif parent == grandparent.right and node == parent.left:
            self.rotate_right(parent)
            node.color = 0
            grandparent.color = 1
            self.rotate_left(grandparent)

    def rotate_left(self, node: Node):
        if node.right is None:
            return

        temp = node.right
        node.right = temp.left
        if temp.left is not None:
            temp.left.parent = node

        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.left:
            node.parent.left = temp
        else:
            node.parent.right = temp
        temp.left = node
        node.parent = temp

    def rotate_right(self, node: Node):
        if node.left is None:
            return

        temp = node.left
        node.left = temp.right
        if temp.right is not None:
            temp.right.parent = node

        temp.parent = node.parent
        if node.parent is None:
            self.root = temp
        elif node == node.parent.right:
            node.parent.right = temp
        else:
            node.parent.left = temp
        temp.right = node
        node.parent = temp

    @staticmethod
    def where_to_insert(node, parent: Node):
        while True:
            node.parent = parent
            if node.value > parent.value:
                if parent.right is None:
                    parent.right = node
                    return node
                parent = parent.right
            else:
                if parent.left is None:
                    parent.left = node
                    return node
                parent = parent.left

    def search(self, key):
        node = self.root
        while node is not None:
            if node.value == key:
                return node
            elif node.value < key:
                node = node.right
            else:
                node = node.left

        return None

    def height(self) -> int:
        node = self.root
        if node is None:
            return 0

        queue = deque()      #to make it from one side
        queue.append(node)
        height = 0

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current_node = queue.popleft()

                if current_node.left is not None:
                    queue.append(current_node.left)

                if current_node.right is not None:
                    queue.append(current_node.right)

            height += 1

        return height

    def size(self):
        node = self.root

        if node is None:
            return 0
        stack = [node]
        size = 0
        while stack:
            curr = stack.pop()
            size += 1
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return size

    def print_root(self):
        print("\nValue of Root is " + str(self.root.value)+"\n")


# MAIN FUNCTION

tree = RBTree()

f = open(r"C:\Users\samah\OneDrive\Desktop\lab2.txt")
for line in f:
    tree.insert_node(line.strip())
f.close()

x = 1
while x == 1:
    print("1 to print Size and Height\n2 to insert a word\n3 to look for a word\n4 to print the root\n5 to quit")
    value = input("Choose a number: ")
    if value == '1':
        print("\nBefore Insertion: ")
        print("Size: " + str(tree.size()))
        print("Height: " + str(tree.height())+"\n")
    elif value == '2':
        val = input("Enter the word you want to insert: ")
        print(val)
        if tree.search(val) is not None:
            print("\nERROR: Word already in the dictionary!\n")
        else:
            tree.insert_node(val)
            # f = open(r"C:\Users\LENOVO\Desktop\dictionary.txt",'a')
            # f.write(val)
            # f.write('\n')
            # f.close()
            print("\nWord inserted in dictionary successfully!\n")
            print("\nAfter Insertion: ")
            print("Size: " + str(tree.size()))
            print("Height: " + str(tree.height())+"\n")
    elif value == '3':
        lookfor = input("Enter the word you want to look for: ")
        print(lookfor)

        if tree.search(lookfor) is not None:
            print("\nYES THE WORD WAS FOUND !!!\n")
        else:
            print("\nNO THE WORD WAS NOT FOUND :( \n")
    elif value == '4':
        tree.print_root()
    elif value == '5':
        x = 0

# tree.insertNode(5)
# tree.insertNode(6)
# tree.insertNode(7)
# tree.insertNode(8)
# tree.insertNode(9)
