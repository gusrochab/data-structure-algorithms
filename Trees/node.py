
class Node():
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


    def get_value(self):
        return self.value


    def set_value(self, value):
        self.value = value


    def set_left_child(self, node):
        self.left_child = node


    def get_left_child(self):
        return self.left_child


    def set_right_child(self, node):
        self.right_child = node


    def get_right_child(self):
        return self.right_child


    def has_left_child(self):
        return bool(self.left_child)


    def has_right_child(self):
        return bool(self.right_child)


    def __repr__(self):
        return f'Ndde{self.get_value()}'


    def __str__(self):
        return f'Node{self.get_value()}'

