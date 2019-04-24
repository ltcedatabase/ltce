queue=[1,2,3,4,5,6]
print("Original queue is:",queue)
queue.append(7)
print("Queue after insertion is",queue)
queue.pop(0)
print("Queue after deletion is:",queue)
last_element_index=len(queue)-1
print("Value obtained after deletion operation is:",queue[last_element_index])
print("First element in queue is",queue[0])