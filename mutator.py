import numpy as np

'''
mutations:
add_neuron, remove_neuron, modify_weight, modify_bias

USAGE:
mutator = Mutator()
mutator.mutate(layer, weights, biases)
'''

class Mutator:
    def __init__(self):
        pass

    def mutate(self, layer, weights, biases):
        random = np.random.uniform(0, 1)

        if random < 0.25:
            return self.add_neuron(layer, weights, biases)
        elif random < 0.5:
            return self.remove_neuron(layer, weights, biases)
        elif random < 0.75:
            return self.modify_weight(layer, weights), biases
        else:
            return weights, self.modify_bias(layer, biases)

    def add_neuron(self, layer, weights, biases):
        weights[layer - 1] = np.concatenate((
            weights[layer - 1],
            np.random.randn(1, len(weights[layer - 1][0]))
        ))

        weights[layer] = np.append(
            weights[layer],
            [[np.random.randn()] for _ in range(len(weights[layer]))],
            axis=1
        )

        biases[layer - 1] = np.concatenate((
            biases[layer - 1],
            np.random.randn(1, 1)
        ))

        return weights, biases

    def remove_neuron(self, layer, weights, biases):
        weights[layer - 1] = weights[layer - 1][:-1]
        weights[layer] = np.delete(weights[layer], len(weights[layer]) - 1, axis=1)

        biases[layer - 1] = biases[layer - 1][:-1]

        return weights, biases

    def modify_weight(self, layer, weights):
        shape = np.shape(weights[layer])
        new_weights = np.random.randn(shape[0], shape[1])

        if np.random.uniform(0, 1) > 0.5:
            weights[layer] = np.add(weights[layer], new_weights)
        else:
            weights[layer] = np.subtract(weights[layer], new_weights)

        return weights

    def modify_bias(self, layer, biases):
        shape = np.shape(biases[layer])
        new_biases = np.random.randn(shape[0], shape[1])

        if np.random.uniform(0, 1) > 0.5:
            biases[layer] = np.add(biases[layer], new_biases)
        else:
            biases[layer] = np.subtract(biases[layer], new_biases)

        return biases
