from abc import ABCMeta, abstractmethod


class AbstractLaneAnimation(metaclass=ABCMeta):

    @abstractmethod
    def advance_animation(self):
        pass

    @abstractmethod
    def get_state(self):
        pass
