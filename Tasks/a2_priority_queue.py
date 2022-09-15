"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.prior_queue = []  # для очереди можно использовать python dict


    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.enqueue_item = {"elem": elem, "priority": priority}
        if not self.prior_queue:
            self.prior_queue.append(self.enqueue_item)
            return None
        for ind, self.current_item in enumerate(self.prior_queue):
            if self.enqueue_item["priority"] >= self.current_item["priority"]:
                self.prior_queue.insert(ind, self.enqueue_item)
                break
        else:
            self.prior_queue.append(self.enqueue_item)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.prior_queue:
            return None

        return self.prior_queue.pop()["elem"]

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        print(ind)

        reversed_index = -ind - 1
        return self.prior_queue[reversed_index]["elem"]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.prior_queue.clear()
        return None
