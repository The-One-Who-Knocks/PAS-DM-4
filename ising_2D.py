# -*- coding: utf-8 -*-

import numpy as np
import pylab as plt

np.random.seed(2)

def energy(i, j, config):
    """ Function which determines the energy """
    size = len(config)
    return -config[i,j]*(config[(i+1) % size, j] + config[(i-1) % size, j] +
                         config[i, (j+1) % size] + config[i, (j-1) % size])
                         
# Parameters of the simulation

L = 25          # Grid size
N = L**2        # Number of spins

beta = 0.0000001        # beta = 1/T : we work in units of k

dt = 1/N        # Time mesh
t_f = 1000000     # Final time

config = np.full((L,L), 1, dtype='int')
plt.imshow(config, cmap = 'Blues', interpolation='nearest')
plt.show()

for t in range(t_f):
    flip_i, flip_j = np.random.randint(0, L, size=2, dtype='int')
    delta_E = -2. * energy(flip_i, flip_j, config) 
    if delta_E <= 0:
        config[flip_i, flip_j] *= -1
    elif np.exp(-beta*delta_E) > np.random.uniform():
        config[flip_i, flip_j] *= -1

plt.imshow(config, cmap = 'Blues', interpolation='nearest')
plt.show()


