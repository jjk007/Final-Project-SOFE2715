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

    def fullStack(self):
        return self.stackContents[0:self.currentSize]
    
    def stackSize(self):
        return self.currentSize

    def atIndex(self, index):
        if index > self.currentSize-1 or index < 0:
            raise Exception('listIndexOutOfRange')
        return self.stackContents[index]


HullX = myStack()

HullX.stackPush(54)
HullX.stackPush(87)
HullX.stackPush(856)
HullX.stackPush(11)
HullX.stackPush(21)
HullX.stackPush(35)

print HullX.fullStack()
print HullX.atIndex(-1)
