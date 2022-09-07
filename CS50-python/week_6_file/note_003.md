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


### Date 2022-09-06
昨天一連看了 CS50 Python week5~ week6 兩週的課堂筆記。Week5 的主題是 unit test, Week6 的內容則是 file I/O。

程式中之所以需要運用到 file，是因為檔案可以將"資料"儲存起來，以節省重覆 input 的麻煩。未學會 file 之前所學到的程式，其輸入值只是暫存在記憶體，一旦執行完畢就會消失。

自己過去在 file I/O 的章節曾被跘住好幾次，可以說是我的心魔之一。昨天先試著復習了 open()/ close() method 的用法與需要參數，再了解另一種透過 "with" + open() method 的寫法

1. file open() syntax : traditional one
   file = open("filename.txt", "w") 
   (file is variable name, open method first arguement is the file to open, its path; the second arguement is the mode of file for manupulation)

2. file open() syntax : "with" keyword
    with open("filename.txt, "w") as file: 
    note there is a code block after this statement ("colon" mark after the variable)	

一般在介紹 file I/O  通常會以 txt / csv 檔案作示範。txt 純文字檔較單純(?)，CSV 則可進一步轉化為欄列形態的試算資料。且 python 還有一個 csv library, 其中有一些好用的功能如 
reader(), DictReader(), writer(), DictWriter() 


#### csv

試著練習 csv library 裏頭的一些 method(), 以下是利用 writer() 把資料寫入檔案 new.csv 

但 writer() 的不便是寫入的資料會變成被逗號分開的字元(delimited strings)


```
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("new.csv", "a" ,delimiter=' ') as new_file:
     new_obj = csv.writer(new_file)
     new_obj.writerow(name)

```

改用另一個 DictWriter() 試試:

```
import csv
name = input("What's your name? ")
home = input("Where's your home? ")

with open("new.csv", "a") as new_file:
     new_obj = csv.DictWriter(new_file, fieldnames =["name", "home"])
     new_obj.writerow({"name": name, "home": home})

```
較之 csv.writer(), csv.DictWriter() 多了一個 fieldnames 參數, 看起來它存放的是 dictionary 的 key



#### Binary Files
除了 txt, csv 純文字格式的檔案, 如何 I/O 其它檔案格式，除了繼續借重 open()/ close() method , 可能還要他方的 library 資源。

## project
 

## supplement reading 



