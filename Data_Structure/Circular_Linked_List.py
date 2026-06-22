"""
LINKED LIST:- 
  -  A linked list is a linear data structure where elements are not stored at contiguous memory locations. 
  -  Instead, the elements are separate objects called nodes, which are chained together using pointers or references.
  -  In CLL, End node next points start node and start node previous points end node
  -  Structure of a Node: -
       - Data: The actual value or information stored in the element.
       - Next/Previous Pointer: A reference variable storing the memory address of the next node in the sequence


"""

class Node:
    def __init__(self, data = None, preNodeAddress = None, nextNodeAddress = None, nodeID = None):
        self.data = data
        self.nodeID = nodeID
        self.preNodeAddress = preNodeAddress
        self.nextNodeAddress = nextNodeAddress      

class LinkedList:
    def __init__(self):
        self.end = None
        self.start = None
        self.ID = 1

    def insertion(self, data = None):
        key = 'Node' + str(self.ID)
        temp = Node(data=data, nextNodeAddress=self.start, preNodeAddress=self.end, nodeID=key)

        if self.end is not None:
            self.end.nextNodeAddress = temp
            self.start.preNodeAddress = temp
        else:
            temp.nextNodeAddress = temp
            temp.preNodeAddress = temp
            self.start = temp

        self.end = temp
        self.ID += 1

        if temp.nodeID == key:
            return key
        else:
            return False

    def deletion(self, deleteData = None):
        if self.start == None:
            return False

        currentNode = self.start
        countNode = []

        stop = False
        while True:
            nextNode = currentNode.nextNodeAddress
            previousNode = currentNode.preNodeAddress

            if currentNode.data == deleteData:
                if self.start == self.end:
                    countNode.append(self.start.nodeID)
                    self.start = None
                    self.end = None
                    break

                if currentNode == self.start:
                    self.start = currentNode.nextNodeAddress

                if currentNode == self.end:
                    self.end = currentNode.preNodeAddress
                    stop = True

                previousNode.nextNodeAddress = currentNode.nextNodeAddress
                nextNode.preNodeAddress = currentNode.preNodeAddress

                countNode.append(currentNode.nodeID)

            if currentNode == self.end or stop:
                break

            currentNode = nextNode

        return countNode


    def traversal(self):
        return self.start

    def search(self, searchData = None):
        if self.end == None:
            return False
        
        currentNode = self.start
        countNode = []
        while True:
            if currentNode.data == searchData:
                    countNode.append(currentNode.nodeID)
            
            if currentNode.nextNodeAddress == self.start:
                break
            currentNode = currentNode.nextNodeAddress

        return countNode
    

def main():
    ll = LinkedList()
    
    while True:
        check = None
        print('___________________________________________________________________________\n')
        print('Choose an operation: -')
        print('To insert a node    --> 1')
        print('To delete a node   --> 2')
        print('To Travel       --> 3')
        print('To Search    --> 4')
        print('To exit       --> 0', '\n')
        
        i = int(input('Enter your choice: '))
        print('___________________________________________________________________________\n')

        if i == 0:
            break

        elif i == 1:
            data = input("Enter an data: ")
            check = ll.insertion(data = data)
            if check:
                print(f'Successfully created {check}')
            else:
                print('insertion operation failed!')

        elif i == 2:
            deleteData = input("Enter delete data: ")
            check = ll.deletion(deleteData = deleteData)
            if check:
                print(f'Successfully deleted nodes: {check} \nThey was containing data: {deleteData}')
            else:
                print('Deletion operation failed!. Linked List is empty or data does not present in the linked list')

        elif i == 3:
            check = ll.traversal()
            if check:
                start = check
                print('HEAD ------------------------------->')
                while True:
                    print('_____________________________________\n')

                    print('Node ID: ', check.nodeID)
                    print('Node Data: ', check.data)
                    print('Previous Node ID: ', check.preNodeAddress.nodeID)
                    print('Next Node ID: ', check.nextNodeAddress.nodeID)

                    print('_____________________________________\n')

                    if check.nextNodeAddress == start:
                        break

                    check = check.nextNodeAddress

                print('<------------------------------- TAIL')
            else:
                print('Linked List is empty!')

        elif i == 4:
            searchData = input("Enter search data: ")
            check = ll.search(searchData = searchData)
            if check:
                print(f'Data found in {check}')
            else:
                print('Search operation failed!. Linked List is empty or data does not present in the linked list')

        else:
            print('Invalide Choice!')

if __name__ == '__main__':
    main()