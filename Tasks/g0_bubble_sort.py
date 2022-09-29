from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    offset = 1
    for _ in range(len(container)):
        for i in range(len(container) - offset):
            current_elem = container[i]
            next_elem = container[i+1]
            if current_elem > next_elem:
                container[i], container[i+1] = next_elem, current_elem
        offset += 1
    return container
