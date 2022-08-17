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
### Date 2022-08-17

昨天白天想繼續攻克 C 語言中 linked lists 的觀念與相關代碼寫法，似乎未完全熟練。回家再重看輔助短片 -- singly linked lists，助教解釋了 linked list 如何: 

- 建立新創一組 linked list
- 插入(通常是把新節點 node 放入第一位)
- 如何進行搜尋
- 刪除其中某個節點 (建議還是利用 double linked list)
- 刪除整串列表

但上述的操作只提到 psuodocode 與步驟，並未看到完整的代碼內容，所以自己還是有點害怕: 不知道怎麼把這些 function 給寫出來..... 

為了釐清對 linked list 的觀念，今早重新找回 CS50 課程指定讀本《programming in c 4th edition》，以多了解 C 語言的基本概念。

### pointer to struct  
先從 pointer 看起，才知道原來 "->" 乃是專用在指向 struct 的指標符號，其原本的寫法應是:

 ```
    // 自定一個 date 的資料類型 
    typedef struct
    {
        int month;
        int day;
        int year;
    }
    date;

    date todays; //宣告一個 date 類型的變數 todays
    date *todaysPrt = &todays;  //宣告一個指向 todays 的 struct pointer
    (*todaysPrt).month = 8; // assign 8 給 todays.month,即 (*todaysPrt).month(indriectly assign)
	 
 ```
    其中最後一行 (*todaysPrt).month = 8;
	可以改為: todaysPrt->month = 8;

### structures containing pointers ( pointer in struct)  

```
    typedef struct
    {
        int *prt1;
        int *prt2;
    }
    intPrt;

    intPrt myprt; // 宣告一個 intPrt 資料類型的變數 myprt
    int ps1 = 10;
    int ps2 = 5;
    myprt.prt1 = &ps1; //將 myprt 第一欄的 pointer 指向 ps1
    myprt.prt2 = &ps2; //將 myprt 第二欄的 pointer 指向 ps2
    *myprt.prt2 = 100; // 將 myprt 第二欄的 pointer 所指向的值改為 100
	// 記得此處 不能改寫為 myprt->prt2 因為 myprt 本身並不是 pointer, 雖然其內容為帶兩個 pointer ,但性質為一個 intPrt 的資料類型
    printf("prt1 %i; ps1: %i\n", *myprt.prt1, ps1);
    printf("prt2 %i; ps2: %i\n", *myprt.prt2, ps2);

```


### linked list


從上述了解所謂的 pointer to struct 與 struct containing pointer 之不同，以及"->" operator 的用法之後，再重新回來看 linked list 似乎就清楚許多


```
    typedef struct node
    {
        int value;
        struct node *next;
    }
    node;

    node n1, n2;
    n1.next = &n2;
    n1.value = 10;
    n2.value = 200;
    printf("n1 value: %i \n", n1.value);
    printf("n2 value: %i \n", n2.value);
    int i = n1.next->value;
    printf("i: %i\n", i);
```

## project


### Date 2022-08-16
今天早上看了一遍 week4 problem set walkthrough 影片,  pixel 如何表示於圖片，和我所推測的二維array 結構相符，也更清楚如何利用已定義好的 struct 來取得 pixel 三原色的值

不過昨天 github codespace rebuild 遇到問題，導致 make 指令無法使用，有點頭痛，今天總算恢復正常。




