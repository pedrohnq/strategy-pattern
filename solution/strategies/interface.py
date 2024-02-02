from abc import ABC, abstractmethod

from classes import Destination, Order


class DeliveryStrategyInterface(ABC):
    """
    Interface that represents a delivery strategy
    """
    @abstractmethod
    def execute(self, order: Order, destination: Destination):
        pass