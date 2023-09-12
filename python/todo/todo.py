"""
do-to list app with a txt file update
using command line arguments as input method

文字指令介面的 todo list append
CL 可輸入待辦事項即更新於printout 與某個純文字檔案
刪除功能為數字 

todo items = list data structure?

"""
import sys

   
with open("list.txt", "a") as file:
    if sys.argv[1] == "add":
        file.write(sys.argv[2]+"\n")
    if sys.argv[2] == "remove":
        todo_list = file.readlines()
          


with open("list.txt") as file:
    todo_list = file.readlines()    
    for i, d in enumerate(todo_list):
        print((i+1), d.rstrip())


    
    