from collections import Counter
from nodes import Node
from tree import Tree

a_great_sentence = 'The bird is the word'

frequency = Counter(a_great_sentence)
frequency_list = []
for letter, freq in frequency.items():
    frequency_list.append((freq, letter))
frequency_list.sort()
#print(frequency_list)

nodes_list = []
for node in frequency_list:
    nodes_list.append(Node(frequency=node[0], letter=node[1]))
nodes_list.sort()
#print(nodes_list)

def make_tree(nodes_list):
    while len(nodes_list) != 1:
        nodes_list.sort()
        #print(nodes_list)
        frequency = nodes_list[0].frequency + nodes_list[1].frequency
        letter = nodes_list[0].letter + nodes_list[1].letter
        left_child = nodes_list.pop(0)
        right_child = nodes_list.pop(0)
        new_node = Node(frequency, left_child, right_child, letter)
        nodes_list.insert(0, new_node)
    return nodes_list[0]

root_node = make_tree(nodes_list)
tree = Tree(root_node)
#print(tree.set_tree())
freq, letter = tree.set_tree()
#print(freq)
#print(letter)
fl_list = []
for f, l in zip(freq, letter):
    fl_list.append((f, l))
print(fl_list)




