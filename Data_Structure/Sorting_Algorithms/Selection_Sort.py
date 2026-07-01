"""
Selection Sort: 
 - Selection Sort is a comparison-based sorting algorithm. 
 - It sorts by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element
"""

def selectionSort(size, elements):
    currentIndex = 0
    while currentIndex < size:
        currentElement = elements[currentIndex]
        check = None
        for i in range(currentIndex + 1, size):
            if elements[i] < currentElement:
                currentElement = elements[i]
                check = i

        if check is not None:
            elements[check] = elements[currentIndex]
            elements[currentIndex] = currentElement

        currentIndex += 1        


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
    selectionSort(size=size, elements=elements)
    print(f'Elements after sorting: {elements}')


if __name__ == '__main__':
    main()

