#CS50 python week_7
- Date : Setp 12th ~ 31th
- https://cs50.harvard.edu/python/2022/weeks/7
- 中文導讀

## 本週目標
- Regular Expressions
-  
- 

## Content:  104 mins

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

## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-09-14
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
1. Groups and Backreferencing
其語法為利用 () 包裹住條件要素，並搭配 Repetition Quantifiers("?", " *", " +")  
 
2. Alternation
利用 | (pipe 符號)與 groups 功能一起使用
ex /gr(a|e)y/ => gray 或 grey 皆符合 

3. Nested alternation: alternation within alternation
(toyota(turis|corona)|honda(civic|nests))

4. Non Capturing groups 

Assertions Lookaround
- Positive Lookahead Assertion
- Negative Lookahead Assertion
- Positive Lookbehind Assertion
- Negative Lookbehind Assertion