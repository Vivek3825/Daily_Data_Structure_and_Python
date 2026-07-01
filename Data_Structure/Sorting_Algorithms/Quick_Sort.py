"""
Merge Sort:- 
 - Quick Sort is a highly efficient, comparison-based sorting algorithm that operates on the Divide and Conquer principle
        it picks an element as a pivot and partitions the remaining elements into two sub-arrays 
        according to whether they are less than or greater than the pivot
"""

def quickSort(size, FunctionElements):
    if size <= 1:
        return FunctionElements
    
    pivot = FunctionElements[size-1]
    smaller = []
    larger = []

    for i in range(size-1):
        if FunctionElements[i] <= pivot:
            smaller.append(FunctionElements[i])
        else:
            larger.append(FunctionElements[i])

    finalList = []

    finalList.extend(quickSort(size=len(smaller), FunctionElements = smaller))
    finalList.append(pivot)
    finalList.extend(quickSort(size=len(larger), FunctionElements = larger))

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
    sortedList = quickSort(size=size, FunctionElements=elements)
    print(f'Elements after sorting: {sortedList}')

if __name__ == '__main__':
    main()

