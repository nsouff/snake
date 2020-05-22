class Node():
    def __init__(self, val, next=None, prev=None):
        self.item = val
        self.next = next
        self.prev = prev
class LinkedList():
    def __init__(self):
        self.first = None
        self.last = None

    def add_first(self, val):
        if self.first == None:
            self.first = self.last = Node(val)
        else:
            node = Node(val, self.first)
            self.first.prev = node
            self.first = node
    def add_last(self, val):
        if self.first = None:
            self.first = self.last = Node(val)
        else:
            node = Node(val, prev=self.last)
            self.last.next = node
            self.last = node
    def remove_first(self):
        if self.first != None:
            if self.first.next == None:
                self.first = self.last = None
            else:
                self.first = self.first.next
                self.first.prev = None
    def remove_last(self):
        if self.last != None:
            if self.last.prev == None:
                self.last = self.first = None
            else:
                self.last = self.last.prev
                self.last.next = None
