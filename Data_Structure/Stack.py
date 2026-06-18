"""
STACK:- Follows LIFO principle
    Top: 
    The pointer that tracks the topmost element in the stack. 
    All insertions and deletions happen exclusively at this position.
"""

class Stack:
    def __init__(self, size = 10):
        self.size = size
        self.list = [None] * self.size
        self.currentLocation = 0
        # print(type(self.list))
        # print(len(self.list))
        print(f'Stack has been created of size {len(self.list)}\n')

    def push(self):
        if self.currentLocation < self.size:
            element = input("Enter an element: ")
            self.list[self.currentLocation] = element
            self.currentLocation += 1
            print(f'Successfully added element {element}')
        else:
            self.isFull()

    def pop(self):
        if self.currentLocation == 0:
            self.isEmpty()
            return None
        else:
            self.currentLocation -= 1
            popElement = self.list[self.currentLocation]
            self.list[self.currentLocation] = None
            print(f'Successfully poped element {popElement}')
            return popElement

    def isEmpty(self):
        if self.currentLocation == 0:
            print('Stack is empty...')
            return True
        else:
            print('Stack is not empty')
            return False

    def isFull(self):
        if self.currentLocation == self.size:
            print('Stack is full!')
            return True

        else:
            print(f"{self.size - self.currentLocation} Elements space is available in the Stake")
            return False

    def show(self):
        print(f'Stack elements are: {self.list[:self.currentLocation]}')

    def peer(self):
        peerElement = self.list[self.currentLocation - 1]
        print(f'Top element in the Stack is {peerElement}')
        return(peerElement)

def main():
    size = int(input('Enter size of Stack: '))
    s = Stack(size = size)

    while True:
        print('___________________________________________________________________________\n')
        print('Choose an operation: -')
        print('To push     --> 1')
        print('To pop      --> 2')
        print('To isEmpty  --> 3')
        print('To isFull   --> 4')
        print('To Show     --> 5')
        print('To Peer     --> 6')
        print('To exit     --> 0', '\n')
        
        i = int(input('Enter your choice: '))
        print('___________________________________________________________________________\n')

        if i == 0:
            break
        elif i == 1:
            s.push()
        elif i == 2:
            s.pop()
        elif i == 3:
            s.isEmpty()
        elif i == 4:
            s.isFull()
        elif i == 5:
            s.show()
        elif i == 6:
            s.peer()
        else:
            print('Invalide Choice!')



if __name__ == '__main__':
    main()