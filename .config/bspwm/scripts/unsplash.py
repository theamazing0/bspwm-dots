# Download URL https://source.unsplash.com/collection/1459961/1440x900

import requests
import os

img_data = requests.get('https://source.unsplash.com/collection/1459961/1440x900').content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

os.system("feh --bg-scale image_name.jpg")