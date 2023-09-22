'''
This is my code from scratch , well somehow 


'''


header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""
print(header)
print("****************************************")
print(" Add your todo task here: ")
tasks_list = []
task = input(">")


while task != "q":
   
    tasks_list.append(task)
    print("Here is your todo items: ")
    for a in tasks_list:
        print(f"{tasks_list.index(a) + 1}) {a}") 
    print(" Add your todo task here: ")    
    task = input(">")


print(f"Today you completed {len(tasks_list) - 1} todos: ")
for a in tasks_list[:-1]:
        print(f"*. {a}") 

