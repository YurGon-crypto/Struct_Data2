class UnsortedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def display(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.get_data())
            current = current.get_next()
        return result

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.get_data() == item:
                return index
            current = current.get_next()
            index += 1
        raise ValueError(f"{item} not found in the list")

    def pop(self, pos=None):
        if pos is None:
            if self.head is None:
                raise IndexError("pop from an empty list")
            else:
                popped_item = self.head.get_data()
                self.head = self.head.get_next()
                return popped_item
        else:
            if pos < 0:
                raise IndexError("pop index out of range")
            elif pos == 0:
                return self.pop()
            else:
                current = self.head
                previous = None
                count = 0
                while count < pos and current is not None:
                    previous = current
                    current = current.get_next()
                    count += 1
                if current is None:
                    raise IndexError("pop index out of range")
                else:
                    popped_item = current.get_data()
                    previous.set_next(current.get_next())
                    return popped_item

    def insert(self, pos, item):
        if pos < 0:
            raise IndexError("list index out of range")
        elif pos == 0:
            new_node = Node(item)
            new_node.set_next(self.head)
            self.head = new_node
        else:
            current = self.head
            previous = None
            count = 0
            while count < pos and current is not None:
                previous = current
                current = current.get_next()
                count += 1
            if count < pos:
                raise IndexError("list index out of range")
            else:
                new_node = Node(item)
                previous.set_next(new_node)
                new_node.set_next(current)

    def slice(self, start, stop):
        if start < 0 or stop < 0 or start >= stop:
            raise ValueError("Invalid start and stop indices")
        current = self.head
        count = 0
        result = UnsortedList()
        while count < stop and current is not None:
            if count >= start:
                result.append(current.get_data())
            current = current.get_next()
            count += 1
        return result.display()


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


# Example of usage:
if __name__ == "__main__":
    my_list = UnsortedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    print("Original List:", my_list.display())

    my_list.insert(1, 5)
    print("List after inserting 5 at index 1:", my_list.display())

    popped_item = my_list.pop()
    print(f"Popped item: {popped_item}")
    print("List after pop:", my_list.display())

    sliced_list = my_list.slice(1, 3)
    print("Sliced List:", sliced_list)
