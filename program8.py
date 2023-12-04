class Stack:
    def __init__ (self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return"None"
    def is_empty(self):
        return len(self.stack)==0
def reverse(sentence):
    words=sentence.split()
    stack=Stack()
    for word in words:
        stack.push(word)
    reversed_sentence=""
    while not stack.is_empty():
        reversed_sentence+=stack.pop()+" "
    return reversed_sentence.strip()
T = int(input())
test_cases=[input()for _ in range(T)]
for sentence in test_cases:
    reversed_sentence=reverse(sentence)
    print(reversed_sentence)
