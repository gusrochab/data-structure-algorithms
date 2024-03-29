
# keeps the state of a node. If it has already visited left or right children
class State():
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False

    def get_node(self):
        return self.node


    def get_visited_left(self):
        return self.visited_left


    def get_visited_right(self):
        return self.visited_right


    def set_visited_left(self):
        self.visited_left = True


    def set_visited_right(self):
        self.visited_right = True


    def __repr__(self):
        s = f'''{self.node.get_value()}
visited left: {self.visited_left}
visited right: {self.visited_right}
    '''
        return s