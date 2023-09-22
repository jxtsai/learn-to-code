"""
do-to list app with a txt file update
using command line arguments as input method

文字指令介面的 todo list append
CL 可輸入待辦事項即更新於printout 與某個純文字檔案
刪除功能為數字 

todo items = list data structure?

"""
import sys


someth = input("Remeber to do: ")
todo_list = []

with open("list.txt", "w") as file:
    file.write(someth)

with open("list.txt", "r") as file:
    content = file.read()
    print("My Todo list: ")
    print(content)



for arguement in sys.argv:
    print(arguement)


    
    