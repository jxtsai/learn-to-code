#CS50 python week_0
- Date : Aug 25th ~ 31th
- https://cs50.harvard.edu/python/2022/weeks/0
- 中文導讀

## 本週目標
- variables  
- function
- 

## Content:  144 mins

    Creating Code with Python
    Functions
    Bugs
    Improving Your First Python Program
        Variables
        Comments
        Pseudocode
    Further Improving Your First Python Program
    Strings and Paremeters
        A small problem with quotation marks
    Formatting Strings
    More on Strings
    Integers or int
    Readability Wins
    Float Basics
    More on Floats
    Def
    Returning Values
    Summing Up

## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-08-26


## project
### probem set 1 indoor vocie

string method lower()/upper() 
```
user = input("")
print(f"{user.lower()}")

```

### probem set 2 Playback Speed

string replace() method
https://www.w3schools.com/python/ref_string_replace.asp


### probem set 3 Making Faces

1. function and str mehtod (replace())
2. emoji 
3. conditionals 

```
def covert(sth):
    if ":(" in sth: 
        x = sth.replace(":(", "🙁")
    
    elif ":)" in sth:
        x = sth.replace(":)", "🙂")

    return x

user = input("")
x = covert(user)
print(x)
```

### probem set 3 Tip Calculator

1. function
2. type convert str, int, float
```

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d)


def percent_to_float(p):
    return float(int(p)/100)


main()


```

## supplement reading 



