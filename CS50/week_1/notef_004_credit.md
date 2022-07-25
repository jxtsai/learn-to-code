#CS50 week_1
- Date : July 21th ~ 31th
- https://cs50.harvard.edu/x/2022/weeks/1/
- 中文導讀

## 本週目標
- C 語言
- review scratch
- 

## Content:  148 mins
    C
    IDEs, compilers, interfaces
    Functions, arguments, return values, variables
    main, header files, commands
    Types, format codes, operators
    Variables, syntactic sugar
    Calculations
    Conditionals, Boolean expressions
    Loops, functions
    Mario
    Imprecision, overflow


## my notes
### Date 2022-07-25 
檢查信用卡卡號是否有效

1. 先辨別發卡公司為哪家
- American Express : 15位 起頭為 34 or 37
- Master: 16位 起頭為 51 ~ 55
- Visa 起頭為 4

2. Luhn’s Algorithm 檢查法
偶位數總合  * 2 
奇位數總合 * 1
二者相加 個位數是否為 0

3. loop ? + conditionals