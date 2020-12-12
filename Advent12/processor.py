import inspect
import math

class baseProcessor:
    def __init__(self, program):
        self.pointer = 0
        self.accumulator_x = 0
        self.accumulator_y = 0
        self.angle = 0
        self.program = program
        self.functions = dict([(key, value) for key, value in inspect.getmembers(self.__class__, predicate = inspect.isfunction) if not key in ['executeCurrent','__init__','ready','finished']])
    
    def executeCurrent(self):
        self.functions[self.program[self.pointer][0]](self, self.program[self.pointer][1])
        self.pointer = self.pointer + 1

    def ready(self):
        return 0 <= self.pointer < len(self.program)

    def finished(self):
        return self.pointer == len(self.program)

class processor(baseProcessor):
    def __init__(self, program):
        super().__init__(program)
        self.factor_x = 1
        self.factor_y = 0

    def N(self, value):
        self.accumulator_y = self.accumulator_y + value

    def S(self, value):
        self.accumulator_y = self.accumulator_y - value
    
    def E(self, value):
        self.accumulator_x = self.accumulator_x + value

    def W(self, value):
        self.accumulator_x = self.accumulator_x - value

    def L(self, value):
        self.angle = self.angle + value
        radangle = math.radians(self.angle)
        self.factor_x = round(math.cos(radangle))
        self.factor_y = round(math.sin(radangle))

    def R(self, value):
        self.angle = self.angle - value
        radangle = math.radians(self.angle)
        self.factor_x = round(math.cos(radangle))
        self.factor_y = round(math.sin(radangle))

    def F(self, value):
        self.accumulator_x = self.accumulator_x + (self.factor_x * value)
        self.accumulator_y = self.accumulator_y + (self.factor_y * value)

class processor2(baseProcessor):
    def __init__(self, program):
        super().__init__(program)
        self.factor_x = 10
        self.factor_y = 1

    def N(self, value):
        self.factor_y = self.factor_y + value

    def S(self, value):
        self.factor_y = self.factor_y - value
    
    def E(self, value):
        self.factor_x = self.factor_x + value

    def W(self, value):
        self.factor_x = self.factor_x - value

    def L(self, value):
        self.angle = self.angle + value
        radangle = math.radians(value)
        x = round(math.cos(radangle)*self.factor_x - math.sin(radangle)*self.factor_y)
        y = round(math.sin(radangle)*self.factor_x + math.cos(radangle)*self.factor_y)
        self.factor_x = x
        self.factor_y = y

    def R(self, value):
        self.L(- value)

    def F(self, value):
        self.accumulator_x = self.accumulator_x + (self.factor_x * value)
        self.accumulator_y = self.accumulator_y + (self.factor_y * value)
