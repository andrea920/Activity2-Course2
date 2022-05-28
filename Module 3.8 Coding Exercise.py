#open the previous file created
#f = open("samplefile.txt", "r") 

#print(f.read()) #read mode to view the contents of the file on the console

#print(f.readline(43)) #read single line using readline

#for x in f:     #using for loops
    #print(x)

#removing the file from path
import os
if os.path.exists("samplefile.txt"):
    os.remove("samplefile.txt")
else:
    print("The File does not exist")