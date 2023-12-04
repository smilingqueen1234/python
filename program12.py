class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Empty"
    def is_empty(self):
        return len(self.items) == 0
def process_queue_operations(operations):
    queue = Queue()
    result = []
    for operation in operations:
        if operation[0] == "e":
            queue.enqueue(int(operation[1]))
        elif operation[0] == "d":
             result.append(queue.dequeue())
    return result
T = int(input())
operations = [input().split() for _ in range(T)]
output = process_queue_operations(operations)
for item in output:
    print(item)
        