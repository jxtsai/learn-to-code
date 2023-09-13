import sys

header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""


if sys.argv[1] == "add":
    with open("list.txt", "a+") as file: 
        file.write(sys.argv[2]+"\n")
        
elif sys.argv[1] == "remove":
    with open("list.txt", "r+") as file: 
        content = file.readlines()
        item = int(sys.argv[2])-1
        content.remove(content[item])
        with open("list.txt", "w+") as file:
            for todo in content:
                file.write(todo)
        
with open("list.txt", "r") as file: 
    content = file.readlines()
    print(header)
    print("Here is your ToDo tasks: "+"\n") 
    for idx, line in enumerate(content):
        print(idx+1, line.rstrip())        
    
    print()    
    print("***********************************")    
