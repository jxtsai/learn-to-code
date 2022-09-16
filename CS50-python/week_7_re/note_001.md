#CS50 python week_7
- Date : Setp 12th ~ 31th
- https://cs50.harvard.edu/python/2022/weeks/7
- 中文導讀

## 本週目標
- File input/ putput
-  
- 

## Content:  104 mins

    
    Regular Expressions
    Case Sensitivity
    Cleaning Up User Input
    Extracting User Input
    Summing Up

     

## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-09-12
本週打算進入 CS50 python week7 有關 regular expression 的介紹，中秋假日在家中先重新溫習了一番三個月前學到一半的 regular expression 網路課程。

3
而在 python 裏頭，主要是透過 library "re" 來檢驗搜索文字符號組合的條件，例如在 re.search()此函數中，其放入的參數為: re.search(pattern, string, flags=0)，string 為欲檢查的對象而 pattern 則是放入"常規表達式"字元組合(regular repression)。而最後一個(optional)參數 flags 則有一些常見的內鍵變數如: 
re.IGNORECASE
re.MULTILINE
re.DOTALL


## project

```
import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)
# if the pattern match, re.search() will return an ojbect, otherwise it return None value 

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")

``` 
 

## supplement reading 

1. python documentation about re: https://docs.python.org/3/library/re.html
2. Tutorial video : [Complete Regular Expressions Bootcamp - Go from Zero to Hero](https://www.udemy.com/course/learn-regular-expressions-in-online-regex-course/)
 


