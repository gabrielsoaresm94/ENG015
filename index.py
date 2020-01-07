from PIL import Image
from matplotlib import colors
import imageio
import rasterio
import numpy
import matplotlib.pyplot as plt
import glob, os

band4 = rasterio.open('./input/2013_07_03_B5_B4.tif') #red
band5 = rasterio.open('./input/2013_07_03_B5_B5.tif') #nir

#number of raster rows
band4.height

#number of raster columns
band4.width

#plot band 
plt.show(band4)

#type of raster byte
band4.dtypes[0]

#raster sytem of reference
band4.crs

#raster transform parameters
band4.transform

#raster values as matrix array
band4.read(1)

#multiple band representation
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
plt.show(band4, ax=ax1, cmap='Blues') #red
plt.show(band5, ax=ax2, cmap='Blues') #nir
fig.tight_layout()

#generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')

nir

#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi=np.where(
    (nir+red)==0., 
    0, 
    (nir-red)/(nir+red))
ndvi[:5,:5]

print(ndvi)
# # Opens a image in RGB mode  
# im = Image.open(filename)  
# print(im.indexes)  
# # Size of the image in pixels (size of orginal image)  
# # (This is not mandatory)  
# width, height = im.size  
# print(width)
# print(height)
# # Setting the points for cropped image  
# left = 1750
# top = 2900
# right = 3000
# bottom = 4000
  
# # redimensionamento da imagem, para abranjir apenas Salvador/BA
# img = im.crop((left, top, right, bottom))
# img.save("{}/resizes.tif".format(save))  


# # selecionando as Bands 3 e 4, espectros Vermelho e Infravermelho
# with rasterio.open("./output/resizes.tif") as src:
#     band_red = src.read(3)
# with rasterio.open("./output/resizes.tif") as src:
#     band_nir = src.read(4)
# # Do not display error when divided by zero 
# numpy.seterr(divide='ignore', invalid='ignore')

# # Calculating NDVI
# ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)

# min=numpy.nanmin(ndvi)
# max=numpy.nanmax(ndvi)
# mid=0.1

# fig = plt.figure(figsize=(20,10))

# ax = fig.add_subplot(111)
# cbar_plot = ax.imshow(ndvi, cmap='gray', vmin=min, vmax=max)
# ax.axis('off')
# ax.set_title('Normalized Difference Vegetation Index', fontsize=17, fontweight='bold')
# cbar = fig.colorbar(cbar_plot, orientation='horizontal', shrink=0.65)

# if not os.path.exists(save):
#     os.makedirs(save)
 
# fig.savefig("{}/ndvi_size#3.png".format(save))

plt.show()  