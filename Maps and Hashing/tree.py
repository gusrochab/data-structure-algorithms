
class Tree():

    def __init__(self, node):
        self.root = node
        self.visit_order = []
        self.stack = []
        self.deque = []

    #return the root of the tree
    def get_root(self):
        return self.root

    #add nodes to the tree for binary search
    def add_node(self, node):
        compare_node = self.get_root()
        while True:
            if int(node.get_value()) < int(compare_node.get_value()):
                if compare_node.has_left_child():
                    compare_node = compare_node.left_node
                else:
                    compare_node.left_node = node
                    break
            elif int(node.get_value()) > int(compare_node.get_value()):
                if compare_node.has_right_child():
                    compare_node = compare_node.right_node
                else:
                    compare_node.right_node = node
                    break

    #The same as 'add_node' function, but using recursive function
    def recursive_add_node(self, node):
        def add(compare_node):
            if int(node.get_value()) < int(compare_node.get_value()):
                if compare_node.has_left_child():
                    add(compare_node.left_node)
                else:
                    compare_node.left_node = node
            elif int(node.get_value()) > int(compare_node.get_value()):
                if compare_node.has_right_child():
                    add(compare_node.right_node)
                else:
                    compare_node.right_node = node
        add(self.get_root())


    #traverse the tree with a depth first search algorithm showing the nodes in a pre order way
    def dfs(self):
        node = self.get_root()
        self.stack.append(node)
        self.visit_order.append(node.value)
        while True:
            #check if the node has a left child and visit the node
            if node.has_left_child() and not node.get_visited_left():
                node.visited_left = True
                node = node.get_left_node()
                self.stack.append(node)
                self.visit_order.append(node.value)
            #check if the node has a right child and visit the node
            elif node.has_right_child() and not node.get_visited_right():
                node.visited_right = True
                node = node.get_right_node()
                self.stack.append(node)
                self.visit_order.append(node.value)
            #if the node doesn't have any child
            else:
                self.stack.pop()
                if len(self.stack) > 0:
                    node = self.stack[-1]
                else:
                    return self.visit_order


    #traverse the tree with a breath first search algorithm
    def bfs(self):
        node = self.get_root()
        self.deque.append(node)
        while True:
            if len(self.deque) > 0:
                node = self.deque.pop()
                self.visit_order.append(node.get_value())
                if node.has_left_child():
                    self.deque.insert(0, node.left_node)
                if node.has_right_child():
                    self.deque.insert(0, node.right_node)
            else:
                return self.visit_order


    def pritn_tree(self):
        

