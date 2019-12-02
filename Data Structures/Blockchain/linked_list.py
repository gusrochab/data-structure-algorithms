from node import Node

class Linked_list():
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        node  = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def size(self):
        if not self.head:
            return 0
        size = 0
        node = self.head
        while node:
            size +=1
            node = node.next
        return size

    # retorna a união de duas listas
    def union(self, other_list):
        union_list = Linked_list()
        node = self.head
        # adiciona os nós da primeira lista
        while node:
            union_list.append(node.value)
            node = node.next
        # adiciona os nós da segunda lista
        node = other_list.head
        while node:
            union_list.append(node.value)
            node = node.next

        return union_list

    #retorna a interseção de duas listas
    def intersection(self, other_list):
        intersection_list = Linked_list()
        other_node = other_list.head
        while other_node:
            node = self.head
            while node:
                if other_node.value == node.value:
                    intersection_list.append(other_node.value)
                    break
                node = node.next
            other_node = other_node.next

        return intersection_list

