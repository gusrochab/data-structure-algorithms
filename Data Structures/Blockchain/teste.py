from linked_list import Linked_list

linked_list_1 = Linked_list()
linked_list_2 = Linked_list()
linked_list_3 = Linked_list()
linked_list_4 = Linked_list()

elements_1 = [3,2,4,35,6,65,6,4,3,21]
elements_2 = [6,32,4,9,6,1,11,21,1]

for i in elements_1:
    linked_list_1.append(i)

for i in elements_2:
    linked_list_2.append(i)

print(linked_list_1.union(linked_list_2))
print(linked_list_1.intersection(linked_list_2))


elements_3 = [3,2,4,35,6,65,6,4,3,23]
elements_4 = [1,7,8,9,11,21,1]

for i in elements_3:
    linked_list_3.append(i)

for i in elements_4:
    linked_list_4.append(i)

print(linked_list_3.union(linked_list_4))
print(linked_list_3.intersection(linked_list_4))
