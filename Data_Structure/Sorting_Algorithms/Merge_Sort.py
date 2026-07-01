"""
Merge Sort:- 
 - It is a highly efficient, comparison-based sorting algorithm that uses the "divide and conquer" strategy
        Divide: The algorithm continually divides the unsorted list in half until each sublist consists of exactly one element.
        Conquer: Since a single element is already inherently sorted, it treats these sublists as trivially sorted and skips extra computation for them.
        Merge: The algorithm systematically merges adjacent pairs of sublists together by comparing their elements and arranging them in the correct sequence. This process is repeated until a single, fully sorted list remains
"""

def mergeSort(size, FunctionElements):
    if size == 1 or size == 0:
        return FunctionElements
    
    mid = size // 2
    firstHalf = FunctionElements[:mid]
    secondHalf = FunctionElements[mid:]
    
    sortedList1 = mergeSort(size=len(firstHalf), FunctionElements = firstHalf)
    sortedList2 = mergeSort(size=len(secondHalf), FunctionElements = secondHalf)

    finalList = []
    i = 0
    j = 0
    
    while j < len(sortedList2) and i < len(sortedList1):
        if sortedList1[i] <= sortedList2[j]:
            finalList.append(sortedList1[i])
            i += 1
        else:
            finalList.append(sortedList2[j])
            j += 1
    # else:
    #     if j == len(sortedList2):
    #         finalList.extend(sortedList1[i:])
    #     elif i == len(sortedList1):

    finalList.extend(sortedList2[j:])
    finalList.extend(sortedList1[i:])

    return finalList
    
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
    sortedList = mergeSort(size=size, FunctionElements=elements)
    print(f'Elements after sorting: {sortedList}')

if __name__ == '__main__':
    main()

