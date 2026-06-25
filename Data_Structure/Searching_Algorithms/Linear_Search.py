"""
Linear Search: - 
 - It is a fundamental searching algorithm that sequentially checks every element in a collection
   from start to finish until a match is found or the data structure ends.
"""

def linearSearch(my_list, element = None):
    idx = []
    for i in range(len(my_list)):
        if my_list[i] == element:
            idx.append(i)

    return idx

def getData():
    my_list = []
    searchElement = None
    print('___________________Please enter integer values_____________________\n')

    while True:
        try:
            size = int(input('Enter size of elements: '))
            break
        except ValueError:
            print('Input must be an integer value! Please enter a value again:')

    print('___________________________________________________________________________\n')


    print('___________________________________________________________________________\n')

    for i in range(size):
        while True:
            try:
                my_list.append(int(input(f"Enter element {i+1}: ")))
                break
            except ValueError:
                print('input must be integer only! Please enter a value again:')
    
    print('___________________________________________________________________________\n')
    while True:
        try:
            searchElement = int(input('Enter search element: '))
            break
        except ValueError:
            print('Search element must be integer only! Please enter a value again:')

    print('___________________________________________________________________________\n')

    return my_list, searchElement



def main():
    my_list, searchElement= getData()

    elementIndex = linearSearch(my_list=my_list, element=searchElement)

    if elementIndex:
        print(f"Element found at {elementIndex} indexes")
    else:
        print('Element not found!!')


if __name__ == '__main__':
    main()