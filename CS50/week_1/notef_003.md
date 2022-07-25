#CS50 week_1
- Date : July 21th ~ 31th
- https://cs50.harvard.edu/x/2022/weeks/1/
- 中文導讀

## 本週目標
- C 語言
- review scratch
- 

## Content:  148 mins
    C: Array
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
### Date 2022-07-25 
週末雖依舊照表操課(主要是觀看課堂影片)，但在記錄心得筆記與習題作業練習就無法維持專注積極。
因為覺得已讀完課堂筆記，所以課堂影片就是不專心地讓它自動播放，另外也跑完中文導讀影片。中文講師在後半部解釋 C 語言資料型態 (例如 整數佔 4 個 bits, 如何表示 負數)，自己聽得有點亂。這似乎也是當年雖然試圖以 C 語言作起手，但又很快放棄宅的原因吧。
不過最大的收獲是，提醒了自己即便把第一週的作業題給作出來，但有些狀況根本沒考慮到(例如輸入的整數若為負數怎麼辦)。
週末有大半的精力在找一套好的學習規劃 app，[My Study Life](https://www.mystudylife.com/) 同具行動與網頁版，似乎可以期待一下。
桌機版的 VSC 完美地整合了 github (雖然 codespace 也不錯,但未開放免費，目前只是佔著 CS50 的名額使用著)。

第 0 週的作業要求是利用直覺式圖示積木組合 Scratch 作練習。不知為何，自己蠻討論 GUI的程式，不管是程式本身要求作出 Graphic 效果或是 scratch 這種完全無需代碼著重思考邏輯訓練的學習方法。不過還是利用早年(五六年前)自己曾經作過的作業，重新地溫習了下 scratch 的玩法。
  
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

這道題目自己是先以 python 來解，一開始的想法是寫一支 functions, 它接受二個參數，第一個參數是硬幣的幣值，第二個是輸入的零錢值
此函數則會返回硬幣數量與扣除後剩下的餘數(tuple形態)
這個算法和上述在解題指引中，建議分別先寫出四種硬幣最大能返還的量目
然後再透過餘數作為不同幣值數量計算函數的參數, 應是相同的意思

```
def get_change(m, cents):
    coins = (int(cents/m))
    remain = cents % m 
    return coins, remain
    
try: 
    while (t = True):
        cents = int(input("Owned by customer: "))

except:
    print("Not string for input")
    

myquarter = get_change(25, cents)
mydime = get_change(10, myquarter[1])
mynickel = get_change(5,  mydime[1])


total_coin = myquarter[0] + mydime[0] + mynickel[0] + mynickel[1]

print(total_coin)


```

## project


## supplement reading 



