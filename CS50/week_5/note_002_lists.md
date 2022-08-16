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
### Date 2022-08-16
昨天看了一下課堂筆記，有點明白又沒完全明白 linked lists 的語法設計，於是回家後先安排看了輔助短片 singly linked lists。但這支短片並沒有從頭仔細介紹 linked lists，而是著重在介紹 linked lists 常會被運用的場景與function 寫法: 

- create list 
- insert elements from list
- delete  element from list
- delete whole list
- .......

於是又去找了中文導讀課程影片，但同樣的講者也未在此部份提供過多的著墨。不過他倒是提供了一些補充資料的連結
- [演算法與資料結構](https://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html) 



#### linked list


初次宣告 list,但又不是宣告 node datatype 而是一個指向 node datatype 的 pointer
```
node *list = NULL;
```
此時先把 list 指定為 0 (pointer在宣告時都要給它指派一個地址, 否則記憶體容易出錯)

```
node *n = malloc(sizeof(node));

```

n 為一個暫存用的 node, 其第一個欄位的值即為新插入的 value, 第二欄 pointer 指向NULL; 


今天 codespace 恢復正常後，練習 linked lists 的寫法，一邊寫一邊試著再好好理解這些代碼的意義。依樣畫孤地寫了創建 linked list 的語法，然後試著在此列表中加入一個元素，然後把可以 print 來看看會打印出什麼東西。

```
    printf("%i \n", n -> value);
    printf("%p \n", list);
    printf("%p \n", n);
	printf("%p \n", list -> next);
	printf("%p \n", n -> next);
    printf("%p \n", &n);
    printf("%p \n", &list);

```

 print out as :

    1 // n 所指向位置  0x562748e142a0 其存入的值為 1 (同 printf("%d \n", list -> value);)
    0x562748e142a0  // n = list , 顯印出此二個 pointer 所指的位置為同一處
    0x562748e142a0 
	(nil) // node 第二欄 pointer 目前指向 null ,表示其為列素的最後
	(nil)  
    0x7fff08355ab8 // n 本身所佔的記憶體位置
    0x7fff08355ac0 // list 本身所佔的記憶體位置 ,可看到兩者有所不同
	

這兩週明顯感到自己學習上的疲乏，也許該暫停一下轉到 python ? (OS: 其實正確該做的是完成 week3 problem set - runoff / week4 problem set BMP file manupluation)


## project


### Date 2022-08-16
今天早上看了一遍 week4 problem set walkthrough 影片,  pixel 如何表示於圖片，和我所推測的二維array 結構相符，也更清楚如何利用已定義好的 struct 來取得 pixel 三原色的值

不過昨天 github codespace rebuild 遇到問題，導致 make 指令無法使用，有點頭痛，今天總算恢復正常。







