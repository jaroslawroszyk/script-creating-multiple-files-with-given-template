# TemplateInsideFile = "#include <iostream> \n\nint main() \n{ \n\n}"
# lines = []
# fileTemplate = open('template.txt','r')
# print(fileTemplate)

temp = open("template.txt",'r')
dupa = temp.read()
print(dupa)


numberOfFiles = input("enter how many files do you want create")

for x in range(1, int(numberOfFiles) + 1):
    file = open("ex%s.cpp" % x, 'w')
    file.write(dupa)
    file.close()

temp.close()