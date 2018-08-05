import numpy as np
import random
import copy

class Agent:
    def __init__(self, code):
        self.code = code
        self.fitness = 0

    def run(self, experiment):
        for _ in range(experiment.times):
            inpt = experiment.generate_input()
            output = self.execute(inpt)
            self.fitness += experiment.fitness(output, self.code)
        self.fitness /= experiment.times

    def mutate(self, experiment):
        for _ in range(random.randint(0, 5)):
            var = np.random.choice(experiment.vars)
            if len(self.code) == 0:
                self.code = [var]
            else:
                if random.randint(0, 1) == 0:
                    index = random.randint(0, len(self.code) - 1)
                    del self.code[index]
                else:
                    index = random.randint(0, len(self.code))
                    self.code.insert(index, var)

    def execute(self, inpt):
        inpt += self.code

        if 'return' in inpt:
            to_execute = inpt[0:inpt.index('return')]
            try:    exec(' '.join(to_execute))
            except: return 'error'

            to_return = inpt[(inpt.index('return') + 1):]
            to_return = to_return[:to_return.index(';')] if ';' in to_return else to_return
            try:    return eval(' '.join(to_return))
            except: return 'error'
        else:
            return 'error'
