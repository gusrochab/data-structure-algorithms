from collections import Counter
from nodes import Node
from tree import Tree

class Huffman_coding():

    def __init__(self):
        self.binary_code_list = []
        self.decoded_string = ''

    #retorna uma lista com tuplas contendo letra e frequencia da letra na string
    def get_letter_frequency(sellf, text):
        frequency_list = []
        frequency_dict = Counter(text)
        for letter, frequency in frequency_dict.items():
            frequency_list.append((frequency, letter))
        frequency_list.sort()
        return frequency_list

    def create_tree(self, frequency_list):
        node_list = []
        tree_nodes = []
        #cria a lista com os nós da base
        for node in frequency_list:
            frequency = node[0]
            letter = node[1]
            node_list.append(Node(frequency, letter))
        #junta os nós até o topo da árvore e armazena todos os nós na lista tree
        while len(node_list) > 1:
            node_list.sort()
            node1 = node_list.pop(0)
            node2 = node_list.pop(0)
            frequency = node1.get_frequency() + node2.get_frequency()
            letter = node1.get_letter() + node2.get_letter()
            #cria o novo nó a partir dos dois anteriores
            new_node = Node(frequency=frequency,letter=letter, left_child=node1, right_child=node2)
            node_list.append(new_node)
            tree_nodes.append(node1)
            tree_nodes.append(node2)
        root = node_list.pop(0)
        tree_nodes.append(root)
        #cria e retorna um objeto tipo árvore
        tree = Tree(tree_nodes=tree_nodes)
        return tree

    #cria uma lista de tuplas com letra e código binário
    def encode_string(self, tree, text):
        root = tree.get_root()
        text_binary_code = ''
        def traverse(node):
            if node.has_left_child() and not node.get_visited_left():
                node.left_child.set_binary_code(node.get_binary_code(), '0')
                node.set_visited_left()
                traverse(node.get_left_child())
            if node.has_right_child() and not node.get_visited_right():
                node.right_child.set_binary_code(node.get_binary_code(), '1')
                node.set_visited_right()
                traverse(node.get_right_child())
            self.binary_code_list.append((node.get_letter(), node.get_binary_code()))
        traverse(root)

        for char in text:
            for letter, binary in self.binary_code_list:
                if char == letter:
                    text_binary_code = text_binary_code + binary
        text_binary_code = text_binary_code + '0'
        return text_binary_code



    def decode_string(self, encoded_string, tree):
        root = tree.get_root()
        node = root
        i = 0
        while i < len(encoded_string):
            if encoded_string[i] == '0':
                if node.has_left_child():
                    node = node.get_left_child()
                    i += 1
                    continue
                else:
                    self.decoded_string = self.decoded_string + node.get_letter()
                    node = root
            if encoded_string[i] =='1':
                if node.has_right_child():
                    node = node.get_right_child()
                    i += 1
                    continue
                else:
                    self.decoded_string = self.decoded_string + node.get_letter()
                    node = root
        return self.decoded_string


huffman = Huffman_coding()
text = 'The bird is the word'
frequency = huffman.get_letter_frequency(text)
print(frequency)
tree = huffman.create_tree(frequency)
#print(tree)
encoded = huffman.encode_string(tree, text)
print(encoded)
decoded = huffman.decode_string(encoded, tree)
print(decoded)