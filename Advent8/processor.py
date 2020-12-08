import inspect

class baseProcessor:
    def __init__(self, program):
        self.pointer = 0
        self.accumulator = 0
        self.program = program
        self.functions = dict([(key, value) for key, value in inspect.getmembers(self.__class__, predicate = inspect.isfunction) if not key in ['executeCurrent','__init__','ready','finished']])
    
    def executeCurrent(self):
        self.functions[self.program[self.pointer][0]](self, self.program[self.pointer][1])

    def ready(self):
        return 0 <= self.pointer < len(self.program)

    def finished(self):
        return self.pointer == len(self.program)


class processor(baseProcessor):
    def __init__(self, program):
        super().__init__(program)

    def nop(self, value):
        self.pointer = self.pointer + 1
    
    def acc(self, value):
        self.pointer = self.pointer + 1
        self.accumulator = self.accumulator + value

    def jmp(self, value):
        self.pointer = self.pointer + value
