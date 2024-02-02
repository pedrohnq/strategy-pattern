from solution.strategies.interface import DeliveryStrategyInterface

from classes import Destination, Order


class DeliverySystemContext:
    """
    Class that represents a delivery system context
    
    Attributes:
        - delivery_strategy: delivery strategy to be used
    """
    delivery_strategy = None

    def set_strategy(self, delivery_strategy: DeliveryStrategyInterface):
        self.delivery_strategy = delivery_strategy

    def execute_delivery(self, order: Order, destination: Destination):
        if self.delivery_strategy is None:
            raise Exception("Delivery strategy is not set")

        self.delivery_strategy.execute(order, destination)
