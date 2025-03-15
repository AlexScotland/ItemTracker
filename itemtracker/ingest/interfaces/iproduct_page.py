from abc import ABC, abstractmethod


class IProductPage(ABC):

    @abstractmethod
    def serialize(self, serializer):
        raise NotImplementedError
