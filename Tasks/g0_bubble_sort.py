from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    for _ in range(len(container)):
        for i in range(len(container)-1):
            current_elem = container[i]
            next_elem = container[i+1]
            if current_elem > next_elem:
                container[i], container[i+1] = next_elem, current_elem
    return container
