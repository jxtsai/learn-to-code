#CS50 week_3
- Date : July 30th ~ August 12th
- https://cs50.harvard.edu/x/2022/weeks/3/
- 中文導讀

## 本週目標
- C 語言
- 演算法
- 

## Content:  137 mins
### Algorithm
- Searching
-- Big O
-- Linear search, binary search
-- Searching with code

- Structs Sorting
-- Selection sort demonstration
-- Bubble sort demonstration
-- Selection sort
-- Bubble sort

- Recursion
- Merge sort


## 完成進度
請登入 https://ticktick.com


## my notes
### Date 2022-08-01

recursion : 仍然有點模糊 ability for a function to call itself 

### Date 2022-08-02 
星期一白天讀過一篇課堂筆記後，回家看內容重覆的影片專注力果然又下降了。不過因為事先的預習，影片觀看重點則在自己還搞不太清楚的 "recursion"，本週補充教材中有一支 13分鐘的短片，算是蠻清楚地整理寫程式時如何應用 recursion：它的使用條件與情境，透過 recursion 的應用，讓程式碼更為簡潔(但這種簡潔很可能讓初學新手有撞牆感的頭痛)。

另外，昨天在讀筆記時，看到新的資料結構 data struct 語法，雖然可以勉為其難地背下它的定義表達方式，但就是有點小疙瘩。但聽過老師的解釋，data struct 讓使用者可自行在 C 語言中定義一組便於自用的資料型態(等同於 int, float, )，但這個自定的資料結構較不會受到 C 語言對於原有資料形態所佔記憶體大小規定的限制。它也不同於 OOP 程式語言會出現的物件，因為物件(或 class) 可能會有 methods, functions, 但 C 語言的自定資料形態只是用於更方便更系統化地儲存資料。因此它的定義與使用宣示語法，其實就如同在 C 語言中宣告某個變數時要表示清楚其資料形態是一樣的道理。  


## project
### Date 2022-08-02

想了一個上午，終於把助教在 recursion 短片中提到的小習題給解出來。其實一開始利用 while loop 解題時覺得還蠻容易，但若要利用到 recursion 的觀念，則似乎變得有點困難.....
利用 debug50 檢查為什麼我放在函數中的計數器一直傳回 0或1而不是想像其函數執行的次數
後來才發現，如果把計數器放在 local variable, 則 recursive progress 每次都會把它宣告"校正"回 0 
難怪得不到正確的函數執行次數。
 
```
#include <cs50.h>
#include <stdio.h>

int colla(int n);

int main(void)
{
    int n = get_int("number: \n");
    int result = colla(n);
    printf("%i \n", result);
    return 0;
}

int count = 0;
int colla(int n)
{
   if (n==1)
   {
      return count;
   }
   else if (n%2==0)
   {
      count = count + 1;
      n = n/2;
   }
   else
   {
      count++;
      n =3*n+1;
   }
   return colla(n);
}

```

