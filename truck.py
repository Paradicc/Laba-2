# truck.py
from car import Car

class Truck(Car):
    """
    Класс Грузовик, наследник Автомобиля.
    Перегружает метод fuel_consumption.
    """
    def __init__(self, model, average_speed, passengers, fuel_rate, cargo_weight):
        super().__init__(model, average_speed, passengers, fuel_rate)
        self.cargo_weight = cargo_weight  # Вес груза

    def fuel_consumption(self, distance):
        """
        Расчет потребления топлива с учетом веса груза.
        """
        base_consumption = super().fuel_consumption(distance)
        return base_consumption * (1 + self.cargo_weight / 2000)
