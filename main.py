import itertools
import numpy as np
from agent import Agent
from mnist_task import Task
from evolution import Evolution

pop_size = 8
batch_size = 4
sizes = [784, 30, 10]
train_iterations = 100
test_iterations = 10

all_params = pop_size * [{
	'weights': [np.random.randn(m, n) for m, n in zip(sizes[1:], sizes)],
	'biases': [np.random.randn(m, 1) for m in sizes[1:]],
	'learning_rate': .1,
	'regularization': .01
}]

task = Task(batch_size)
evolution = Evolution()

for i in itertools.count():
	agents = [Agent(params['weights'], params['biases'], params['learning_rate'], params['regularization']) for params in all_params]

	for j in range(train_iterations):
		x, y = task.train_input()
		costs = [np.average(a.costs) for a in agents]
		print ('Ite {}: Avg cost: {}. Best cost {}'.format(j, np.average(costs), max(costs)))
		for agent in agents: agent.train(x, y)

	for _ in range(test_iterations):
		x, y = task.test_input()
		for agent in agents: agent.test(x, y)

	fitnesses = [np.average(a.accuracies) for a in agents]
	print ('Gen {}: Avg fitness: {}. Best fitness {}'.format(i, np.average(fitnesses), max(fitnesses)))
	data = [[f, p] for f, p in zip(fitnesses, all_params)]
	all_params = evolution.update(data)
	
