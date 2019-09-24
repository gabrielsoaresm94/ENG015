import imageio

from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import glob, os

first = plt.imread('./files/copy.jpg','JPEG')
second = plt.imread('./files/camp.png')

dims = np.shape(first)
print(dims)
print(np.min(first), np.max(first))
pixel_matrix = np.reshape(first, (dims[0] * dims[1], dims[2]))
print(np.shape(pixel_matrix))

_ = plt.hist2d(pixel_matrix[:,1], pixel_matrix[:,2], bins=(50,50))
plt.imshow(first)
plt.imshow(second)
# plt.savefig(first)

# plt.savefig("%s.png"%first)
# "%s.png" % os.path.join("./files", name)
plt.imsave('image_new.jpg', second)

plt.show()
plt.close()