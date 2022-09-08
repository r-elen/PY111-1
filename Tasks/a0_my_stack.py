"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.stack = []  # для стека можно использовать python list
        self.reversed_index = None

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.stack.append(elem)  # добавление элемента в конец через append

        print(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """

        print(ind)

        try:
            reversed_index = -ind - 1
            return self.stack[reversed_index]
        except IndexError:
            return None


    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.stack.clear()
        return None
