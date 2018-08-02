from experiment import Experiment
from program import Program
from numpy.random import randint

amount = 12

main = Program(amount)
experiment = Experiment(
    main,
    ['a', 'w', 'x', 'y', '*', '/', '-', '+', '=', 'return', ';'],
    lambda: ['w', '=', str(randint(2, 7)), ';', 'x', '=', str(randint(2, 7)), ';', 'y', '=', str(randint(2, 7)), ';'],
    'w * x + y',
    5
)

main.run(experiment)
