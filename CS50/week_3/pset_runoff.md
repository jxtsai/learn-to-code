#CS50 week_3
- Date : July 30th ~ August 12th
- https://cs50.harvard.edu/x/2022/weeks/3/
- 中文導讀

## Note for problem set - runoff election

1. custom data struct: candiate(as in plurality), ballot ?
2. function : need for several times
   - 發票與記錄(參選人應會漸減): arguements: candiates參選人名單, 選民人數, .... , return ???
   - count ballots: arguement ballot[][],  return ?? 無法傳回 array
   - eliminate candidate: arguement name of candiate return bool
   - call for next round: 應是再叫呼叫"發票與記錄"這支函數 (recursion until cadidate is one?)



### instruction from CS50
1. ballot two dimensions arrays ex ballot[0]["Amy", "David", "Tom"]
   first index: votes (how many voters : max 100)
   sec index: candiates (max 9 candidates and its index reflecting voter's preference, index 0 scored hightest)
   如何計算選票(a function to caculate ballot[x][y] x-1 張選票的 y )

2. self defined data struct: candidate with three fields, the third one eliminated ( bool)
   第三欄 bool value 的作用? 決定是否進入 next round ballot