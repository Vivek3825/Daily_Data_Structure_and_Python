"""
Bubble Sort 
 - It is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.
"""

def bubbleSort(size, elements):
    optimize = size - 1
    found = True
    while found:
        found = False
        for i in range(optimize):
            if elements[i] > elements[i + 1]:
                elements[i] = elements[i] + elements[i + 1]
                elements[i + 1] = elements[i] - elements[i + 1]
                elements[i] = elements[i] - elements[i + 1]
                found = True
        
        optimize -= 1

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
    bubbleSort(size=size, elements=elements)
    print(f'Elements after sorting: {elements}')


if __name__ == '__main__':
    main()

