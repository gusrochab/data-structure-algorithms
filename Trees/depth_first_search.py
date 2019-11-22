from state import State

class DFS():
    def __init__(self, tree):
        self.tree = tree
        self.visit_order = []
        self.stack = []
        self.root = tree.get_root()

    # traverse the tree using depth first search with 'pre order' method
    def pre_order(self):
        self.visit_order = []
        #State keeps de state of the node if it has already visited the left or the right child.
        #State also keeps a copy of the node
        state = State(self.root)
        #stack is used to keep track of the nodes. Used when need to go one node back on the tree
        self.stack.append(state)
        self.visit_order.append(self.root.get_value())
        while True:
            #check if the current node has a left child and it was not visited
            if node.has_left_child() and not state.get_visited_left():
                #change the state of visited_left to 'True' of the current node
                state.set_visited_left()
                node = node.left_child
                state = State(node)
                self.stack.append(state)
                self.visit_order.append(node.get_value())
            # check if the current node has a right child and it was not visited
            elif node.has_right_child() and not state.get_visited_right():
                #change the state of visited_right to 'True' of the current node
                state.set_visited_right()
                node = node.right_child
                state = State(node)
                self.stack.append(state)
                self.visit_order.append(node.get_value())
            else:
                #if the node doesn't have any child it is poped from the stack list
                self.stack.pop()
                if self.stack:
                    #the current node become the last node in stack list
                    state = self.stack[-1]
                    node = state.get_node()
                else:
                    return self.visit_order


    # traverse the tree using depth first search with 'pre order' method
    def recursive_pre_order(self):
        self.visit_order = []
        def traverse(node):
            if node:
                self.visit_order.append(node.get_value())
                traverse(node.get_left_child())
                traverse(node.get_right_child())

        traverse(self.root)
        return self.visit_order


    # traverse the tree using depth first search with 'in order' method
    def in_order(self):
        self.visit_order = []
        def traverse(node):
            if node:
                traverse(node.get_left_child())
                self.visit_order.append(node.get_value())
                traverse(node.get_right_child())
        traverse(self.root)
        return self.visit_order


    # traverse the tree using depth first search with 'post order' method
    def post_order(self):
        self.visit_order = []
        def traverse(node):
            if node:
                traverse(node.get_left_child())
                traverse(node.get_right_child())
                self.visit_order.append(node.get_value())
        traverse(self.root)
        return self.visit_order



