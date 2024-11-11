import exifread
import json
#Example Photo: "https://raw.githubusercontent.com/ianare/exif-samples/master/jpg/gps/DSCN0042.jpg"

photoFile = "photoTest.jpg"

# Open image file for reading (binary mode)
f = open(photoFile, 'rb')

# Return Exif tags
tags = exifread.process_file(f)
print(tags)

#Tags to look for 
# 'GPS GPSLatitudeRef', 'GPS GPSLongitudeRef'
