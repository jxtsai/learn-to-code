import sys

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
    for idx, line in enumerate(content):
        print(idx+1, line.rstrip())        
