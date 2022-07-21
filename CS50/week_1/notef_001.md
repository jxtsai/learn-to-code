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
### Date 2022-07-21
課程筆記閱讀，開始介紹 C 語言，並利用第 0 週教過的 Scratch 作對比。雖然不是第一次使用網頁版的 VSC，但卻是初次使用 github codespace 功能，這個雲端的 IDE 感覺超酷的(雖然自己的筆電已經很老舊)

本週課程的重點在於學習 C 語言，這也是我"當年"(2015年左右)嘗試學習的第一種程式。後來之所以很快放棄的原因是，每次要設定變數前還得宣告變數的資料型態，然後想看看自己寫的語法內容是否正確執行檔案之前又得先 compile，修改檔案後又得重複 compile.....好麻煩哦.....
讀筆記內心的 OS 是崩潰的哈佛優等生居然都可以在三小時的課堂學完程式語言的基本概念: 變數、運算、條件、迴圈、函數......，實在太強大了。

利用一個上午的時間(大約二小時)，看完了課堂筆記，借光首次試用 github codespace，一用立即感到 驚為天人，因為雲端的開發環境比網頁版的 VSC 多出了 terminal 功能 ，幾乎就跟桌面版一模一樣，真的很方便。想來如果在 Chrome OS 使用，大概可以滿足我這種初學者的全部開發環境需求。

下午繼續利用 [codespace](https://github.com/code50/8361268) 來作 problem set，大概也是花了近六七十分鐘才完成簡版 mario 的階梯式迴圈解法。
[code]
```int main(void)
{
    int h = get_int("height: \n");
    for (int i = h; i > 0; i--)
        {
            for (int j = 0; j < i; j++)
            {
                printf(" ");
            }
            for (int k = 0; k <= h - i; k++)
            {
            printf("#");
            }
         printf("\n");
     }

}

````

想想先用圖紙把問題分析一下，並在多種不同(錯誤)方式的來回測試之間，的確是蠻有趣的。

## project


## supplement reading 



