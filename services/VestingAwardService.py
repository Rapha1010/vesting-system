import abc

class VestingAwardService(abc.ABC):
    @abc.abstractmethod
    def get_all(self):
        pass
    @abc.abstractmethod
    def get_by_id(self, id):
        pass