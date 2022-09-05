
print("File two __name__ is set to: {}" .format(__name__))


def function_three():
   print("Function three is executed")



if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")