def sort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


numbers = '13 56 34 25 67 89 78'
custom_number = int(input("Введите число: "))
number_list = [int(s) for s in numbers.split()]
number_list.append(int(custom_number))
sorted_number_list = sort(number_list)
print(sorted_number_list)
print("ID = ", binary_search(sorted_number_list, custom_number, 0, len(sorted_number_list) - 1))