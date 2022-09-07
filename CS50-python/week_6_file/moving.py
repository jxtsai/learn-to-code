import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
# 將 command line 放入的圖片檔案參數存成一個列表 list 

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)

#Image.save() method, append_images, durataion, loop 似為此 method 之非必要參數