class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        self.items.pop(0)
    def is_empty(self):
        if len(self.items) > 0:
            print("La cola no esta vacia")
        else:
            print("La cola esta vacia")
    def show_items(self):
        for i in range(len(self.items)):
            print(self.items[i])
    
queue_1 = Queue()
for i in range(1, 10):
    queue_1.enqueue(i)

print(queue_1.items)
queue_1.dequeue()
print(queue_1.items)
queue_1.show_items()