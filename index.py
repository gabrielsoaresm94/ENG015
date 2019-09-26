import imageio

from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import glob, os

first = plt.imread('./input/copy.jpg','JPEG')
second = plt.imread('./input/camp.png')

save = "output"

dims = np.shape(first)
print(dims)
print(np.min(first), np.max(first))
pixel_matrix = np.reshape(first, (dims[0] * dims[1], dims[2]))
print(np.shape(pixel_matrix))

_ = plt.hist2d(pixel_matrix[:,1], pixel_matrix[:,2], bins=(50,50))

if not os.path.exists(save):
    os.makedirs(save)

plt.imsave("./{}/image_new.jpg".format(save), first[:,:,2] - first[:,:,1])
plt.imsave("./{}/image_new2.jpg".format(save), second[:,:,2] - second[:,:,1])

plt.show()
plt.close()