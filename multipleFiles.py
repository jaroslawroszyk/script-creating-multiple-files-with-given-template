fileWithTemplate = open("template.txt",'r')
template = fileWithTemplate.read()

numberOfFiles = input("enter how many files do you want create: ")
nameOfFiles = input("enter name of file: ")

for x in range(1, int(numberOfFiles) + 1):
    file = open(nameOfFiles+"%s.cpp" % x, 'w')
    file.write(template)
    file.close()

fileWithTemplate.close()

