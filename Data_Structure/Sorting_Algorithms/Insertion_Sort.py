"""
Insertion sort: -
 - It is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list 
   into its correct position in a sorted portion of the list. 
 - It is like sorting playing cards in your hands.
"""
#Swap Based Approach

# def insertionSort(size, elements):
#     sortIndex = 1
#     while sortIndex < (size):
#         for i in range(sortIndex, 0, -1):
#             if elements[i-1] < elements[i]:
#                 elements[i] = elements[i] + elements[i-1]
#                 elements[i-1] = elements[i] - elements[i-1]
#                 elements[i] = elements[i] - elements[i-1]
#             else:
#                 break
#         sortIndex += 1

#Shifting Based Approach

def insertionSort(size, elements):
    for i in range(1, size):
        tempElement = elements[i]

        tempIndex = i-1

        # while tempIndex >= 0:
        #     if elements[tempIndex] > tempElement:
        #         elements[tempIndex + 1] =  elements[tempIndex]
        #         tempIndex -= 1
        #     else:
        #         break

        while tempIndex >= 0 and elements[tempIndex] > tempElement:
            elements[tempIndex + 1] =  elements[tempIndex]
            tempIndex -= 1
            
        elements[tempIndex + 1] = tempElement
            



def getData():
    while True:
        try:
            size = int(input('Enter size of element: '))
            break
        except ValueError:
            print("Size must be an integer. Please enter element again.")
        
    elements = []

    for i in range(size):
        while True:
            try:
                elements.append(int(input(f'Enter element{i+1}: ')))
                break

            except ValueError:
                print("Element must be an integer. Please enter element again.")

    return size, elements

def main():
    print('___________________________________________________________________________\n')
    size, elements = getData()
    print('___________________________________________________________________________\n')
    print(f'Elements before sorting: {elements}')
    insertionSort(size=size, elements=elements)
    print(f'Elements after sorting: {elements}')


if __name__ == '__main__':
    main()

