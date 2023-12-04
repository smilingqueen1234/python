#wapp to reverse the given linked lisclass SinglyLinkedListNode:
class SinglyLinkedListNode:
    def __init__ (self,data):
        self.data = data
        self.next = None
def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next
def createLinkedList(elements):
    if not elements:
        return None
    head = SinglyLinkedListNode(elements[0])
    current = head
    for data in elements[1:]:
        current.next = SinglyLinkedListNode(data)
        current = current.next
    return head
test_cases = 1
test_data = [[1,2,3,4,5]]
for _ in range(test_cases):
    head = createLinkedList(test_data[_])
    print("Original Linked List:")
    printLinkedList(head)
    head = reverse(head)
    print("\nReversed Linked List:")
    printLinkedList(head)



