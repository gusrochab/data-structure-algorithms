
class BFS():
    def __init__(self, tree):
        self.tree = tree
        self.root = tree.get_root()
        self.visited_order = []
        self.queue = []
        self.print_list = []
        self.node_list = []


    # traverse the tree using breadth first search method
    def bfs(self):
        self.node_list.append(self.root)
        self.queue.insert(0, self.root)
        self.visited_order = []
        while self.queue:
            node = self.queue.pop()
            self.node_list.append(node)
            self.visited_order.append(node.get_value())
            if node.has_left_child():
                self.queue.insert(0, node.get_left_child())
            if node.has_right_child():
                self.queue.insert(0, node.get_right_child())
        return self.visited_order

    # prints the structure of the tree
    def print_bfs(self):
        #put the nodes values or empty values in a print list
        self.print_list = []
        self.queue.insert(0, self.root)
        self.print_list.append(self.root.get_value())
        while self.queue:
            node = self.queue.pop()
            if node.has_left_child():
                self.queue.insert(0, node.get_left_child())
                self.print_list.append(node.left_child.get_value())
            else:
                self.print_list.append('<empty>')
            if node.has_right_child():
                self.queue.insert(0, node.get_right_child())
                self.print_list.append(node.right_child.get_value())
            else:
                self.print_list.append('<empty>')

        #format the print list
        i = 0
        j = 0
        n = 0
        line = '| '
        while j < len(self.print_list):
            i = j
            j += 2 ** n
            for l in self.print_list[i:j]:
                line = line + str(l) + ' | '
            print(line)
            line = '| '
            n += 1
