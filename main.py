from experiment import Experiment
from program import Program
from numpy.random import randint

amount = 6

experiment = Experiment(
    ['a', 'w', 'x', 'y', '*', '/', '-', '+', '=', 'return', ';'],
    lambda: ['w', '=', str(randint(2, 10)), ';', 'x', '=', str(randint(2, 10)), ';', 'y', '=', str(randint(2, 10)), ';'],
    'w * x + y'
)

main = Program(amount);
main.startup();
main.run(experiment);
