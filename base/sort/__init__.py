import abc


class Sort:
    @classmethod
    @abc.abstractmethod
    def sort(cls, arr):
        pass
