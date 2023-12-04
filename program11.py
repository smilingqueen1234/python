import queue
q1 = queue.Queue()
q1.put(11)
q1.put(5)
q1.put(4)
q1.put(21)
q1.put(3)
def reverseQueue (q1src,q2dest):
    buffer = q1src.get()
    if (q1src.empty()==False):
        reverseQueue(q1src,q2dest)
    q2dest.put(buffer)
    return q2dest
q2dest = queue.Queue()
qReversed = reverseQueue(q1,q2dest)
while(qReversed.empty()==False):
    print(qReversed.queue[0],end=" ")
    qReversed.get()
