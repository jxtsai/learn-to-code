file1 = open("TestFile.txt","w")
for i in range(1,10+1):
  if i>1:
    file1.write("-")
  file1.write(str(i))
file1.close()
