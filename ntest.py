from matplotlib import colors
import rasterio
import numpy
import matplotlib.pyplot as plt
import glob, os

save = "./output"

# Extracting the data from the red and near-infrared bands

# filename = './input/camp.png' # Problem with PNG
filename = './input/landsat.tif'

# Esta imagem tem apenas 3 band, portanto selecionei o index, dos últimos

with rasterio.open(filename) as src:
    band_red = src.read(2) # change for 2 
with rasterio.open(filename) as src:
    band_nir = src.read(3) # change for 3

# Calculating NDVI
# Do not display error when divided by zero 

numpy.seterr(divide='ignore', invalid='ignore')

# NDVI 
ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
print(ndvi)
print(numpy.nanmin(ndvi)) 
print(numpy.nanmax(ndvi))

# get the metadata of original GeoTIFF:
meta = src.meta
print(meta)

# get the dtype of our NDVI array:
ndvi_dtype = ndvi.dtype
print(ndvi_dtype)

# set the source metadata as kwargs we'll use to write the new data:
kwargs = meta

# update the 'dtype' value to match our NDVI array's dtype:
kwargs.update(dtype=ndvi_dtype)

# update the 'count' value since our output will no longer be a 4-band image:
kwargs.update(count=1)

# Finally, use rasterio to write new raster file 'data/ndvi.tif':
# with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
#     dst.write(ndvi, 1)
# ?
class MidpointNormalize(colors.Normalize):
   
    def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
        self.midpoint = midpoint
        colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
       
        x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
        return numpy.ma.masked_array(numpy.interp(value, x, y), numpy.isnan(value))

# Set min/max values from NDVI range for image

min=0.2 # min=numpy.nanmin(ndvi)
max=0.3 # max=numpy.nanmax(ndvi)

# Set our custom midpoint for most effective NDVI analysis
mid=0.1

# Setting color scheme ref:https://matplotlib.org/users/colormaps.html as a reference
colormap = plt.cm.RdYlGn
norm = MidpointNormalize(vmin=min, vmax=max, midpoint=mid)
fig = plt.figure(figsize=(20,10))

ax = fig.add_subplot(111)

# Use 'imshow' to specify the input data, colormap, min, max, and norm for the colorbar
cbar_plot = ax.imshow(ndvi, cmap=colormap, vmin=min, vmax=max, norm=norm)

# Turn off the display of axis labels 
ax.axis('off')

# Set a title 
ax.set_title('Normalized Difference Vegetation Index', fontsize=17, fontweight='bold')

# Configure the colorbar
cbar = fig.colorbar(cbar_plot, orientation='horizontal', shrink=0.65)

# Call 'savefig' to save this plot to an image file
if not os.path.exists(save):
    os.makedirs(save)

fig.savefig("{}/ndvi-image.png".format(save), dpi=200, bbox_inches='tight', pad_inches=0.7)

# let's visualize
plt.show()