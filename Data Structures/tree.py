from nodes import Node

class Tree():
    def __init__(self, tree_nodes=None):
        self.root = tree_nodes[-1]
        self.tree_nodes = tree_nodes

    def get_root(self):
        return self.root

    def set_root(self,data):
        self.root.data = data

    def get_nodes_list(self):
        return self.tree_nodes

'''
    def __str__(self):
        def traverse(node):
            if node.has_left_child() and not node.get_visited_left():
                print(node)
                node.get_left_child().set_visited_left()
                traverse(node.get_left_child())
            if node.has_right_child() and not node.get_visited_right():
                print(node)
                node.r
'''

'''
    def __str__(self):

        nodes_list = []
        for node in self.tree_nodes:
            nodes_list.append(node)
            if node.has_left_child():
                nodes_list.append(node)
            else:
                nodes_list.append('<empty>')
            if node.has_right_child():
                nodes_list.append(node)
            else:
                nodes_list.append('<empty>')


        i = 0
        while True:
            j = i
            i += 1

'''