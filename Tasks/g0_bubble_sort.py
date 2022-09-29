from typing import List
from operator import lt, gt


def sort(container: List[int], ascending: bool = True, inplace: bool = True) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not inplace:
        container = container.copy()
    offset = 1
    compare_operator = gt if ascending else lt

    for _ in range(len(container)):
        is_change = False  # список изначально отсортирован

        for i in range(len(container) - offset):
            current_elem = container[i]
            next_elem = container[i+1]

            if compare_operator(current_elem, next_elem):
                if current_elem > next_elem:
                    container[i], container[i+1] = next_elem, current_elem
                    is_change = True

        if not is_change:
            break

        offset += 1

    return container


if __name__ == '__main__':
    list_ = [1, 17, 4, 9, 8, 34]
    sorted = sort(list_)
    print(list_)
    print(sorted)

    sorted = sort(list_, inplace=False)
    print(list_)
    print(sorted)
    # print(sort(list_, ascending=False))
