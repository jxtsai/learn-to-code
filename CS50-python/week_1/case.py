def main():
    
    file_name = input("File name:  ")
    hello = file_name.split(".")[1]
    print(hello)
    
    match hello :
       case "jpg" | "jpeg":
          print("images/jpeg")
    #   case "gif":
    #      print("images/jpeg")
    #   case "pdf": 
    #      print("application/pdf")
    #   case "zip":
    #      print("application/zip")
    #   case "txt":
    #      print("text/plain")
    #   case _:
    #      print("Who?")

    

main()
