#CS50 week_3
- Date : Agust6th ~ August 21th
- https://cs50.harvard.edu/x/2022/weeks/5/
- 中文導讀

## 本週目標
- pointers
- 

## Content:  145 mins
### Memory /pointer / address



## 完成進度
請登入 https://ticktick.com

## my notes
### Date 2022-08-12
昨天試著作了一點 C 語言 file function 的語法練習，不過還是搞不太懂其中的 fread/ fwrite 要怎麼使用，其和 fscanf / fprintf 有什麼不同？試著查一下網路其它的教學文，但多有看沒有懂。但是有一點我覺得蠻關鍵：fread/fwrite 可以用在 bitsware，而 fscanf/ fprintf 則是適用於 ASCII 系統。因為 week4 作業會處理到 wav/jpg 聲音與圖像檔案，這也大概是為什麼助教有稍微提及 fread/ fwrite 但沒介紹  fscanf/ fprintf 的綠故吧。

說是這樣說，想是這樣想，但我還是不會運用 fread/fwrite，故回家又重新看了一遍助教短片 file pointer 對這二個 function 的介紹。除此之外，自己就未再作什麼練習。

本週的學習熱情明顯下降，這不只是來到第五週的倦怠，恐怕是因為 week3 習題二尚未解開的挫敗感，讓自己的學習信心有點崩坍吧。
 

#### File handling in C
keep learning function for file operations 

- fscanf() - reads a set of data from a file
- fread() - fread(<buffer>, <size>, <qty>, <file pointer>) 
- fprintf() - writes a set of data to a file
- fwrite() - fwrite(<buffer>, <size>, <qty>, <file pointer>) 

今天的目標是先利用 fread/ fwrite 學會複製檔案。不知道 bmp 的資料形態是什麼，需要多少數量，但試著	操作看看，雖是成功地新生成一個 bmp 檔案，但開啟內容卻是黑麻嘛一片....

試著讀關於各種[檔案格式](https://docs.fileformat.com/) 的文件，雖然透過文件說明好像有點模模糊糊的想像，但還是弄不明白所謂的 head 


## project
### Date 2022-08-12

#### week4 lab : wav format volume
按文件說明，wav 可分為二部份，一為 head 應是記錄檔案的基本資料(類似 metadata 之類的?)，另一個則是由 sample 樣本組成的序列。如按此結構，則 head 部份可以原封不動地複製到新檔案，而聲音樣本部份，則是透過 while loop 把它 2bytes 2bytes x 2 ?但我還是不知道2byte sample datatype. sizeof 要怎麼表達.....

## todo list for 08/11 evening
- 找網路影片, 更了解 fread(), fwrite()用法
- 

