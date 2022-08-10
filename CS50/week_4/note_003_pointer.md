#CS50 week_3
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
### Date 2022-08-10
回家看了 week4 short video pointers 後半部，對於 pointer 的觀念還是很混亂。昨天下午看了一點 Standford Computer Science 入門課程的輔助文件 [Pointers and Memory](http://cslibrary.stanford.edu/102/) , 它多少對觀念的釐清是有幫助的。但這份文件有點過長，我的專注力大概只到 pointers section。

臨睡前想到，不如找找油管上是否有高人氣的講解影片。如果找到一支"[you will never ask about pointers again after watching this video](https://www.youtube.com/watch?v=2ybLD6_2gKM)" ，至少把 memory( address, value, name) , \*pointer , \*dereference 二種不同的意義解釋地更為清楚。

- \*  用在 datatype 之後，仍是作為宣告後面緊接著的變數是一個 pointer,它的值是指向記憶體中某處位置
- \*  用在變數前(而非宣告)則是一個 operator , 應用在 dereference , 也就是把 = 左側的變數設定其值為  \*pointer 所指向位置上的值 value

經過這番掙扎後，似乎比較更能掌握 pointer 要指向何處，它所要引用的值是哪個

弄清楚這些 \*  符號，多少讓我更有信心繼續跟上後面的課程。

week4 課堂影片最後三十分鐘的內容(file, bitmap, pixel/ wav editing....) David 上得很快，恐怕要靠自己多讀"課本"或其它教材再做練習題才會怪怪熟練。因此找了 CS50 課堂的指定教科書來看看，分別是:
- Hacker's Delight
- How Computers Work
- Programming in C 
這幾本書都可以在 github 找到 

#### File handling in C
some function for file operations 



## project
### Date 2022-08-10
Lab : wav file Volume change
前一週 runoff 的作業還沒完成，想讓自己轉換一下心情先看看 week4 Lab 內容。 CS50 lab 其實是 problem set 的先導暖身預熱，作完 lab 就能更從容地面對 problem 習題。 lab 先從聲音檔 wav 的音量調整開始，problem 則會進入到 bitmap, jpg 照片像素色盤(RGB) 的調整。

不過自己似乎還未完全明白 file 這部份，得先熟悉 file 相關 function 函數如何使用以及 Pointer 在其中扮演的角色吧。慢慢來，別太心急。


## supplement reading 

- 
## todo list for 08/10 evening
- week3 problem set runoff walkthrough
- shorts : call stack, file pointer (reviewing pointers)

