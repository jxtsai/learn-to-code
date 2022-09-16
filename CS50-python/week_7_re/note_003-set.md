#CS50 python week_7
- Date : Setp 12th ~ 31th
- https://cs50.harvard.edu/python/2022/weeks/7
- 中文導讀

## 本週目標
- Regular Expressions
-  
- 

## Content:  104 mins

Characters Set in Regular Expressions
- Character Set or Character Class
- Character Range
- Negating a Character Set
- Metacharacter inside Character Set
- Shorthand Character Classes

Repetition with Quantifiers
- Quantifiers
- Limiting Repetition
- Greedy Nature
- Lazy Regex

Anchors and Boundary
- Anchors
- Boundary

## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-09-13
這篇筆記是整理自三個月前聽網路課 [Complete Regular Expressions Bootcamp - Go from Zero to Hero](https://www.udemy.com/course/learn-regular-expressions-in-online-regex-course/)
 介紹 regular expression 的內容。當時只有手寫版本，如今乾脆把它們打字一起存在 CS50 python week7 regular expression 的資料夾。
 
### RE Bootcamp 課程大綱:
Basic I
- Regular Expression Syntax
- Literal Characters
- Modes
- Metacharacters
- Metacharacters II

Basic II
- More Metacharacters
- Wild Card or period
- Non Printable Characters

Characters Set
- Character Set or Character Class
- Character Range
- Negating a Character Set
- Metacharacter inside Character Set
- Shorthand Character Classes

Repetition with Quantifiers
- Quantifiers
- Limiting Repetition
- Greedy Nature
- Lazy Regex

Anchors and Boundary
- Anchors
- Boundary

Groups and Backreferencing
- Groups capturing and backreferencing
- Alternation
- Nested alternation
- Non Capturing groups 

Assertions Lookaround
- Positive Lookahead Assertion
- Negative Lookahead Assertion
- Positive Lookbehind Assertion
- Negative Lookbehind Assertion

### 筆記整理
1. characters set 字符組合，利用 []來包裹 RE 之表達示，裏頭可以有多重字符，但只要符合其中任可一個即會選中

2. characters ranges: 字符範圍
在字符組合 set [] 中利用 - (hyphen 連字符號)，即可表達"連續"之特殊意義
[A-Ba-z0-9_] ==> /w  
^ (caret 插入記號、脫字符)則表示"反向選取" negative
[^a] ==> 除了 a 以外的字符
[^AB] ==> AB 以外的任何字符

3. 重覆次數，可利用以下三種 metacharacter 來控制重覆次數
? : 0 或 1 次
* : 0 或 1 次以上
+ : 1次或1次以上

4. 利用{} (curly brackets，中文叫花括弧) 限制某些字符出現次數
ex a{4} => aaaa 符合

5. greedy | lazy expressions 
greedy expressions : 符合要件者越多越好，利用 "+" 控制
lazy expressions: 符合條件者越少越好(但至少要有一次符合)，用"?"來控制

6. Anchors 
^ : 其後的 character 需為首
   ^A : 需符合 A在第一個位置
$ : 其前的 character 需為最後的位置
   a$ : a 為最後一個字元

7. Boundary
前後用 \b \b 包夾，中間的pattern 即為需符合之條件且前後無任何字元