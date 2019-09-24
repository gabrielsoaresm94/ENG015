import matplotlib.pyplot as plt
import numpy

fig,ax = plt.subplots(1,1)
image = numpy.array([[1,1,1], [2,2,2], [3,3,3]])
im = ax.imshow(image)

print(fig,ax)
print(image)
print(im)