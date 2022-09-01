def main():
    i = get_int()
    print(f"the value is {i}")
    
 
def get_int():
    while True:
        try:
            return int(input("the number: "))
        except:
            print("not an integer!")      
 

main()