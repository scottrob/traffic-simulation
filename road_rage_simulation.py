import random

from road_rage_car import *

class Simulation:
    def __init__(self):
        self.cars = []
        total_cars = range(3)
        car_in_front = None

        for i in total_cars:
            car = Car(i * 20, car_in_front)
            car_in_front = car
            self.cars.append(car)

        self.cars[0].car_in_front = self.cars[-1]

    def run(self):
        while True:
            for car in self.cars:
                # for 10% of the time...
                car.acceleration = random.randint(-2, 2)
                if car.can_move():
                    car.move()
            break # only run 1 time

def main():
    Simulation().run()

if __name__ == '__main__':
    main()
