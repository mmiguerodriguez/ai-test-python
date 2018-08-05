from nn import NN
class Task:
    batch_size = 128
    epoch_size = 50
    test_runnings = 10000

    def __init__(self):
        self.nn = NN()

    def train(self):
        for _ in range(self.epoch_size):
            indices = np.random.choice(self.train_images.shape[0], self.batch_size)
            batch_X = [self.train_images[i] for i in indices]
            batch_Y = [self.train_labels[i] for i in indices]
            self.nn.sgd(batch_X, batch_Y)
