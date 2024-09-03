"""Working implementation of bubble sort

Part of lesson 'Bubble and Insertion Sort' (2023-10-05)"""


def bubble_sort(array: list):
    length = len(array)
    for current_pass in range(0, length):
        for i in range(length - 2 - current_pass):
            if array[i] > array[i + 1]:
                old_item = array[i]
                array[i] = array[i + 1]
                array[i + 1] = old_item


numbers = [3, 7, 1, 0, -2, 99, 999]
print(numbers)
bubble_sort(numbers)
print(numbers)
