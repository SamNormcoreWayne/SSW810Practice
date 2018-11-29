# @author: Ziyu Zhang
# BiTree impleted!
# I use both queue and stack to maintain the tree.
# It was super tough when I was dealing with preoreder traversal with stack.
# But finally I figured it out.


class Queue:
    __slots__ = {'size', 'data'}

    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self):
        if len(self.data) == 0:
            return 'Queue is empty'
        return self.data.pop()


class Stack:

    __slots__ = {'size', 'data'}

    def __init__(self, max_size=100):
        # I define size to limit stack in case of stack overflow.
        # I believe this is a good habit to assign size before use.
        self.size = max_size
        self.data = []

    def push(self, element):
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


class BiNode:
    __slots__ = {'value', 'leftChild', 'rightChild'}

    def __init__(self, value, leftChild=None, rightChild=None):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild


class BITree:
    __slots__ = {'root', 'leftChild', 'rightChild'}

    def __init__(self, value, leftChild=None, rightChild=None):
        self.root = BiNode(value, leftChild, rightChild)

    def add_element(self, value=None):
        # Actually this is a procedure of level order traversal
        Node = BiNode(value)
        if self.root is None:
            self.root = Node
        else:
            NodeQueue = Queue()
            NodeQueue.enqueue(self.root)
            while True:
                item = NodeQueue.dequeue()
                if item.leftChild is None:
                    item.leftChild = Node
                    return True
                elif item.rightChild is None:
                    item.rightChild = Node
                    return True
                else:
                    NodeQueue.enqueue(item.leftChild)
                    NodeQueue.enqueue(item.rightChild)

    '''
    IGNORE this docstring! I do not know what I was writing.
    Maybe this is just a stack version of add_element which is super unreadable.
    It is so weired that I cannot remember why I wrote this method.

    def traversal(self):
        NodeStack = Stack()

        EleList = [self.root.value]
        print(self.root.value)
        NodeStack.push(self.root)
        while True:
            if self.root.leftChild is not None:
                EleList.append(self.root.leftChild.value)
                # print(self.root.leftChild.value)
            if self.root.rightChild is not None:
                EleList.append(self.root.rightChild.value)
                # print(self.root.rightChild.value)
            if self.root.leftChild is not None:
                self.root = self.root.leftChild
                NodeStack.push(self.root)
            if self.root.leftChild is None and self.root.rightChild is None:
                NodeStack.pop()
                self.root = NodeStack.pop()
                self.root = self.root.rightChild
                if NodeStack.is_empty() and self.root.leftChild is None and self.root.rightChild is None:
                    break
                else:
                    NodeStack.push(self.root)

        return EleList
    '''

    def preorder_traversal(self):
        # Basically, for this kind of recursive program,
        # I think, first we can use recurse function to define it
        # Or, stack or queue is also a nice choice depends on its property.
        # Actually maybe I can implement this traversal as a generator.
        NodeStack = Stack()
        EleList = []
        Node = self.root

        while True:
            while Node is not None:
                # Make sure I will visit all left children firstly.
                EleList.append(Node.value)
                if Node.leftChild is not None:
                    # If it is none, I will not push it because no need to backtrack this node.
                    NodeStack.push(Node)
                Node = Node.leftChild
            if not NodeStack.is_empty():
                # If it is empty, it means all nodes are visited, so break.
                # If it is not, then pop something, then visit its right child.
                Node = NodeStack.pop()
                Node = Node.rightChild
            else:
                break
        return EleList

    def preorder_traversal_recurse(self, Node):
        if Node is None:
            return []
        Elelist = [Node.value]
        left_value = self.preorder_traversal_recurse(Node.leftChild)
        right_value = self.preorder_traversal_recurse(Node.rightChild)
        return Elelist + left_value + right_value

    def preorder_traversal_rowland(self):
        values = list()

        if self.leftChild:
            values.extend(self.leftChild.preorder_traversal_rowland())

        values.append(self.value)

        if self.rightChild:
            values.extend(self.rightChild.preorder_traversal_rowland())

        return values

    def find(self, value):
        # I firmly believe that find() is a kind of traversal in its worst case.
        # So why not just traverse all nodes and then find the correct one by a nice search method.
        # I did not use str.find() but I write a binary_search() function.
        EleList = self.preorder_traversal()
        EleList.sort()
        return binary_search(EleList, value)


def binary_search(sequence, value):
    start = 0
    end = len(sequence) - 1
    while start <= end:
        middle = int(start + (end - start) / 2)
        if sequence[middle] == value:
            return True
        elif value < sequence[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return False


def main():
    tree = BITree(1)
    tree.add_element(2)
    tree.add_element(3)
    tree.add_element(4)
    tree.add_element(5)
    tree.add_element(6)
    tree.add_element(7)
    tree.add_element(8)
    tree.add_element(9)
    tree.add_element(10)
    tree.add_element(11)
    tree.add_element(12)
    tree.add_element(13)
    print(tree.preorder_traversal())
    print(tree.preorder_traversal_recurse(tree.root))
    i = input('Input element you want to find in the tree: ')
    print('find result: ', tree.find(int(i)))


if __name__ == '__main__':
    main()
