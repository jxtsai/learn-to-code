#CS50 week_5
- Date : Agust15th ~ August 28th
- https://cs50.harvard.edu/x/2022/weeks/5/
- 中文導讀

## 本週目標
- data structure in C
- pointers

## Content:  132 mins
### Data Structures



## 完成進度
請登入 https://ticktick.com

## my notes
### Date 2022-08-19
試著利用 git branch 功能把自己作的筆記檔案切成兩個分支。其實之所以需要用的 branch，不過是因為:

1. 把 CS 資料放到 learn-to-code 目錄夾底下，但後者差不多是 6年前開始學習各種程式語言所留下的破碎記錄，想來其時間點就是第一次試著學 CS50 吧。既然當時未曾留下明確的學習記錄，多年後捲土重來當然要繼續在 learn-to-code 底好好好地記上一筆。
2. 雖說把 CS50 歸檔在 learn-to-code 有其正當性，但畢竟 6 7 年前的資料實在太過雜亂無用，自己都有點看不下去，幾週後忽然靈機一動想到：自己不是一直在利用 github 存放學習記錄與試寫程式碼，那何不利用 git 版本分枝功能來把 CS50  以外眼不見為淨又捨不得直接刪的的檔案利用 branch"分隔"-----也就是在同一個 learn-to-code repo 另開一個 CS50 branch。學習使用 git 也差不多七八年，總算有機會好好地來熟悉 git branch 的實務操作。


## project


### Date 2022-08-18
因為這週 github codespace 連番出現問題，所以決定在本地端電腦安裝 C 語言開發環境 (vsc + extension + gcc)，但因為是 windows 作業系統，一整個很麻煩。另一個作法仍是依賴雲端開發環境，找找有什麼 codespace 的無料替代方案，方知 [replit](https://replit.com/) 也有支援 C compiler 的功能，所以一些小程式直接在 replit 
 嘗試即可。



#### pointer as function's arguement and return

照抄地寫了一個搜尋 linked list 是否有某個值的函數 findnode(), 其本身傳回的資料形態也為自定之struct(node)--
即找到相符值所被指之 pointer, 若找不到則傳回列表最後一個 pointer == NULL 訊息

不知是哪裏出錯，如果輸入不存在的數值，系統就會說是 segmentation fault (原來是在 findnode 最後一行寫錯, 正確是 return somevalue = NULL; 而非  return somevalue "==" NULL; )

教科書 linked list 的寫法並未進行 malloc()  / fredd() 動作，這樣沒問題嗎 ? 懷惑........

```
#include <stdio.h>

typedef struct node
{
    int value;
    struct node *next; 
}
node;

node *findnode(node *somevalue, int match)
{
  while(somevalue != NULL)
    {
      if (somevalue -> value == match)
      {
        return somevalue;
      }
      else
      {
        somevalue = somevalue -> next;
      }
    }
  return somevalue = NULL;
}

int main(void) {
  node n1, n2, n3;
  node *startest = &n1;

  int search;
  n1.value = 100;
  n1.next = &n2;

  n2.value = 200;
  n2.next = &n3;
  n3.value = 300;
  n3.next = 0;
  node *hello;
  hello = findnode(startest, 100);
  if (hello != NULL)
  {
     printf ("Found %i.\n", hello->value);
  }
  else
  {
     printf ("Not Found \n");
  }
    
}

```
