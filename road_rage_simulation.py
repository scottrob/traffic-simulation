import random
from collections import deque
from road_rage_car import *
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self):
        self.cars = []
        total_cars = range(30)
        car_in_front = None
        for i in total_cars:
            car = Car(i * 20, car_in_front)
            car_in_front = car
            self.cars.append(car)

        self.cars[0].car_in_front = self.cars[-1]

    def run(self):
        count = 0
        count_car = 30

        list_for_graph = []
        while count <= 10:
            for car in reversed(self.cars):
                print('-------------->car: ', count_car)

                if car.can_move():
                    if random.random() < .1:
                        car.slow()
                    else:
                        car.accel()
                    car.move()

                if count_car == 1:
                    count_car = 30
                else:
                    count_car -= 1

                list_for_graph.append(car.pos_in_road)
            count += 1
        return list_for_graph


def main():
    listy = Simulation().run()
    plt.plot(listy, 'ro')
    #plt.axis([-1, 11, -1, 1000])
    plt.show()

if __name__ == '__main__':
    main()
