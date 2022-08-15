#CS50 week_5
- Date : Agust15th ~ August 28th
- https://cs50.harvard.edu/x/2022/weeks/5/
- 中文導讀

## 本週目標
- pointers
- 

## Content:  132 mins
### Data Structures



## 完成進度
請登入 https://ticktick.com

## my notes
### Date 2022-08-15
上週末有點"發荒"，因此再次偷跑地先看一部份 lecture 講堂影片，進度大概到 linked lists 的部份，但聽到 lists 自己也差不多迷糊 get lost 跟不上內容了。所以今日白天的重點還是在於趕緊把課堂筆記讀過一篇，看看能否強化對於 C 語言資料形態的理解。

另外上週開始讀指定教材之一《[How computers work ](https://archive.org/details/howcomputerswork0009whit) 》，第一部份講電腦硬體設計，沒想到是從最基本的電子電流電磁開始講起。雖然讀起來有點吃力，但還是蠻有趣的，試著去了解這些最底層基礎的內容。

草草地先讀過一遍課堂筆記，再回想一下講座影片：為什麼要介紹 linked lists ，從陣列 array (固定數量要如何改變其數量=> malloc() array, free array , 再次malloc 變更的 array 內含數量, 暫存成另一個 array, copy 暫存 array 給原來之 array 以改變其內含之數量.....。或是利用另一個 function: "realloc()", 但二者程序及要寫的代碼長度也差不多一樣麻煩)

因此到了本週，融貫目前學過的 pointer, struct 等觀念， David 介紹 linked lists 的寫法，其優點將是可以更快地 "insert/ delete" 序列中的元素

#### linked list
linked list 每一個"單元"其實佔了二個記憶體位置，一個是記錄其 value，一個是記錄下一個值的位置，我們將這樣的組合稱之為 nodes, 其資料結構定義如下:

```
typedef struct node
{
    int number;
    struct node *next; // node *next, 
}
node;

```
自定義 node datatype 第一個欄位是整數值此處以變數 number 代之。第二個欄位則是 "struct node \*next" 不完全理解這一行的意思。( a pointer to the next node with struct node : struct node 為資料形態宣告, \*表示其為 pointer, next示意為指向後一位 number的位置? 感覺在自定node struct 裏頭再使用 struct node 有點 recursion 的味道????) struct 第二行原本應寫為 "node \*next", next 為變數名, 表示下一個, 而 node 為此變數之資料類型, \* 則代表宣告 next 為一個pointer 

初次宣告 list
```
node *list = NULL;
```
此時先把 list 指定為 0 (pointer在宣告時都要給它指派一個地址, 否則記憶體容易出錯)

```
node *n = malloc(sizeof(node));

```

n 為一個暫存用的 node, 其第一個欄位的值即為新插入的 value, 第二欄 pointer 指向NULL; 


## project
### Date 2022-08-12

#### week4 lab : wav format volume
按文件說明，wav 可分為二部份，一為 head 應是記錄檔案的基本資料(類似 metadata 之類的?)，另一個則是由 sample 樣本組成的序列。如按此結構，則 head 部份可以原封不動地複製到新檔案，而聲音樣本部份，則是透過 while loop 把它 2bytes 2bytes x 2 ?但我還是不知道2byte sample datatype. sizeof 要怎麼表達.....

### Date 2022-08-15
上週五回家後看過 lab walkthrough 影片，跟著作完了 volume scale mamulpating 操作。其代碼寫法，和我在腦海中想像的流程一樣，但自己對 fread/fwrite 的語法(特別是前三個參數)的定義還是感到有點迷。

認真地再看一次 week4 problem set 對於 bitmap 檔案結構的說明:
- 檔案終歸是一連串 bit 的排序組合
- 24 bits bitmap 格式,表示其 8bit 代表 Red, 8bit 表示 Green, 剩下的 8bit則是 Blue。既然紅色可能有 255 種深程度淺表達(2的8次方-1)，總三原色計算起來不就有16,777,216 色。
-  bitmap 檔案有二個 header 來儲存該檔案的 metadata, 第一為 BITMAPFILEHEADER (14bytes long)，第二為 BITMAPINFOHEADER (40bytes long)
-  header 之後即為正體的內容，由利用 bit 代表 RGB 之深淺。每 24bit 代表單一像素之色彩。
- bitmap 像素組合可視為一個二維陣列(two dimension arrays)

綜上所述，如何"改造"原本的 bitmap 檔案?
- BITFILEHEADER/ BITMAPINFOHEADER 利用 fread/fwrite 讀取寫入, 不須更動其內容
- 24 bit 的色彩組合 ==> GRBTRIPLE, a datatype struct defined in bmp.h 
- pixel[height][width]



## todo list for 08/15 evening
- watching walkthrough video of week4 problem set
- video shorts for linked lists



