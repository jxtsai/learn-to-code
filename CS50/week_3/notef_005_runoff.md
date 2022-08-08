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

### Date 2022-08-05
回家重看了 week3 四支介紹 search / sort 的短片，才發現其中藏著許多過去自己未曾注意到的細節。例如 search 在找到符合條件的第一個元素程式就會停止，不會再繼續檢查後面的資料，而排序則是會從頭到尾地檢查過(即使該物件集合已是排序好)確認已正確依序。
因此 selection sort / bubble sort 所花費的時間是差不多 (Big O(n二次方); Ω(n))，但bubble sort 若遇上倒序資料則會比 selection 花更多時間。至於這三種最佳最快的 merge sort (Big O(n x log n); Ω(log n))


## project
### Date 2022-08-04
既然姑且把 pluraity 習題作出來(雖然還需要再依作業提示重寫，但想先來作 runoff, 而不是一直繞在第一道。
延續昨天對於 problem set 第二題 runoff 之思考，其與 plurality 主要的差別在
1. 每張選票上呈現的是選民對於 n位候選人偏好的排名，而非只有一個名字
原本此處的選票只是用 votes[voters] array, 但在 runoff 的選票有 ranking 1~3, 故其 ballot 或需採 datatype struct ?
先試著寫出 ballot 的資料型態, 應該為只有一個 rank(array)之型態 
ballot size 則為由 user 輸入的" voters
    int voters = get_int("How many number of votes? \n");

雖然把 選票的資料形態與收集 user 的投票記錄給寫出來了
但感覺要這樣的寫法來計算選票,會把 main 寫得亂七八糟,尤其是不只到把 recursion 放在何處

2. 得票最多者，其票數要超過 50%，否則就要進入第二輸投票。而前一輪中得票最少者無法參加 第二輪。若第二輪仍無人取得 50％，則如前一輪再淘汰一名進入第三輪直到有人取得 50％之選票。
3. 關鍵點：選票的 data struct (data type) 如何設計？選票計算過程如何運用 recursion?
   base case : 
   recursion case

