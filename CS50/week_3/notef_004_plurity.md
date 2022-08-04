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
### Date 2022-08-04
昨天休假在家仍不忘學習，不過在家裏房間學習(特別是寫代碼與用電腦打心得筆記)的效果似乎還不如在辦公室，一來在是家裏太容易被其它事物分散注意力(如電視或 podcast)二來是心態上好像覺得在家應該就是要放鬆躺平。不過放任頭腦這樣無所事事到了下午傍晚，終於覺得該來想一想 week3 的第二道進階習題。或者這幾週密集式的自學訓練，也讓自己接受了這種如何利用時間思索數理性質問題的方式。
話說前天自己想出來的 collatz recursion 寫法，結果還是和"標準答案"不一樣，心裏有點涼了.....還是沒有充分把 recursion 觀念運用在二種會發生的情況作出不同又類似的 recursion(把 recursion 用在最後的 return 而以,且最後已完成判斷式，所以這個 recursion 就不夠elegant...)


## project
### Date 2022-08-04
problem set Plurality 解題思路
plurity 習題中，一一要克服的是
1. 如何讓使用者輸入候選人名字，且將之記錄起來（儲在一個 array）或是直接利用 command line arguements 輸入功能(argv[]) 
2. 如何讓選民一個一個投票（輸入先前候選人名字），且記錄每一次票 (string votes[voters]; 原本試著把這部份移作為另一段函數，但後來才知道 C 語言的函數無法輕易地傳回 array)
  - 需要檢查機制, 選票數量為 int and  >0
  - 確認選票上的名字 ?
  
3. 如何計算候選人的得票數，並找出其中最高票者:似乎要用到二次內迴圈，若只先計算某一候選人，則是一次 lopp(作一支小函數 count 來計算個各得票數, 但麻煩之處在於還是要 loop 一次候選人名單, 再統合計算誰的票數最高,有點麻煩）

4. 利用 struct ? (候選人: count), 但似乎仍無法解決 datatype 無法在 function 回傳的麻煩
5. 最後的解法是利用 max_count 變數來暫存 for loop 哪一位候選人的票數最高, 再把勝出者的名字打印出來。

#### 總檢討上述的解題思維的缺點
- 似乎仍是先射箭再畫靶，沒依照作業指引提供的 function 編寫提示。
- 如果遇上 user 不按牌理的輸入(例如不在選票上的名字等等，可能結果或執行就會出錯)
- main function 內容過於繁瑣，因要處理 C 語言function 無法回傳 array, 所以都擠在這裏了


#### CS50 助教提示的代碼安排
- 自定一個 candidate 資料形態, 其包含 1. string name (候選人名字); 2. int votes (其得票數)
- function vote(name) : 傳入某位候選人的名字, 傳回值為 true (如果 name 為某位參選者)
- function print_winner : 印出票數最高者, 有可能是一位以上 



