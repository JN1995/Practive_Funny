"""
Author: Duan Le Van
Date:   Oct 05, 2019
"""

class Task:

    """
    INFO: Task - class define job to do in interval

        attribute:

            + name: _name
            + begin: _b
            + end: _e
            + time: _t
            + numofworker_per_unit: _w
            + prerequisite: _pc
            + condition_boundary: _cb

        method: 

            =

    """

    def __init__(self, name, b, e, w, t=None, pc=None, cb=None):

        self._name = name
        self._b = b
        self._e = e 
        self._t = e - b + 1 if t == None else t
        self._w = w
        self._pc = pc 
        self._cb = cb


    def all_worker(self):

        return self._t * self._w


class Work:

    def __init__(self, *tasks):

        self.tasks = sorted(tasks, key=lambda x: x._b)
        self._histogram = self.__calculate_histogram()

    
    def __calculate_histogram(self):

        for t in self.tasks:
            print(t._name)

        return []

    def max_workers(self):

        return max(self._histogram)


    def average_workers(self):

        return sum(self._histogram)/len(self._histogram)


            
