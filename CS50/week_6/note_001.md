#CS50 week_6
- Date : Aug 25th ~ 31th
- https://cs50.harvard.edu/x/2022/weeks/6/
- 中文導讀

## 本週目標
- python
-  
- 

## Content:  144 mins
   
    Python syntax
    Libraries
    Input, conditions
        meow
    Mario
    Documentation
    Lists, strings
    Command-line arguments, exit codes
    Algorithms
    Files
    More libraries

## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-08-25
直接進入 python library 應用，除了 CS50 提供的 cs50 library，第一個用上的是 PIL
Python Imaging Library (PIL)
目前 python 圖像編輯的 library 應是多用 pillow(由 PIL 分叉出來)，其使用文件在:
https://pillow.readthedocs.io/

在課堂案例:

```
from PIL import Image, ImageFilter

before = Image.open("bridge.bmp")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.bmp")


```
ImageFilter, Image 分別為 PIL library 裏頭的二個 modules
而 filter() 為物件(Image object) before 的一種方法(method), 可透過 . 語法來呼叫使用


 

## project


## supplement reading 



