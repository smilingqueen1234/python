class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return"Empty"
    def is_empty(self):
        return len(self.stack)==0
def perform_operations(operations):
    stack=Stack()
    results=[]
    for operation in operations:
        if operation[0]=="push":
            stack.push(int(operation[1]))
        elif operation[0]=="pop":
            results.append(stack.pop())
    return results
T = int(input())
operations=[input().split() for _ in range(T)]
output = perform_operations(operations)
for result in output:
    print(result)
