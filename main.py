# main.py
from bicycle import Bicycle
from car import Car
from truck import Truck

def demonstrate(vehicle):
    distance = 100  # Расстояние для демонстрации
    print(f"Модель: {vehicle.model}")
    print(f"Время в пути на расстояние {distance} км: {vehicle.travel_time(distance)} часов")
    print(f"Потребление топлива на расстояние {distance} км: {vehicle.fuel_consumption(distance)} литровn")

bicycle = Bicycle("Mountain Bike", 15, 1)
car = Car("Sedan", 60, 4, 8)
truck = Truck("BigTruck", 45, 2, 30, 5000)

demonstrate(bicycle)
demonstrate(car)
demonstrate(truck)
