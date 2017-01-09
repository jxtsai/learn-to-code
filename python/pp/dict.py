d={1:'one',2:'two',3:'three', 4: "test", "age": 43, "name": "jx"}
def search(d,v):
    for i in d:
        if d[i]==v:
            return i
    return "the value not found"
v1=raw_input("enter a value to be recorded: ")

print(search(d,v1))