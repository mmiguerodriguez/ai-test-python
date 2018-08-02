import copy
import math

class Experiment:
    def __init__(self, vars, inpt, output, times):
        self.vars = vars
        self.inpt = inpt
        self.output = output
        self.times = times

    def generate_input(self):
        inpt = self.inpt()
        self.last_inpt = copy.deepcopy(inpt)
        return inpt

    def fitness(self, output, code):
        exec(' '.join(self.last_inpt))
        correct_output = int(eval(self.output))
        if 'error' in str(output):
            if '1' in output:
                fitness = -3
            if '2' in output:
                fitness = -2
            if '3' in output:
                fitness = -4
        else:
            fitness = self.fitness_func(correct_output - output)
        return fitness - len(code) / 5

    @staticmethod
    def fitness_func(x):
        if x < 0: return math.exp(x / 10 + 3)
        else:     return math.exp(-x / 10 + 3)
