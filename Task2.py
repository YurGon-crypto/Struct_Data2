from Task1 import UnsortedList


class StackUsingLinkedList:
    def __init__(self):
        self.items = UnsortedList()

    def is_empty(self):
        return self.items.is_empty()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        else:
            return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        else:
            return self.items.display()[-1]


if __name__ == "__main__":
    stack = StackUsingLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Original Stack:", stack.items.display())
    print("Peek:", stack.peek())

    popped_item = stack.pop()
    print(f"Popped item: {popped_item}")
    print("Stack after pop:", stack.items.display())
