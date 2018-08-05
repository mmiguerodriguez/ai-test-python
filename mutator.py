'''
mutations:
add_neuron, remove_neuron, modify_weight, add_bias, remove_bias, add_link, remove_link
'''

class Mutator:
    add_neuron(self, layer, weights, bias):
        # no manden layer = 0 o we fucked up

        np.concatenate((
            weights[layer],
            np.random.randn('''len(weights[layer][0] ?''', 1) #ugly or as a parameter?
        ))

        np.concatenate((
            bias[layer - 1],
            np.random.randn(1, 1)
        ))
