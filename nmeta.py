from osgeo import gdal

filename = './input/landsat.tif'

dataset = gdal.OpenEx(filename)
md = dataset.GetRasterBand(1).GetStatistics(0,1)
add = dataset.AddBand(11) # GDALDataType eType, char **papszOptions = nullptr
multi = dataset.RasterIO(GDALDataType=11)
print(md)
print(add)
print(multi)

dataset = gdal.OpenEx(filename)
md = dataset.GetMetadata('IMAGE_STRUCTURE')

# Use dict.get method in case the metadata dict does not have a 'COMPRESSION' key
compression = md.get('COMPRESSION', None)

print(md)
# {'COMPRESSION': 'LZW', 'INTERLEAVE': 'BAND'}
print(compression)
# LZW

dataset = gdal.OpenEx(filename) #Has no compression
md = dataset.GetMetadata('IMAGE_STRUCTURE')
compression = md.get('COMPRESSION', None)

print(md)
# {'INTERLEAVE': 'BAND'}
print(compression)
# None

# https://gdal.org/tutorials/raster_api_tut.html