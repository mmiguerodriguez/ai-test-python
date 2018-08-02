import numpy as np
import random
import time
import copy

class Agent:
    def __init__(self, code):
        self.code = code
        self.fitness = 0

    def run(self, experiment):
        inpt = copy.deepcopy(experiment.inpt)
        output = self.execute(inpt)
        self.fitness = experiment.fitness(output, self.code)

    def mutate(self, experiment):
        for _ in range(random.randint(0, 3)):
            word = np.random.choice(experiment.vars)
            if len(self.code) == 0:
                self.code = [word]
            else:
                if random.randint(0, 1) == 0:
                    index = random.randint(0, len(self.code) - 1)
                    del self.code[index]
                else:
                    index = random.randint(0, len(self.code))
                    self.code.insert(index, word)

    def execute(self, inpt):
        inpt += self.code

        if 'return' in inpt:
            to_execute = inpt[0:inpt.index('return')]
            try:
                exec(' '.join(to_execute))
            except:
                return 'error 1'

            to_return = inpt[(inpt.index('return') + 1):]
            to_return = to_return[:to_return.index(';')] if ';' in to_return else to_return
            try:
                return eval(' '.join(to_return))
            except:
                return 'error 2'
        else:
            return 'error 3'

class Experiment:
    def __init__(self, vars, inpt, output):
        self.vars = vars
        self.inpt = inpt
        self.output = output

    def fitness(self, output, code):
        if 'error' in str(output):
            if '1' in output:
                fitness = 2
            if '2' in output:
                fitness = 1
            if '3' in output:
                fitness = 0
        else:
            fitness = 1/((self.output - output) ** 2 + 0.0000000001)

        return fitness - len(code)

class Program:
    def __init__(self, agents_amount):
        self.agents = []
        self.agents_amount = agents_amount

    def startup(self):
        for x in range(self.agents_amount):
            agent = Agent([]);
            self.agents.append(agent)

    def run(self, experiment):
        if len(self.agents) == 0:
            print('Did you forget to call Program.startup()?')
            time.sleep(100000)

        i = 0
        j = 0

        while(True):
            self.agents[i].mutate(experiment)
            self.agents[i].run(experiment)

            print('----- Agent information -----')
            print('Fitness: ' + str(self.agents[i].fitness))
            print('Code: ' + str(self.agents[i].code))
            print('\n')

            if self.agents[i].fitness > 10:
                print('Total iterations = ' + str(j))
                self.stop()

            if i == self.agents_amount - 1:
                self.agents.sort(key=lambda x: x.fitness, reverse=True)
                self.cut()
                i = 0
            else:
                i += 1

            j += 1

    def cut(self):
        half = int(self.agents_amount / 2)
        agents = self.agents[:half]

        for x in range(half):
            new_agent = copy.deepcopy(self.agents[x])
            self.agents.append(new_agent)

    def stop(self):
        time.sleep(10000000)

amount = 6

experiment = Experiment(
    ['a', 'w', 'x', 'y', '*', '/', '-', '+', '=', 'return', ';'],
    ['w', '=', '2', ';', 'x', '=', '3', ';', 'y', '=', '7', ';'],
    2 * 3 + 7
)

main = Program(amount);
main.startup();
main.run(experiment);
