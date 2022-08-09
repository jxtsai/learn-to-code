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


### Date 2022-07-25 
週末雖依舊照表操課(主要是觀看課堂影片)，但在記錄心得筆記與習題作業練習就無法維持專注積極。
因為覺得已讀完課堂筆記，所以課堂影片就是不專心地讓它自動播放，另外也跑完中文導讀影片。中文講師在後半部解釋 C 語言資料型態 (例如 整數佔 4 個 bits, 如何表示 負數)，自己聽得有點亂。這似乎也是當年雖然試圖以 C 語言作起手，但又很快放棄宅的原因吧。
不過最大的收獲是，提醒了自己即便把第一週的作業題給作出來，但有些狀況根本沒考慮到(例如輸入的整數若為負數怎麼辦)。
週末有大半的精力在找一套好的學習規劃 app，[My Study Life](https://www.mystudylife.com/) 同具行動與網頁版，似乎可以期待一下。
桌機版的 VSC 完美地整合了 github (雖然 codespace 也不錯,但未開放免費，目前只是佔著 CS50 的名額使用著)。

今日上午完成了作業題的第二道簡易版,其代碼如下:

```
//Greedy Algorithms
// quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)

#include <stdio.h>
#include <cs50.h>


int get_cent(){
    int changes = get_int("Many changes owned by customer: \n");
    while (changes < 0){
       printf("It has to be greater than 0.");
       changes = get_int("Many changes owned by customer: \n");
    }

    return changes;
}

int calculate_quarters(n){
    if(n < 25)
    {
        return 0;
    }
    else
    {
        return n/25;
    }

}

int calculate_dimes(n){
    if(n < 10)
    {
        return 0;
    }
    else
    {
        return n/10;
    }

}

int calculate_nickels(n){
    if(n < 5)
    {
        return 0;
    }
    else
    {
        return n/5;
    }

}

int calculate_pennies(n){
    return n;
}

int main(void){
    int n = get_cent();
    int q = calculate_quarters(n);
    n = n - (q * 25);
    int d = calculate_dimes(n);
    n = n - (d * 10);
    int nk = calculate_nickels(n);
    n = n - (nk * 5);
    int p = calculate_pennies(n);
    int coins = q + d + nk + p ;
    printf("%i \n", coins);
}

```

## project


## supplement reading 



