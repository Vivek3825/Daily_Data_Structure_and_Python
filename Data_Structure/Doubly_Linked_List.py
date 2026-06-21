"""
LINKED LIST:- 
  -  A linked list is a linear data structure where elements are not stored at contiguous memory locations. 
  -  Instead, the elements are separate objects called nodes, which are chained together using pointers or references.
  -  Structure of a Node: -
       - Data: The actual value or information stored in the element.
       - Next/Previous Pointer: A reference variable storing the memory address of the next node in the sequence
"""

class Node:
    def __init__(self, data = None, preNodeAddress = None, nextNodeAddress = None, nodeID = None):
        self.data = data
        self.nodeID = nodeID
        self.preNodeAddress = preNodeAddress
        self.nextNodeAddress = nextNodeAddress      #Update only next node get created

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.ID = 1

    def insertion(self, data = None):
        key = 'Node' + str(self.ID)
        temp = Node(data=data, preNodeAddress=self.tail, nodeID=key)

        if self.tail is not None:
            self.tail.nextNodeAddress = temp
        else:
            self.head = temp

        self.tail = temp
        self.ID += 1

        if temp.nodeID == key:
            return key
        else:
            return False

    def Deletion(self, deleteData = None):
        if self.head == None:
            return False

        currentNode = self.head
        countNode = []
        while currentNode is not None:
            nextNode = currentNode.nextNodeAddress
            previousNode = currentNode.preNodeAddress

            if currentNode.data == deleteData:
                    if currentNode.preNodeAddress is not None:
                        previousNode.nextNodeAddress = currentNode.nextNodeAddress
                    else:
                        self.head = currentNode.nextNodeAddress

                    if currentNode.nextNodeAddress is not None:
                        nextNode.preNodeAddress = currentNode.preNodeAddress 
                    else:
                        self.tail = currentNode.preNodeAddress 

                    countNode.append(currentNode.nodeID)
            
            currentNode = nextNode

        return countNode

    def traversal(self):
        return self.head

    def Search(self, searchData = None):
        if self.head == None:
            return False
        
        currentNode = self.head
        countNode = []
        while currentNode is not None:
            if currentNode.data == searchData:
                    countNode.append(currentNode.nodeID)
            
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
            check = ll.Deletion(deleteData = deleteData)
            if check:
                print(f'Successfully deleted nodes: {check} \nThey was containing data: {deleteData}')
            else:
                print('Deletion operation failed!. Linked List is empty or data does not present in the linked list')

        elif i == 3:
            check = ll.traversal()
            if check:
                print('HEAD ------------------------------->')
                while check is not None:
                    print('_____________________________________\n')

                    print('Node ID: ', check.nodeID)
                    print('Node Data: ', check.data)
                    print('Previous Node ID: ', check.preNodeAddress)
                    print('Next Node ID: ', check.nextNodeAddress)

                    print('_____________________________________\n')

                    check = check.nextNodeAddress

                print('<------------------------------- TAIL')
            else:
                print('Linked List is empty!')

        elif i == 4:
            searchData = input("Enter search data: ")
            check = ll.Search(searchData = searchData)
            if check:
                print(f'Data found in {check}')
            else:
                print('Search operation failed!. Linked List is empty or data does not present in the linked list')

        else:
            print('Invalide Choice!')

if __name__ == '__main__':
    main()