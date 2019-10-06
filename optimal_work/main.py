"""
Author: Duan Le Van
Date:   Oct 05, 2019
"""

from task import Task, Work


def main():

    task_a = Task("task A", 0, 1, 3)
    task_b = Task("task B", 0, 2, 5)
    task_c = Task("task C", 1, 2, 10)

    l = [task_a, task_c, task_b]

    w = Work(*l)

    w._histogram

if __name__ == "__main__":
    
    main()