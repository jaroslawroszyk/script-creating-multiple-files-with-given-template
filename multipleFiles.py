fileWithTemplate = open("template.txt",'r')
template = fileWithTemplate.read()

numberOfFiles = input("Enter how many files do you want create: ")
nameOfFiles = input("Enter name of file: ")
givenExtension = input("Enter extension on file: ")
for x in range(1, int(numberOfFiles) + 1):
    file = open((nameOfFiles+"%s."+givenExtension) % x, 'w')
    file.write(template)
    file.close()

fileWithTemplate.close()

