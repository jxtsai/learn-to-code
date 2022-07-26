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



3. loop ? + conditionals

### Date 2022-07-26
昨天因為 credit card checksum 的解法一直想不出來，只好重新"認真"地看了第一週講座後半段的影片，想說自己是否漏掉錯過了什麼重要的主題、觀念。但看下來一點也沒有直接提到與該題目直接相關的東西，倒是強迫自己看了一些過去一直刻意忽略的東西，例如 C 語言的資料型態以及其所佔用的位元數，為什麼有些資料型態會出現不準確失真的情況.....這些出現在早期低階程式的問題，不復在高階語言。但也正是高階語言的強大與方便(特別是晚期硬體效能的革新)，讓我只想走捷徑看結果而逃避了這整片森林底下的基礎生態。
的確寫 C 語言後麻煩，沒什麼強大的 library, modules, 套件可以直接套用。但也正因為它的樸素，學習者必須從最基本的功夫慢慢練起一個函數一片積木地去建構自己寫出來的世界。
