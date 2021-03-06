import numpy as np

import cga

import pickling_ga
from search_space_reimpl import search_space


folder = 'experiments/'

# Set up evaluation
population_size = 20

epochs = 60


def const_epochs_60(individual, gen_index, prev_evaluations):
    return epochs


def create_individual():
    return cga.CNN.random_approach3(
        input_shape=data.example.shape,
        num_classes=data.num_classes,
        search_space=search_space
    )


# original paper
learning_rate_decay_points = [1, 149, 249]

relative_decay_points = [i/350 for i in learning_rate_decay_points]
# parse that to out number of epochs
learning_rate_decay_points = [int(np.ceil(i * epochs))
                              for i in relative_decay_points]


data = cga.CIFAR10()

pickling_ga.run('approach-3__', data, folder,
                population_size=population_size,
                search_space=search_space,
                epoch_fn=const_epochs_60,
                learning_rate_decay_points=learning_rate_decay_points,
                create_individual=create_individual
                )
