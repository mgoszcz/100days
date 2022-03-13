from random import randint

from day23_turtle_crossing.car import Car
from day23_turtle_crossing.statics import MIN_X, MAX_X, MIN_Y, MAX_Y


class CarContainer:

    def __init__(self, car_count):
        self._max_car_count = car_count
        self._cars = []
        self.cars_initialize()
        self._speed = 1

    def cars_initialize(self):
        while len(self._cars) < self._max_car_count:
            car = Car()
            car.goto(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y))
            self._cars.append(car)

    def cars_update(self):
        cars_out_of_bounds = []
        for car in self._cars:
            car.move(self._speed)
            if car.xcor() < MIN_X:
                cars_out_of_bounds.append(car)

        for car in cars_out_of_bounds:
            car.hideturtle()
            self._cars.remove(car)
            new_car = Car()
            new_car.goto(MAX_X, randint(MIN_Y, MAX_Y))
            self._cars.append(new_car)

    def increase_speed(self):
        self._speed += 1

    def detect_collision(self, turtle_position):
        turtle_left = turtle_position[0][0]
        turtle_right = turtle_position[0][1]
        turtle_bottom = turtle_position[1][0]
        turtle_top = turtle_position[1][1]
        for car in self._cars:
            car_left = car.bounding_rect()[0][0]
            car_right = car.bounding_rect()[0][1]
            car_bottom = car.bounding_rect()[1][0]
            car_top = car.bounding_rect()[1][1]
            if (car_left < turtle_left < car_right) or (car_left < turtle_right < car_right):
                if (car_bottom < turtle_bottom < car_top) or (car_bottom < turtle_top < car_top):
                    return True
        return False
