class ArrayStack:
    """ 通过 Python 列表实现 LIFO 栈"""

    def __init__(self):
        self._data = []

    def size(self):
        """ return the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        """ return True if the stack is empty"""
        return len(self._data) == 0

    def push(self, e):
        """ add element e to the top of the stack"""
        self._data.append(e)

    def pop(self):
        """ remove and return the element from the top of the stack
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data.pop()

    def top(self):
        """return the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]  # the last item in the list


arrayStack = ArrayStack()
arrayStack.push("Python")
arrayStack.push("Learning")
arrayStack.push("Hello")
print("Stack top element: ", arrayStack.top())
print("Stack length: ", arrayStack.size())
print("Stack popped item: %s" % arrayStack.pop())
print("Stack is empty?", arrayStack.is_empty())
arrayStack.pop()
arrayStack.pop()
print("Stack is empty?", arrayStack.is_empty())
# arrayStack.pop()