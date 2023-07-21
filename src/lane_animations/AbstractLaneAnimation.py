from abc import ABCMeta, abstractmethod
from typing import List, Tuple

Frame = List[Tuple]


class AbstractLaneAnimation(metaclass=ABCMeta):

    @abstractmethod
    def advance_animation(self):
        pass

    @abstractmethod
    def get_state(self) -> Frame:
        pass
