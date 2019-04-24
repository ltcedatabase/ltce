stack=[1,2,3,4,5,6]
print("Original stack is:",stack)
stack.append(7)
print("stack after push operation is:",stack)
stack.pop()
print("stack after pop operation is:",stack)
print("Length of stack=",len(stack))
last_element_index=len(stack)-1
print("Last value of stack after pop operation is",stack[last_element_index])
del stack[:]
print("stack elements after deletion",stack)