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



## 完成進度
請登入 https://ticktick.com

## my notes
### Date 2022-08-04


### Date 2022-08-05
回家重看了 week3 四支介紹 search / sort 的短片，才發現其中藏著許多過去自己未曾注意到的細節。例如 search 在找到符合條件的第一個元素程式就會停止，不會再繼續檢查後面的資料，而排序則是會從頭到尾地檢查過(即使該物件集合已是排序好)確認已正確依序。
因此 selection sort / bubble sort 所花費的時間是差不多 (Big O(n二次方); Ω(n))，但bubble sort 若遇上倒序資料則會比 selection 花更多時間。至於這三種最佳最快的 merge sort (Big O(n x log n); Ω(log n))

不知是否因遇上週末前夕，還是過去衝了三個星期，今天提不起興緻來寫習題代碼，尤其是看到助教所提供的提示模板內容，其排除user錯誤輸入的程序實在太過細緻，這些問題讓只是專注在解決"正常情況"沒有思考過的例外狀況如何防禦(尤其是 C 語言可能會發生的 segament float 之類的)

這個星期只作出了 plurality, 進階的 runoff 沒能完成，看來當初一開始急著讓自己趕進度地超前完成讀筆記與看講座影片，就是怕自己後面的課會跟不上啊....下週或週末再繼續思考 runoff/tiderman 習題吧....

## project
### Date 2022-08-05
昨天下午在檢討了自己對於 problem set pularity 寫法的問題後，重新再依照課方解題指引的提示，練習另一種解題路徑。先從 functuion vote(string name) : return bool  下手。在這個過程會，讓自己有機會更了解"變數"的 scale 要把它們放在何處才能讓其它 function 可以利用。另外，C 語言本身的重重限制，雖然一開始讓我吃了苦頭，但也慢慢體會到如何用最土味基本的方法來對應問題。雖然一開始可能會把代碼寫得又長又肥， 但其好處是讓初學建立對程式運行最基本功的訓練,有點像是一招半式就要打天下的感覺。
 


