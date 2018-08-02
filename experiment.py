import copy

class Experiment:
    def __init__(self, vars, inpt, output):
        self.vars = vars
        self.inpt = inpt
        self.output = output

    def generate_input(self):
        inpt = self.inpt()
        self.last_inpt = copy.deepcopy(inpt)
        return inpt

    def fitness(self, output, code):
        print (' '.join(self.last_inpt))
        exec(' '.join(self.last_inpt))
        correct_output = int(eval(self.output))
        if 'error' in str(output):
            if '1' in output:
                fitness = -3
            if '2' in output:
                fitness = -2
            if '3' in output:
                fitness = -4
        else:
            fitness = 1/((correct_output - output) ** 2 + 0.0000000001)

        return fitness - len(code) / 5
