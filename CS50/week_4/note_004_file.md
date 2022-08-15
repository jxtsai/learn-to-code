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
### Date 2022-08-11
昨天回家先重看了一遍 pointer 短片，老實說助教的解說方式還不是"最頂的"(私以為最佳的介紹當屬 [low level learing 的影片](https://www.youtube.com/watch?v=2ybLD6_2gKM) )。但重看一遍算是確認自己是否真的搞懂了 pointer 的觀念。
接下來的重頭戲則是 file pointers，在大堂講座上沒時間仔細提及的 FILE 等相關函數的作用、使用參數等等，都在短片裏有了基本的介紹，接下來就要應用這些 file functions 與 file pointer 來完成 week4 的 lab 習作與課題(wav files/ jpg files manupluation)
 

#### File handling in C
some function for file operations 
- fopen() : 會傳回一個 file pointer, 需二個參數，第一為欲開啟之檔案，第二為操作模式，如"w", "r", "a"(append)
- fclose(): 只需放入一個參數即欲關閉之已開啟檔案的 file pointer。一定要記得用 fclose 關閉 file pointer，以免造成記憶體問題
- fgetc() - reads a character from a file, 取回 file pointer 所指的第一個字元 character。 其參數為 file pointer。可利用 while != EOF (end of file) loop 取出該檔案全部字元。需注意，所打開的檔案其模式必須為"r" 方可讀取。
- fputc() - writes a character to a file, 寫入字元。其語法為 fputc(<character>, <file pointer>)。需注意，所打開的檔案其模式必須為"w" 方可執行寫入。
- 另有 fgets(), fputs() 用來讀取/寫入 string 
- fscanf() - reads a set of data from a file
- fread() - fread(<buffer>, <size>, <qty>, <file pointer>) 
- fprintf() - writes a set of data to a file
- fwrite() - fwrite(<buffer>, <size>, <qty>, <file pointer>) 

昨天初步練習了 file fopen(), fclose(), 今天來熟悉 fgetc(), fput() 的使用。至於可以一次寫人(讀取)更多資料的 fwrite(), fread(), 還沒完全弄懂它的用法。

## project
### Date 2022-08-11
#### week3 problem set- runoff
昨天看過一回習題思路引導的短片，方知自己對於 runoff 進行方式與選票計算流程有著錯誤的認知。這種 runoff 選制並不會進行多次投票，而是依照唯一一次投票中選民反應的候選人偏好次序來進行逐次淘汰與被淘汰者的那選票效力的重新計算。


## todo list for 08/11 evening
- 找網路影片, 更了解 fread(), fwrite()用法
- 

