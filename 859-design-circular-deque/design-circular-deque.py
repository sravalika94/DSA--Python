class MyCircularDeque:

    def __init__(self, k):
        self.q = [0] * k
        self.k = k
        self.front = 0
        self.rear = -1
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k
        self.q[self.front] = value
        self.size += 1
        if self.size == 1:
            self.rear = self.front
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        self.size += 1
        if self.size == 1:
            self.front = self.rear
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        return True

    def getFront(self):
        return -1 if self.isEmpty() else self.q[self.front]

    def getRear(self):
        return -1 if self.isEmpty() else self.q[self.rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.k