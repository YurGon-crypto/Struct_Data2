from Task1 import UnsortedList


class QueueUsingLinkedList:
    def __init__(self):
        self.items = UnsortedList()

    def is_empty(self):
        return self.items.is_empty()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        else:
            return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("front from an empty queue")
        else:
            return self.items.display()[0]


# Example of usage:
if __name__ == "__main__":
    queue = QueueUsingLinkedList()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Original Queue:", queue.items.display())
    print("Front:", queue.front())

    dequeued_item = queue.dequeue()
    print(f"Dequeued item: {dequeued_item}")
    print("Queue after dequeue:", queue.items.display())
