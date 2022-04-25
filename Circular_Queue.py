"""
Queue - Steps
1 - define the attributes: capacity (necessary to build the object), begin of the queue, final of the queue, nº elements, vector.
2 - two methods: 1 to determine if the queue is empty, other if is full.
3 - method to queue: first we verify if the queue is full, else we put the element in the last position
"""

import numpy as np


class CircularQueue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__begin = 0
        self.__final = -1
        self.__number_elements = 0
        self.__values = np.empty(self.__capacity, dtype=int)

    def __full_Queue(self):
        return self.__number_elements == self.__capacity

    def __empty_Queue(self):
        return self.__number_elements == 0

    def queue(self, value):
        if self.__full_Queue():
            print("Full queue!")
            return

        if self.__final == self.__capacity - 1:
            self.__final = - 1
        self.__final += 1
        self.__values[self.__final] = value
        self.__number_elements += 1

    def unqueue(self):
        if self.__empty_Queue():
            print("Queue is already empty!")
            return

        element = self.__values[self.__begin]
        self.__begin += 1
        if self.__begin == self.__capacity:
            self.__begin = 0
        self.__number_elements -= 1
        return element

    def first_queue(self):
        if self.__empty_Queue():
            return -1

        return self.__values[self.__begin]

    def view_queue(self):
        return self.__values

    def first_final_queue(self):
        return f"First element: {self.__values[self.__begin]}\nFinal element: {self.__values[self.__final]}"


queue = CircularQueue(5)

print(queue.first_queue())
print("---")
queue.queue(1)
queue.queue(2)
queue.queue(3)
queue.queue(4)
queue.queue(5)
print("---")
print(queue.first_queue())
print(queue.view_queue())
print(queue.first_final_queue())
print("---")
print(queue.unqueue())
print("---")
print(queue.unqueue())
print("---")
print(queue.unqueue())
print("---")
print(queue.first_queue())
print("---")
print(queue.unqueue())
print(queue.first_final_queue())
queue.queue(6)
queue.queue(7)
queue.queue(8)
queue.queue(9)
print("---")
print(queue.first_final_queue())
print(queue.view_queue())

