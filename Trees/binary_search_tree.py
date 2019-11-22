from node import Node

class BST():
    def __init__(self, value):
        self.root = Node(value)
        self.node_found = None


    def get_root(self):
        return self.root


    # compare the insert value with the existing nodes value and insert a node with the value in the appropriate place
    def insert(self, value):
        node = self.get_root()
        while True:
            #goes to the left side child of the tree, if exists, else create a new left child
            if value < node.get_value():
                if node.has_left_child():
                    node = node.left_child
                else:
                    node.left_child = Node(value)
                    return
            # goes to the right side child of the tree, if exists, else create a new right child
            elif value > node.get_value():
                if node.has_right_child():
                    node = node.right_child
                else:
                    node.right_child = Node(value)
                    return


    # return a node of the tree that value matches with the insert value
    def recursive_search(self, value):
        def traverse(node):
                if node:
                    if node.get_value() == value:
                        self.node_found = node
                    if not self.node_found:
                        traverse(node.get_left_child())
                    if not self.node_found:
                        traverse(node.get_right_child())
                    return self.node_found
        return traverse(self.get_root())


    # return a node of the tree that value matches with the insert value
    def search(self, value):
        node = self.get_root()
        while True:
            if value == node.get_value():
                return node
            elif value < node.get_value():
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return None
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return None



