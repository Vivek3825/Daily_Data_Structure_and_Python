"""
QUEUE:- Follows FIFO principle
    Front (Head): The end from which elements are removed or deleted.
    Rear (Tail): The end at which new elements are inserted or added.
"""

class Queue:
    def __init__(self, size = 10):
        self.size = size
        self.enqueueLocation = 0
        self.dequeueLocation = 0
        self.queue = [None] * self.size

    def enqueue(self, element = None):
        if self.queue[self.enqueueLocation] == None:
            self.queue[self.enqueueLocation] = element
            if self.enqueueLocation == self.size - 1:
                self.enqueueLocation = 0
            else:
                self.enqueueLocation += 1
            return True
        else:
            return False

    def dequeue(self):
        if self.queue[self.dequeueLocation] is not None:
            dequeueElement = self.queue[self.dequeueLocation]
            self.queue[self.dequeueLocation] = None
            if self.dequeueLocation == self.size - 1:
                self.dequeueLocation = 0
            else:
                self.dequeueLocation += 1
            return dequeueElement
        else:
            return None

    def peek(self):
        self.peekElement = self.queue[self.dequeueLocation]
        if self.peekElement is not None:
            return True
        else:
            return False

    def isEmpty(self):
        if self.dequeueLocation == self.enqueueLocation and self.queue[self.dequeueLocation] is None:
            return True
        else:
            return False

    def isFull(self):
        if self.dequeueLocation == self.enqueueLocation and self.queue[self.dequeueLocation] is not None:
            return True
        else:
            self.space = None
            if self.isEmpty():
                self.space = self.size
                return False
            else:
                if self.dequeueLocation > self.enqueueLocation:
                    self.space = (self.dequeueLocation - self.enqueueLocation)    #Modification
                elif self.dequeueLocation < self.enqueueLocation:
                    self.space = self.size - (self.enqueueLocation - self.dequeueLocation)    #Modification
                return False

    def show(self):
        temp = []
        if self.isEmpty():
            return temp
        
        elif self.isFull():
            temp.extend(self.queue[self.enqueueLocation:])
            temp.extend(self.queue[:self.enqueueLocation])
            return temp
        
        else:
            if self.dequeueLocation > self.enqueueLocation:
                temp.extend(self.queue[self.dequeueLocation : self.size])
                temp.extend(self.queue[0 : self.enqueueLocation])
            elif self.dequeueLocation < self.enqueueLocation:
                temp.extend(self.queue[self.dequeueLocation : self.enqueueLocation])
            return temp


def main():
    size = int(input('Enter size of Queue: '))
    q = Queue(size = size)
    print(f'Queue has been created of size {len(q.queue)}')

    while True:
        print('___________________________________________________________________________\n')
        print('Choose an operation: -')
        print('To enqueue    --> 1')
        print('To dequeue    --> 2')
        print('To peek       --> 3')
        print('To isEmpty    --> 4')
        print('To isFull     --> 5')
        print('To show       --> 6')
        print('To exit       --> 0', '\n')
        
        i = int(input('Enter your choice: '))
        print('___________________________________________________________________________\n')

        if i == 0:
            break

        elif i == 1:
            element = input("Enter an element: ")
            en = q.enqueue(element = element)
            if en:
                print(f'Successfully enqueued element {element}')
            else:
                print('Enqueue operation failed. Maybe queue is full!')

        elif i == 2:
            de = q.dequeue()
            if de is not None:
                print(f'Successfully dequeued element {de}')
            else:
                print('Dequeue operation failed. Maybe queue is empty!')

        elif i == 3:
            if q.peek():
                print(f'The element at front is {q.peekElement}')
            else:
                print('Queue is empty!')

        elif i == 4:
            if q.isEmpty():
                print('Queue is empty!')
            else:
                print('Queue is not empty.')

        elif i == 5:
            check = q.isFull()
            if check:
                print('Queue is Full!')
            else:
                print(f'Queue is not full. {q.space} elements space are available')

        elif i == 6:
            print(f'Queue: Front --> {q.show()} <-- Rear')

        else:
            print('Invalide Choice!')

if __name__ == '__main__':
    main()