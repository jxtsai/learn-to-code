#CS50 python week_6
- Date : Setp 5th ~ 31th
- https://cs50.harvard.edu/python/2022/weeks/6
- 中文導讀

## 本週目標
- File input/ putput
-  
- 

## Content:  104 mins

    File I/O
    open
    with
    CSV
    Binary Files and PIL
    Summing Up

     

## 完成進度
請登入 https://app.blitz.do/



## my notes


### Date 2022-09-07
昨天看了關於 python file I/O CSV 格式後，今天繼續往下讀 binary file，電腦可讀的二元格式檔案，binary file 可儲存的格式就很多了，但人腦不一定能直覺地吸收。

#### Binary Files
除了 txt, csv 純文字格式的檔案, 如何 I/O 其它檔案格式，除了繼續借重 open()/ close() method , 可能還要他方的 library 資源。CS50 Python 課堂上提供的案例是 PIL 來讀取 GIF 檔案

```
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

```

查了一下 PILLOW 的資源文件，Image.save() 支援的參數功能主要還是和圖片格式有關. GIF 檔案就含有更多的 para ,諸如: background, transperency, version , duration, loop, comment, extenstion 等等
https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html


## project
 

## supplement reading 



