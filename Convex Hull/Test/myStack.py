class myStack(object):

    def __init__(self):
        self.stackContents = [None]*2000
        self.currentSize = 0

    def stackPop(self):
        "This method removes and returns the top most element in the stack"
        if self.stackContents[0] is None:
            return None
        else:
            item = self.stackContents[self.currentSize-1]
            self.stackContents[self.currentSize-1] = None
            self.currentSize -= 1
            return item

    def stackTop(self):
        "This method returns the top most element of the stack"
        if self.stackContents[0] is None:
            return None
        else:
            item = self.stackContents[self.currentSize-1]
            return item

    def stackPush(self, element):
        "This method inserts element into the current stack"
        self.stackContents[self.currentSize] = element
        self.currentSize += 1

    def printStack(self):
        for i in range(0, self.currentSize):
            print self.stackContents[i],
        print ""

    def stackSize(self):
        return self.currentSize


HullX = myStack()

HullX.stackPush(54)
HullX.stackPush(87)
HullX.stackPush(856)
HullX.stackPush(11)
HullX.stackPush(21)
HullX.stackPush(35)

HullX.printStack()
print HullX.stackPop()
print HullX.stackSize()
print HullX.stackTop()
