#CS50 python week_7
- Date : Setp 12th ~ 31th
- https://cs50.harvard.edu/python/2022/weeks/7
- 中文導讀

## 本週目標
- Regular Expressions
-  
- 

## Content:  104 mins
Regular Expressions Basic I
- Regular Expression Syntax
- Literal Characters
- Modes
- Metacharacters
- Metacharacters II

Regular Expressions Basic II
- More Metacharacters
- Wild Card or period
- Non Printable Characters
   
     

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
Regular Expressions  基本語法:
- Regular Expression Syntax 利用前後兩個 forward slash / / 夾住，中間即為 RE 元素組成
- Literal Characters: 按字面可直接解讀的字母、數字 (letters, digits)
- Modes 第二個 forward slash 後跟著出現的英文小寫 g, i, m, s 分別代表: global 全域、 i (case insensitive 忽略大小寫)、多行、單行等 RE之模式。 
- Metacharacters 元字符(aka symbol)，在 RE 中具有特別作用的字符: \ ^ | . $ ? * + () [] {} 
  例如 \ backslash  即表示 escape, 而 \ 與下列字母一起則有特別表示作用(Shorthand Character Classes)
  \d    decimal digit 任何數字
  \D    not a decimal digit 任何不是數字的字符
  \s    whitespace characters 
  \S    not a whitespace character
  \w    word character, as well as numbers and the underscore 除了 metacharacters, non-printable characters 以外的字符
  \W    not a word character
  \t    matches a tab character only
 上述字母大小寫正好表示"相反"的東西 
  
Basic II
- More Metacharacters
- Wild Card or period  "." 可代表任何字符(literal character/ metacharacters)
- Non Printable Characters: 空白 whitespace、新行 new line、tab.... 無法顯示看出但仍佔 byte 之字符