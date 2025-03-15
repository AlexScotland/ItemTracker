from abc import ABC, abstractmethod


class ProductPage(ABC):

    @abstractmethod
    def serialize(self, serializer):
        raise NotImplementedError
