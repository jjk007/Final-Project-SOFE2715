class myStack(object):

    def __inti__(self):
        self.stackContents = [None]*2000
        self.currentSize = 0

    def stackPop(self):
        "This method removes and returns the top most element in the stack"
        if self.stackContents[0] is None:
            return None
        else:
            item = self.stackContents[self.currentSize]
            self.stackContents[self.currentSize] = None
            self.currentSize -= 1
            return item

    def stackTop(self):
        "This method returns the top most element of the stack"
        pass

    def stackPush(self, element):
        "This method inserts element into the current stack"
