import numpy as np
from mutator import Mutator

class Evolution:
    mutator = Mutator()

    def __init__(self):
        pass

    def update(self, agent_info):
        # Sort by fitness = index 0
        sorted_info = sorted(agent_info, key=lambda x: x[0], reverse=True)
        all_params = [params for _, params in sorted_info]

        # Remove half
        half = int(len(all_params) / 2)
        all_params = all_params[:-half]

        # Mutate before duplicating
        for i, params in enumerate(all_params):
            # Choose a random layer
            layers = len(params['weights'])
            layer = np.random.randint(1, layers)

            # Generate new weight or biases and replace the information
            weights, biases = self.mutator.mutate(layer, params['weights'], params['biases'])
            all_params[i]['weights'] = weights
            all_params[i]['biases'] = biases

        # Duplicate the best
        all_params *= 2

        return all_params
