from linked_list import Linked_list

link_list1 = Linked_list()
link_list1.append(0)
link_list1.append(1)
link_list1.append(2)
link_list1.append(3)
link_list1.append(4)
link_list1.append(5)

item = link_list1[3]

print(item)
print(link_list1)

link_list1.delete(3)
print(link_list1)

link_list1.delete(0)
print(link_list1)

link_list1.append(6)
print(link_list1)

link_list1.prepend(0)
print(link_list1)
