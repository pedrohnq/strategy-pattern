from solution.strategies.interface import DeliveryStrategyInterface

from classes import Destination, Order


class BikeDelivery(DeliveryStrategyInterface):
    """
    Strategy that represents a bike delivery
    """
    def execute(self, order: Order, destination: Destination):
        print("Delivering by bike")


class CarDelivery(DeliveryStrategyInterface):
    """
    Strategy that represents a car delivery
    """
    def execute(self, order: Order, destination: Destination):
        print("Delivering by car")


class TruckDelivery(DeliveryStrategyInterface):
    """
    Strategy that represents a truck delivery
    """
    def execute(self, order: Order, destination: Destination):
        print("Delivering by truck")


class BoatDelivery(DeliveryStrategyInterface):
    """
    Strategy that represents a boat delivery
    """
    def execute(self, order: Order, destination: Destination):
        print("Delivering by boat")


class ShipDelivery(DeliveryStrategyInterface):
    """
    Strategy that represents a ship delivery
    """
    def execute(self, order: Order, destination: Destination):
        print("Delivering by ship")


class PlaneDelivery(DeliveryStrategyInterface):
    """
    Strategy that represents a plane delivery
    """
    def execute(self, order: Order, destination: Destination):
        print("Delivering by plane")