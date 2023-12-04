class SinglyLinkedListNode:
    def __init__ (self,data):
        self.data = data
        self.next = None
def insertNodeAtTail(head,data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        head = new_node
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
    return head
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
n = 5
elements = [141,302,164,530,474]
head = None
for data in elements:
    head = insertNodeAtTail(head,data)
printLinkedList(head)

