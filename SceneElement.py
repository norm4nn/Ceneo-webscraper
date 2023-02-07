from abc import ABC, abstractmethod


class AbstractSceneElement(ABC):
    def __init__(self, scene):
        self.scene = scene

    @abstractmethod
    def create(self):
        pass