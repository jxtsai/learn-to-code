#CS50 python week_5 Unit Test
- Date : Sept 1st ~ 3rd
- https://cs50.harvard.edu/python/2022/weeks/5
- 中文導讀

## 本週目標


   



## Content:  144 mins
    Unit Tests
    assert
    pytest
    Testing Strings
    Organizing Tests into Folders
    Summing Up


## 完成進度
請登入 https://app.blitz.do/



## my notes
### Date 2022-09-05

#### __name__
試著讀本週的課堂筆記，花了一點時間了解程式碼最後出現的二行代碼:

```
if __nanme__ == __main__ :
    main()

```
 其作用與目的為何(昏睡中聽著講座影片，不太記得 David 是否有提及與解釋)，找了 freecodecamp 寫的[示範介紹](https://www.freecodecamp.org/news/if-name-main-python-example/)
 理解這二行代碼的意思大概每次執行 python 時， python 的編譯器會自動產生一個叫做 " __nanme__" 的變數，而這個變數即是所執行檔案中的 main() 。之所以會需要寫這兩行程式，是因為 python 常常會套用其它人寫的 modules,  library , packages，而這兩行程式可以讓滙入(import)的 library
 正確執行而不會干擾影響主程式 main() 裏頭的代碼。
 
 
 
## project


### probem set 