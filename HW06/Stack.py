# @author: Ziyu Zhang
# It is fun to implement data structures.
# And it is good for no needs to new & delete or malloc & free


class Stack:

    __slots__ = {'size', 'data'}

    def __init__(self, max_size=100):
        # I define size to limit stack in case of stack overflow.
        # I believe this is a good habit to assign size before use.
        self.size = max_size
        self.data = []

    def push(self, element):
        if len(self.data) > self.size:
            raise ValueError('Stack Overflow.')
        else:
            self.data.append(element)
            return True

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty.')
        else:
            """
            element = self.data[self.index - 1]
            del self.data[self.index - 1]
            self.index -= 1
            return element
            """
            return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0
