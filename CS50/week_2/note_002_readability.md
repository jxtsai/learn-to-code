#CS50 week_2
- Date : July 26th ~ 31th
- https://cs50.harvard.edu/x/2022/weeks/2/
- 中文導讀

## 本週目標
- C 語言
- 
- 

## Content:  147 mins
 C 語言第二部
    Compiling
    Debugging
    Memory
    Arrays
    Characters
    Strings
    Command-line arguments
    Applications


## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-07-27

今天上午開始作 problem set 習題1 : readability
原本以為"readability" 要討論的是新手寫出來的程式碼，是否易懂好讀等等相關的提示，仔細一讀才知道自己誤會大了，原來還是練習寫程式本身。這題無須應用什麼複雜的演算法，不過就 C語言本身資料型態的轉換(int <-> float...) 自己覺得還是有點頭痛。

整理一下本道習題所會使用到的函數:
1. round (<maht.h>) :方便把浮點數轉化為整數型態
2. ASCII 英文 A-Z(65~90) a-z(97-122)  : 利用
```
int a_as_int = (int) 'a';
```
對應英文字母的 ASCII 代號，以計算文章中使用多少字母
