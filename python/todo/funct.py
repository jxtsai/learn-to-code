'''
本習題重點
 open() 函數的幾種檔案讀寫模式 : x, a, r, w (+)(b) 的差異
 列表變數是何種局部? 放置位置
 command line arguement (sys.argv[])

'''
    
import sys

header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""

def todos(action = "quit", task=""):
   
    if action == "add":
        with open("list.txt", "a+") as file: 
            file.write(task+"\n")
        
    elif action == "remove":
        with open("list.txt", "r+") as file: 
            content = file.readlines()
            item = int(task)-1
            content.remove(content[item])
            with open("list.txt", "w+") as file:
                for todo in content:
                    file.write(todo)
    else:
         print(" WARNING!!!! add or remove fucntion only")


    with open("list.txt", "r") as file: 
        content = file.readlines()
        print(header)
        print("Here is your ToDo tasks: "+"\n") 
        for idx, line in enumerate(content):
            print(idx+1, line.rstrip())        
    
        print()    
        print("***********************************")    
        
if len(sys.argv) <= 2:
    todos()
else:
    todos(sys.argv[1], sys.argv[2])
