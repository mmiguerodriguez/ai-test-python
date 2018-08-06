import numpy as np

class Evolution:
    mutator = Mutator()

    def __init__(self):
        pass

    def update(self, agent_info):
        # Sort by fitness = index 0
        sorted_info = sorted(agent_info, key=lambda x: x[0], reverse=True)

        # Remove half
        half = len(sorted_info) / 2
        sorted_info = sorted_info[:-half]

        # Mutate before duplicating
        for i, (fitness, params) in enumerate(sorted_info):
            # Choose a random layer
            layers = len(params['weights']) + 1
            layer = np.random.randint(0, layers)

            # Generate new weight or biases and replace the information
            weights, biases = mutator.mutate(layer, params['weights'], params['biases'])
            sorted_info[i]['weights'] = weights
            sorted_info[i]['biases'] = biases

        # Duplicate the best
        sorted_info *= 2

        return sorted_info
