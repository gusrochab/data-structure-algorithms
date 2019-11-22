from nodes import Node
from tree import Tree

node0 = Node('apple')
node1 = Node('banana')
node2 = Node('orange')
node3 = Node('pineapple')
node4 = Node('grape')
node5 = Node('melon')

node0.set_left_node(node1)
node1.set_left_node(node2)
node0.set_right_node(node3)
node3.set_left_node(node4)
node3.set_right_node(node5)

tree = Tree(node0)
set = tree.dfs()
print(dfs)

