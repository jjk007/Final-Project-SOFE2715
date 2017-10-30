#!/usr/bin/env python2.7
# thou shall not cross 80 columns in thy file

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
