import rasterio
import numpy
import matplotlib.pyplot as plt
from matplotlib import colors

# Extracting the data from the red and near-infrared bands

# filename = './input/camp.png'
filename = './input/landsat.tif'
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