# bicycle.py
from transport import Transport

class Bicycle(Transport):
    """
    Класс Велосипед, наследник Средства передвижения.
    """
    def __init__(self, model, average_speed, passengers=1):
        super().__init__(model, average_speed, passengers)

    def fuel_consumption(self, distance):
        """
        Велосипед не потребляет топливо.
        """
        return 0
