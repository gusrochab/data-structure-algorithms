'''Create nodes that make up a tree'''
class Node():
    def __init__(self, frequency, left_child=None, right_child=None, letter = None):
        self.frequency = frequency
        self.letter = letter
        self.binary_code = None
        self.left_node = left_child
        self.right_node = right_child
        self.visited_left = False
        self.visited_right = False

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency

    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter

    def get_binary_code(self):
        return self.binary_code

    def set_binary_code(self, binary_code):
        self.binary_code = binary_code

    def get_left_node(self):
        return self.left_node

    def set_left_node(self, node):
        self.left_node = node

    def get_right_node(self):
        return self.right_node

    def set_right_node(self, node):
        self.right_node = node

    def has_left_child(self):
        return bool(self.left_node)

    def has_right_child(self):
        return bool(self.right_node)

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right


    def __repr__(self):
        return f'Node({self.get_letter()}: {self.get_frequency()})'

    def __str__(self):
        return f'Node({self.get_letter()}: {self.get_frequency()})'

    def __len__(self):
        return self.get_frequency()

    def __gt__(self, other):
        if self.frequency > other.frequency:
            return True
