class Car():
    def __init__(self, pos_in_road, car_in_front):
        self.pos_in_road = pos_in_road
        self.length = 5
        self.max_speed = 33.33
        self.acceleration = 2
        self.current_speed = 0
        self.car_in_front = car_in_front

    def can_move(self):
        return (self.pos_in_road + self.length + self.current_speed) != self.car_in_front.pos_in_road

    def move(self):
        self.pos_in_road += self.current_speed
        print('move pos: ', self.pos_in_road)

    def accel(self):
        if self.current_speed < self.max_speed:
            self.current_speed += self.acceleration
        elif self.current_speed > self.max_speed:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>police:', self.current_speed)
            self.current_speed = self.max_speed


    def slow(self):
        if self.current_speed > 0:
            self.current_speed -= self.acceleration
        else:
            pass

    def stop(self):
        self.current_speed = 0
        print('stop pos: ', self.pos_in_road)
