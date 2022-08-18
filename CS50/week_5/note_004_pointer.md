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
### Date 2022-08-18

因為對於 linked list 還是有許多疑惑，昨天找了 CS50 課程指定讀本《programming in c 4th edition》來看看。老實說自己看過有限的 C 語言教學文字材料裏頭，能夠讓我看懂的真是少之又少。這本 programming in c 倒是能讓我讀得下去(雖然許多文字述敍還是會讓我感到煩燥)，想來不只是這本書編寫的清楚，有一部份也該歸功於過去四五
週來透過 CS50  自學，算是讓自己對於 C 語言有一點點的進步吧。
CS50 大概是一學期三學分的通識課，老師上課速度已經夠快了，想來即便是哈佛的天之驕子，除了光聽課外也勢必要透過一些輔助教材來跟上內容進度，所以對於開始認真看課本的自己，應該覺得出息了才是。


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
