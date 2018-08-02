import time
import copy
from agent import Agent

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

            if self.agents[i].fitness > 5:
                print('----- Agent information -----')
                print('Fitness: ' + str(self.agents[i].fitness))
                print('Code: ' + str(self.agents[i].code))
                print('\n')
                print('Total iterations = ' + str(j))
                self.stop()

            if i == self.agents_amount - 1:
                self.agents.sort(key=lambda x: x.fitness, reverse=True)
                self.cut(experiment)
                i = 0
            else:
                i += 1

            j += 1

    def cut(self, experiment):
        half = int(self.agents_amount / 2)
        self.agents = self.agents[:half]
        new_agents = []
        for agent in self.agents:
            new_agent = copy.deepcopy(agent)
            new_agent.mutate(experiment)
            new_agents.append(new_agent)
        self.agents += new_agents

    def stop(self):
        time.sleep(10000000)
