from random import randrange
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, person):
        self.heap.append(person)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index]["priority"] < self.heap[parent_index]["priority"]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def insert_queue(self, queue):
        for person in queue:
            self.insert(person)

    def show(self):
        print(self.heap)

if __name__ == "__main__":
    queue = [
        {"priority": randrange(1, 10), "person": "Amanda"},
        {"priority": randrange(1, 10), "person": "Bruno"},
        {"priority": randrange(1, 10), "person": "Carlos"},
        {"priority": randrange(1, 10), "person": "Daniela"},
        {"priority": randrange(1, 10), "person": "Eduardo"},
        {"priority": randrange(1, 10), "person": "Fernanda"},
        {"priority": randrange(1, 10), "person": "Gabriel"},
        {"priority": randrange(1, 10), "person": "Helena"},
        {"priority": randrange(1, 10), "person": "Igor"},
        {"priority": randrange(1, 10), "person": "Juliana"},
        {"priority": randrange(1, 10), "person": "Kleber"},
        {"priority": randrange(1, 10), "person": "Larissa"},
        {"priority": randrange(1, 10), "person": "Marcelo"},
        {"priority": randrange(1, 10), "person": "Natália"},
        {"priority": randrange(1, 10), "person": "Otávio"},
        {"priority": randrange(1, 10), "person": "Patrícia"},
        {"priority": randrange(1, 10), "person": "Rafael"},
        {"priority": randrange(1, 10), "person": "Simone"},
        {"priority": randrange(1, 10), "person": "Tiago"},
        {"priority": randrange(1, 10), "person": "Vanessa"}
    ]

    heap = MinHeap()
    heap.insert_queue(queue)
    heap.show()
