from experiment import Experiment
from program import Program
from numpy.random import randint

amount = 12

# If we want to load agents from a file in 'saved_agents/' we can use the
# following line
'''
main = Program(amount, 'test')
'''

# If not, we use the regular one
main = Program(amount)

experiment = Experiment(
    main,
    ['a', 'w', 'x', 'y', '*', '/', '-', '+', '=', 'return', ';'],
    lambda: ['w', '=', str(randint(2, 15)), ';', 'x', '=', str(randint(2, 15)), ';', 'y', '=', str(randint(2, 15)), ';'],
    'w * x + y',
    5
)

main.run(experiment)
