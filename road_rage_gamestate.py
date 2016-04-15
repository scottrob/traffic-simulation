from road_rage_car import *


def make_cars():
    total_cars = range(30)
    car_in_front = None
    cars = []

    for i in total_cars:
        Car.car = (i * 20)
        car_in_front = Car.car
        cars.append(Car.car)

    print(cars)

print(make_cars())
