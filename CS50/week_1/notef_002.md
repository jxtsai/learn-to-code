#CS50 week_1
- Date : July 21th ~ 31th
- https://cs50.harvard.edu/x/2022/weeks/1/
- 中文導讀

## 本週目標
- C 語言
- review scratch
- 

## Content:  148 mins
    C
    IDEs, compilers, interfaces
    Functions, arguments, return values, variables
    main, header files, commands
    Types, format codes, operators
    Variables, syntactic sugar
    Calculations
    Conditionals, Boolean expressions
    Loops, functions
    Mario
    Imprecision, overflow

## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-07-22
昨日白天看完了第一週的課堂筆記並寫出二道作業題之一後，晚上就鬆懈許多。但還是勉強再看完了正堂講座影片之外的短片補充敎材(shorts，其實是主要是躍躍欲試剛取貨的 A5牛皮頁封面線圈橫條筆記本)
本週短片共五支，其主題分別為:

- data types
- conditionals/boolean 
- loops
- operators
- comments

昨天看了前四支，但只有 loops/ operators 才較專心(因為 A5 筆記本在手)。睡前則是勉強地把講座影片消耗長度拉到 30 分鐘左右。依稀記得好像講了 C 語言第一支程式(印出  hello world), compilers 的觀念之類的。
第二天大清早還賴在床上之際，半醒不醒地想著作業的進階加分題( mario 左右對稱的階梯迴圈)要怎麼解...

上午雖然把進階加題的代碼寫出來了，但自己對於多重迴捲圈如何控制的關鍵觀念似乎仍未完全摸透，只能靠著把幾個變數改來改去，總算改成答案的樣子而已。不過這些弱點的曝露，正是告誡自己要好好弄懂哪些地方。
```
#include <cs50.h>
#include <stdio.h>

int main(void){
    int h = get_int("Height: \n");
    for(int i = 0; i < h; i++)
    {
         for(int j = 0; j < h-i ; j++) 
        {
            printf(" ");
        }
        for (int k = 0; k < i+1 ; k++)
         {
            printf("#");
         }
        printf(" ");
        for(int j = 0; j < i+1 ; j++)
        {
            printf("#");
        }
        printf("\n");
    }

}

```
## project


## supplement reading 



