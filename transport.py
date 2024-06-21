# transport.py

class Transport:
    """
    Базовый класс для средств передвижения.
    Атрибуты:
    - model (str): название модели
    - average_speed (float): средняя скорость
    - passengers (int): количество пассажиров
    """
    def __init__(self, model, average_speed, passengers):
        self.model = model
        self.average_speed = average_speed
        self.passengers = passengers

    def fuel_consumption(self, distance):
        """
        Виртуальный метод для расчета потребления топлива на заданное расстояние.
        Переопределится в наследниках.
        """
        pass

    def travel_time(self, distance):
        """
        Расчет времени движения на заданное расстояние.
        """
        return distance / self.average_speed
