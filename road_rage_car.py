class Car():
    def __init__(self, starting_pos):
        self.position = starting_pos
        self.size = 5
        self.max_speed = 33.33
        self.acceleration = 2
        self.slow = 2
        self.speed = 0

    def move_car(self):
        self.position[1] = self.position[0] + self.acceleration
        self.position[1] += 1
        return self.position

    def slow_down(self):
        self.position[1] = self.position[0] - self.slow
        self.position[1] += 1
