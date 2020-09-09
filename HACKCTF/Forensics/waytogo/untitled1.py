import sys

result = ""
f1 = open("C:/Users/user/Desktop/포렌식/waytogo/text.txt","r")
f2 = open("answer.txt","w")

line = f1.readline()
string = line.split(" ")
l = len(string)
print(l)
for i in range(0, l):
    result += string[l-i-1]
f2.write(result)

f1.close()
f2.close()
