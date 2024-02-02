from classes import Destination, Order


class DeliverySystem:
    """
    Class that represents a delivery system

    Methods:
        - execute_delivery: executes the delivery of an order to a destination
            - order: order to be delivered
            - destination: destination of the order
    """
    def execute_delivery(self, order: Order, destination: Destination):
        if destination.is_connected_by_road:
            if order.weight < 2 and order.volume < 2 and destination.distance < 1000:
                print("Delivering by bike")
            elif order.weight < 10 and order.volume < 10 and destination.distance < 10000:
                print("Delivering by car")
            else:
                print("Delivering by truck")
        elif destination.is_connected_by_sea and destination.distance < 7000 * 10^3:
            if order.weight < 10 and order.volume < 10:
                print("Delivering by boat")
            else:
                print("Delivering by ship")
        else:
            print("Delivering by plane")