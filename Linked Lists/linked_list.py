from nodes import Node

class Linked_list():
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)

    def prepend(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_head = Node(data)
            new_head.next = self.head
            self.head = new_head

    def delete(self, data):
        if self.head == None:
            return

        current = self.head
        if self.head.data == data:
            self.head = self.head.next
            return

        else:
            while current.next.data != data:
                current = current.next
            current.next = current.next.next
            return

    def __getitem__(self, item):
        current = self.head
        while item > 0:
            current = current.next
            item -= 1
        return current

    def __str__(self):
        current = self.head
        s = ''
        while current:
            s =  s + f'({current.data})-'
            current = current.next
        s = s[:-1]
        return s