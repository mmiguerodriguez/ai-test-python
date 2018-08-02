import time
import copy
from agent import Agent
import numpy as np
import random
import itertools

class Program:
    def __init__(self, agents_amount):
        self.agents_amount = agents_amount
        self.agents = [Agent([]) for _ in range(self.agents_amount)]

    def run(self, experiment):
        i = 0
        j = 0

        while True:
            self.agents[i].run(experiment)
            if j % 1000 == 0:
                print('----- Agent information -----')
                print('Fitness: ' + str(self.agents[i].fitness))
                print('Code: ' + str(self.agents[i].code))
                print('\n')
                time.sleep(1)

            if self.agents[i].fitness > 18.7:
                print('----- Agent information -----')
                print('Fitness: ' + str(self.agents[i].fitness))
                print('Code: ' + str(self.agents[i].code))
                print('\n')
                print('Total iterations = ' + str(j))
                self.stop()

            if i == self.agents_amount - 1:
                self.agents.sort(key=lambda x: x.fitness, reverse=True)
                self.cut_2(experiment)
                for agent in self.agents: agent.fitness = 0
                i = 0
            else:
                i += 1

            j += 1

    def cut(self, experiment):
        half = int(self.agents_amount / 2)
        self.agents = self.agents[:half]
        new_agents = []
        for x in range(half):
            new_agent = copy.deepcopy(self.agents[x])
            new_agent.mutate(experiment)
            new_agents.append(new_agent)
        self.agents += new_agents

    def cut_2(self, experiment):
        half = int(self.agents_amount / 2)
        new_agents = []

        for _ in range(half):
            fitnesses = np.array(sorted([a.fitness for a in self.agents], reverse=True))
            fitnesses -= np.amin(fitnesses) if np.amin(fitnesses) < 0 else 0
            probs = fitnesses / np.sum(fitnesses)
            parent1 = np.random.choice(self.agents, p=probs)
            parent2 = np.random.choice(self.agents, p=probs)
            new_agent = Agent(self.crossover(parent1.code, parent2.code))
            new_agent.mutate(experiment)
            new_agents.append(new_agent)

        self.agents = self.agents[:half] + new_agents

    def crossover(self, c1, c2):
        self.slices = 2
        if len(c1) != 0 and len(c2) != 0:
            slices = min(self.slices - 1, len(c1) - 1, len(c2) - 1)
            c1_ix = sorted([0, len(c1)] + random.sample(range(1, len(c1)), slices))
            c2_ix = sorted([0, len(c2)] + random.sample(range(1, len(c2)), slices))

            c1_slices = [c1[i:j] for i, j in zip(c1_ix, c1_ix[1:])]
            c2_slices = [c2[i:j] for i, j in zip(c2_ix, c2_ix[1:])]
            all_slices = [[w1, w2] for w1, w2 in zip(c1_slices, c2_slices)]

            new_code = [s1 if random.randint(0, 1) == 0 else s2 for s1, s2 in all_slices]
            return list(itertools.chain(*new_code))
        elif len(c1) != 0:
            return c1
        else:
            return c2


    def stop(self):
        time.sleep(10000000)
