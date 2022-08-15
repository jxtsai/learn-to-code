#CS50 week_4
- Date : Agust6th ~ August 21th
- https://cs50.harvard.edu/x/2022/weeks/4/
- 中文導讀

## 本週目標
- pointers
- 

## Content:  145 mins
### Memory /pointer / address



## 完成進度
請登入 https://ticktick.com

## my notes
### Date 2022-08-08
週一上班日，在辦公室裏整理筆記與寫心得日記其效率明顯高出週末在家裏。不過稍回顧一下目前筆記的分類與記錄方式，實在非常雜亂，而且還攪入了不明不白的 git control 操作，除把兩部設備上的檔案作一番統整同步外，還得想想該怎麼段落分割，架構出更清楚的系統脈絡。

上午開始讀 week4 的課堂筆記。雖然上週末先看過近一半的講座影片，但對於其中提到的 pointer 觀念還是不夠清楚，今天勉強讀完筆記，依舊是一知半解，第一次覺得看不太懂筆記，好想看 David 的講座會如何 present 這部份的內容。

根據課堂筆記: pointer 的定義
**** A pointer is a variable that stores an address in memory, where some other variable might be stored **** 
故當使用 \* operator, 即表示它(變數)代表記憶體裏頭一個位置，而這個位置可能有其它變數。\* operator 又被叫作"dereference operator", 至該位置去取得其所儲放的"值"(goes to an address to get the value stored there)

而另一個 other "&"則是用於取得變數其記憶體位置的符號(used to get the address of some variable)

```
char *s = get_string("s :  \n");
```
***get_string()*** function (by CS50.h) a function retrun the pointer of first charactor of the string
 

**** Memory allocation ****
malloc() function: a function to allocate some ****number of bytes in memory****.  

**** valgrind ****
command line tool helps to check the program  if  any memory-related issues.



## project
### Date 2022-08-08
週末在習題作業的進展為零。本週雖然繼續跟著 week4 課堂影片跑，但作業完成度已開始出現落後，就算追不上齊步也不能丟下反正最後到終點沒人在意完成的時間是否打破記錄。

 


