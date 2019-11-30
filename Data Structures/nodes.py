class Node():
    def __init__(self, frequency=None, letter=None, left_child=None, right_child=None):
        self.frequency = frequency
        self.letter = letter
        self.left_child = left_child
        self.right_child = right_child
        self.binary_code = ''
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

    def get_left_child(self):
        return self.left_child

    def set_left_child(self, node):
        self.left_child = node

    def get_right_child(self):
        return self.right_child

    def set_right_child(self, node):
        self.right_child = node

    def has_left_child(self):
        return bool(self.left_child)

    def has_right_child(self):
        return bool(self.right_child)

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True

    def set_binary_code(self, parent_code, letter):
        self.binary_code = parent_code +  letter

    def get_binary_code(self):
        return self.binary_code



    def __repr__(self):
        return f'Node({self.get_letter()}, {self.get_frequency()}, {self.get_binary_code()})'

    def __str__(self):
        return f'Node({self.get_letter()}, {self.get_frequency()} ,{self.get_binary_code()})'

    def __len__(self):
        return self.get_frequency()

    def __gt__(self, other):
        if self.frequency > other.frequency:
            return True
