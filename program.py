import time
import copy
from agent import Agent

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
            #self.agents[i].mutate(experiment)
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
                self.cut(experiment)
                i = 0
            else:
                i += 1

            j += 1

    def cut(self, experiment):
        half = int(self.agents_amount / 2)
        self.agents = self.agents[:half]
        for x in range(half):
            new_agent = copy.deepcopy(self.agents[x])
            new_agent.mutate(experiment)
            self.agents.append(new_agent)

    def stop(self):
        time.sleep(10000000)
