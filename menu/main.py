from collections import deque
from abc import ABCMeta, abstractstaticmethod

class Session(metaclass=ABCMeta):
    __instance = None
    history = deque()
    currentCapsule = history[-1]

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls
        return cls.__instance

    def control(self):
        """ Control of menu """


class Capsule:
    def __init__(self, title):
        self.title = title
        self.components = deque()

class Component:
    def __init__(self):
        pass #type, clickable, position
class SimpleButton:
    def __init__(self, parent: Capsule, title):
        self.title = title
        parent.components.append(self)

