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
### Date 2022-08-09
昨日白天讀過"兩"遍課堂筆記，有些地方仍未完全理解，期待回家透過 David 在課堂上的講解能讓自己更明白 pointer 在 C 語言的角色，以及程式語言設計和電腦記憶體之間的關係。撐著精神看完 lecture 影片，好像有多了解一點但還不能說是完全明白。這時候心裏又跑出來 OS : C 語言真是一種麻煩的程式， function 不能直接傳回 array 資料型態、變數的資料形態要事先宣告、只有 char 沒有 string (除非直接包含 cs50.h).......但也因為這些麻煩，我們才得以窺見早期電腦硬體效能低的年代，工程師要如何克服重重限制來解決問題。而這些應變能力與創意，也正是面對未來各種挑戰時所必備的基礎功力吧。

正因為之前利用 CS50 library 很方便，沒料理想到原來真正的 C 語言沒有 string 此種 datatype，故用點時間去測試 char array, string in function 等等。在最單純的 C 語言環境中，要宣告 string 的語法之一可為:

```
char *s = "hello";
```
char s = "hello"; 錯誤,無法 compiling
 


之前寫 function, 但不知如何讓它傳回 array, 若包括 cs50.h 則其 string datatype 可以應用在 function return.

#### File handling in C
some function for file operations 
- fopen()
- fclose()
- getc() - reads a character from a file
- putc() - writes a character to a file
- fscanf() - reads a set of data from a file
- fprintf() - writes a set of data to a file
- getw() - reads a integer from a file
- putw() - writes a integer to a file
- fseek() - set the position to desire point
- ftell() - gives current position in the file
- rewind() - set the position to the beginning point


## project
### Date 2022-08-09



## supplement reading 

- [Pointers and Memory](http://cslibrary.stanford.edu/102/)


