# car.py
from transport import Transport

class Car(Transport):
    """
    Класс Автомобиль, наследник Средства передвижения.
    """
    def __init__(self, model, average_speed, passengers, fuel_rate):
        super().__init__(model, average_speed, passengers)
        self.fuel_rate = fuel_rate  # Расход топлива на 100 км

    def fuel_consumption(self, distance):
        """
        Расчет потребления топлива на заданное расстояние.
        """
        return (distance / 100) * self.fuel_rate
