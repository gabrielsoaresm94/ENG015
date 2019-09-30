import matplotlib.pyplot as plt
import numpy as np    # only for dummy data

X,Y = np.mgrid[-2:3,-2:3]
Z = np.random.rand(*X.shape)
FIGSIZE = (2,3)

plt.figure(figsize=FIGSIZE)
mpb = plt.pcolormesh(X,Y,Z,cmap='viridis')

# plot a colorbar into the original to see distortion
plt.colorbar()
plt.savefig('plot_withcbar.png')
