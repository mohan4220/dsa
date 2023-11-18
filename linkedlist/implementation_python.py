class Node:
    data = None
    next = None

    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    head = None
    tail = None

    def print(self):
        current = self.head
        while not current == None:
            print(current.data)
            current = current.next

    def insert(self, data):
        current = self.head
        if current == None:
            self.head = Node(data)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(data)

    def __len__(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def insert_at_start(self, data):
        self.head = Node(data, self.head)

    def insert_at_index(self, data, index):
        current = self.head
        if index == 0:
            self.insert_at_start(data)
        elif index > self.__len__():
            self.insert(data)
        else:
            count = 0
            next_ptr = None
            while count < index - 1:
                current = current.next
                count += 1
            next_ptr = current.next
            print("--", current.data)
            print("==", next_ptr)
            current.next = Node(data, next_ptr)

    def find(self, value):
        pass

    def find_all(self, value):
        pass

    def update(self, value, index):
        pass

    def delete(self, value):
        pass

    def delete_at(self, index):
        pass


if __name__ == "__main__":
    linklist = LinkedList()
    linklist.insert(5)
    linklist.insert(4)
    linklist.insert(3)
    linklist.insert(2)
    linklist.insert(1)
    linklist.insert_at_start(44)
    linklist.insert_at_index(45, 8)
    linklist.print()
    print("length", len(linklist))

    print("\ndone")
