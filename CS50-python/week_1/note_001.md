#CS50 python week_1
- Date : Aug 25th ~ 31th
- https://cs50.harvard.edu/python/2022/weeks/1
- 中文導讀

## 本週目標
- conditionals
-  
- 

## Content:  144 mins

    Conditionals
    if Statements
    Control Flow, elif, and else
    or
    and
    Modulo
    Creating Our Own Parity Function
    Pythonic
    match
     

## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-08-26

#### match statement for conditionals
match variablename to map its cases



## project
### probem set  Deep Thought

conditionals : if / else "and" "or"  
```
def main():
    
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    if answer == "42" or answer == "forty-two" or answer == "forty two" :
        print("Yes")
    else:
        print("No")


main()

```

### probem set  Home Federal Savings Bank

1. conditionals : if , elif, or and 
2. find() method for string : return first argument position in the string 

```
greeting = input("Greeting: ")

    if greeting.find("Hello") == 0 or greeting.find("hello") == 0:
        print("$0")
    elif greeting.find("H") == 0 or greeting.find("h") == 0:
        print("$20")
    else:
        print("$100")
```
### probem set File Extensions

1. check file's extenion string and reply its type
 string method : 利用 split() 抽取出副檔名
2. match case == 只能在 python 3.10  以上環境使用

```
file_name = input("File name:  ")
    hello = file_name.split(".")[1]
    print(hello)

    match hello :
       case "jpg" | "jpeg":
          print("image/jpeg")
       case "gif":
          print("image/gif")
       case "pdf":
          print("application/pdf")
       case "zip":
          print("application/zip")
       case "txt":
          print("text/plain")
       case _:
          print("Who?")

```

### probem set  Math Interpreter

1. 同上題, 利用 split() 分割取出 xyz
2. 利用 float() 改變 x, z 之data type
3. 因為無法改變 y string ,只好利用  match case 來應付可能的加減乘除
```
 xyz = input("Expression: ")
    x = float(xyz.split(" ")[0])
    y = xyz.split(" ")[1]
    z = float(xyz.split(" ")[2])

    match y:
       case "*":
          print(x*z)
       case "+":
           print(x+z)
       case "-":
          print(x-z)
       case "/":
           print(x/z)


```
### probem set  Meal Time

## supplement reading 



