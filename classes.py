class Destination:
    """
    Class that represents a destination
    
    Attributes:
        - distance: distance to the destination in meters
        - is_connected_by_road: True if the destination is connected by road
        - is_connected_by_sea: True if the destination is connected by sea
    """
    def __init__(self, distance, is_connected_by_road, is_connected_by_sea):
        self.distance = distance
        self.is_connected_by_road = is_connected_by_road
        self.is_connected_by_sea = is_connected_by_sea


class Order:
    """
    Class that represents an order

    Attributes:
        - weight: weight of the order in kilograms
        - volume: volume of the order in cubic meters
    """
    def __init__(self, weight, volume):
        self.weight = weight
        self.volume = volume