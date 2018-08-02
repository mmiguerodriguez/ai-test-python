import numpy as np
import copy
import math

class Experiment:
    def __init__(self, program, vars, inpt, output, times):
        self.program = program
        self.vars = vars
        self.inpt = inpt
        self.output = output
        self.times = times

    def generate_input(self):
        inpt = self.inpt()
        exec(' '.join(inpt))
        self.correct_output = int(eval(self.output))
        return copy.deepcopy(inpt)

    def fitness(self, output, code):
        fitness = self.fitness_fn(output) if type(output) != str else 0
        fitness += 1 if 'return' in code else 0
        fitness -= 2 if 'error' in str(output) else 0
        fitness -= len(code) / 5
        fitness += self.get_novelty(code)
        return fitness

    def get_novelty(self, code):
        codes = [a.code for a in self.program.agents]
        length = abs(np.average([len(c) for c in codes]) - len(code))#te acordas de c, migue?
        times = []
        for var in self.vars:
            own = code.count(var) / (len(code) + 1)
            others = np.average([c.count(var) / (len(c) + 1) for c in codes])
            times.append(abs(others - own))
        return length / 8 + np.average(times) / 4

    def fitness_fn(self, output):
        x = self.correct_output - output
        if x < 0: return math.exp(x / 10 + 3)
        else:     return math.exp(-x / 10 + 3)
