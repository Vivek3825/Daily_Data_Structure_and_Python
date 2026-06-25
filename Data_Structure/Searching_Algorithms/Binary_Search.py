"""
Binary Search: -
 - It uses a divide-and-conquer strategy to find a target value by repeatedly dividing the search space in half.
"""

# Using Reccurson
# def binarySearch(my_list = None,  element = None, start = 0, end = None):
        
#         pivotElement = (start + end) // 2

                
#         if start > end:
#             return False
        
#         elif my_list[pivotElement] == element:
#             return pivotElement 

#         elif element > my_list[pivotElement]:
#             return binarySearch(my_list=my_list, element=element, start=pivotElement + 1, end=end)

#         elif element < my_list[pivotElement]:
#             return binarySearch(my_list=my_list, element=element, start=start, end=pivotElement - 1)


# Using Loop
def binarySearch(my_list = None,  element = None, end = None):
    start = 0
    while start <= end:
        pivotElement = (start + end) // 2
        
        if my_list[pivotElement] == element:
            return pivotElement
        
        elif my_list[pivotElement] > element:
            end = pivotElement - 1

        elif my_list[pivotElement] < element:
            start = pivotElement + 1

    return False


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

    while True:
        for i in range(size):
            while True:
                try:
                    my_list.append(int(input(f"Enter element {i+1}: ")))
                    break
                except ValueError:
                    print('input must be integer only! Please enter a value again:')
        check = sorted(my_list)
        if check == my_list:
            break
        else:
            print('List is not sorted, Please enter elements in sorted order')
            my_list = []   

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

    elementIndex = binarySearch(my_list=my_list, element=searchElement, end = len(my_list) - 1)

    if type(elementIndex) is not bool:
        print(f"Element found at {elementIndex} indexes")
    else:
        print('Element not found!!')

if __name__ == '__main__':
    main()