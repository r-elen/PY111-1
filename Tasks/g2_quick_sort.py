from typing import List
from random import randint, choice


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if not container:
        return container
    pivot = choice(container)
    return sort([v for v in container if v < pivot])\
        + [v for v in container if v == pivot]\
        + sort([v for v in container if v > pivot])


    # первый вариант
    # def _sort(left_border, right_border):
    #     if left_border >= right_border:
    #         return
    #     random_index = randint(left_border, right_border)
    #     pivot = container[random_index]
    #
    #     i, j = left_border, right_border
    #     while i <= j:
    #         while container[i] < pivot:
    #             i += 1  # увеличивает на 1 пока не встретит равный или больше опорного
    #         while container[j] > pivot:
    #             j -= 1  # уменьшаем на 1 пока не встретит равный или меньше опорного
    #         if i <= j:
    #             container[i], container[j] = container[j], container[i]
    #             i += 1
    #             j -= 1
    #     _sort(left_border, j)
    #     _sort(right_border, i)
    #
    # _sort(0, len(container))
    #
    # return container


    # # мои идеи (не доделано)
    # random_index = randint(left_border, right_border)
    # support_elem = container[random_index]
    # left_result = []
    # right_result = []
    #
    # for _ in container:
    #     for i in range(len(container)):
    #         if container[i] < support_elem:
    #             left_result.append(container[i])
    #         if container[i] > support_elem:
    #             right_result.append(container[i])
    # return container
